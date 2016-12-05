"""Using Markov Process - HMM, create transition and emission probabilities, use viterbi algorithm."""

from __future__ import division
import csv

class markovChain():

    def __init__(self):
        self.tags_count = {}
        self.words = {}
        self.transition_prob = {}
        self.emission_prob = {}
        self.processed_list = []

    def preProcess(self):
        with open("penntree.tag") as f:
            readfile = csv.reader(f, delimiter='\t')
            self.processed_list.append(['<s>', 'SSSS'])
            for row in readfile:
                if len(row) == 0:
                    self.processed_list.append(['</s>', 'EEEE'])
                    self.processed_list.append(['<s>', 'SSSS'])
                else:
                    self.processed_list.append(row)

        #added an extra </s>
        length = len(self.processed_list)
        self.processed_list = self.processed_list[:length-1]

    def getWordsAndTags(self):
        self.preProcess()
        list(self.processed_list)

        for w,t in self.processed_list:
            #get words
            self.words[w] = None

            #get tags and the count
            if t in self.tags_count:
                self.tags_count[t] += 1
            else:
                self.tags_count[t] = 1

    def tranProb(self):
        #create possible transitions
        for tag1 in self.tags_count:
            for tag2 in self.tags_count:
                add_key = {'%s %s' % (tag1, tag2) : 0}
                self.transition_prob.update(add_key)

        for i in range(0, len(self.processed_list)):
            try:
                tag1 = self.processed_list[i][1]
                tag2 = self.processed_list[i+1][1]
                find_key = '%s %s' % (tag1, tag2)
                self.transition_prob[find_key] += 1
            except IndexError:
                #end of list
                pass

        #calculate prob
        for key,value in self.transition_prob.iteritems():
            x = key.split()
            tag = x[0]
            self.transition_prob[key] = value / self.tags_count[tag]

    def emisProb(self):
        #updating a nested dictionary requires a trick
        for word in self.words.keys():
            add_key = {word : {}}
            self.emission_prob.update(add_key)
            for tag in self.tags_count:
                if tag == 'SSSS':
                    add_another = {tag : 1.0}
                    self.emission_prob[word].update(add_another)
                else:
                    add_another = {tag : 0}
                    self.emission_prob[word].update(add_another)

        #another trick... 
        for word, tag in self.processed_list:
            self.emission_prob[word][tag] += 1 / self.tags_count[tag]


        #add start probs
        self.emission_prob['<s>'] = {'SSSS' : 1.0}
        self.emission_prob['</s>'] = {'EEEE' : 1.0}

        for tag in self.tags_count.keys():
            if tag != 'SSSS':
                x = {tag : 0}
                self.emission_prob['<s>'].update(x)

            if tag != 'EEEE':
                x = {tag : 0}
                self.emission_prob['</s>'].update(x)

    def viterbi(self, sentence):
        V = []
        for i in sentence:
            V.append({})
            
        V[0] = {tag : {"prob": self.emission_prob[sentence[0]][tag], "prev": None} for tag in self.tags_count.keys()}
        # Run Viterbi when t > 0

        for t in range(1, len(sentence)):
            for tag in self.tags_count.keys():
                max_tr_prob = max(V[t-1][prev_st]["prob"]*self.transition_prob[('%s %s' % (prev_st, tag))] for prev_st in
                                                                                self.tags_count.keys())
                for prev_st in self.tags_count.keys():
                    if V[t-1][prev_st]["prob"] * self.transition_prob[('%s %s' % (prev_st, tag))] == max_tr_prob:
                        max_prob = max_tr_prob * self.emission_prob[sentence[t]][tag]
                        V[t][tag] = {"prob": max_prob, "prev": prev_st}
                        break
        
        opt = []
        # The highest probability
        max_prob = max(value["prob"] for value in V[-1].values())
        previous = None
        # Get most probable state and its backtrack
        for st, data in V[-1].items():
            if data["prob"] == max_prob:
                opt.append(st)
                previous = st
                break

        # Follow the backtrack till the first observation
        for t in range(len(V) - 2, -1, -1):
            opt.insert(0, V[t + 1][previous]["prev"])
            previous = V[t + 1][previous]["prev"]

        #remove 'SSSS' and 'EEEE' from opt for printing
        opt.remove('SSSS')
        opt.remove('EEEE')

        print 'The steps of states are: \n' + ' '.join(opt)


if __name__ == "__main__":
    list_of_tests = [ ['<s>', 'This', 'is', 'a', 'sentence', '.', '</s>'],
                      ['<s>', 'Can', 'a', 'can', 'can', 'a', 'can', '?', '</s>'],
                      ['<s>', 'This', 'might', 'produce', 'a', 'result', 'if',
                       'the', 'system', 'works', 'well', '.', '</s>'],
                      ['<s>', 'Can', 'a', 'can', 'move', 'a', 'can', '?', '</s>'],
                      ['<s>', 'Can', 'you', 'walk', 'the', 'walk', 'and', 'talk',
                       'the', 'talk', '?', '</s>']]

    n = markovChain()
    n.getWordsAndTags()
    n.tranProb()
    n.emisProb()

    for test in list_of_tests:
        print "The sentence: " + ' '.join(test[1:len(test)-1])
        print '\n'
        n.viterbi(test)
        print '\n'


