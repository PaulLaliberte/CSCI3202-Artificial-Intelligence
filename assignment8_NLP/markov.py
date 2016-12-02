"""Using Markov Process, create transition and emission probabilities"""

from __future__ import division
import re


class markovChain():

    def __init__(self):
        self.processed_list = []
        self.transition_count = {}
        self.total_count = {}
        self.transition_prob_dict = {}


    def preProcess(self):
        with open("penntree.tag") as f:
            self.processed_list.append("SSSS")
            for line in f:
                if line == '\n':
                    self.processed_list.append("EEEE")
                    self.processed_list.append("SSSS")
                else:
                    self.processed_list.append(line.rstrip())

    def transition_probabilities(self):
        list_of_tags = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ',
                        'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS', 'NNP',
                        'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR',
                        'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD',
                        'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$',
                        'WRB']
        
        #list_of_tags = ['DT', 'NN', 'CC'] #Check. See if DT == 870.

        #calculate total number of tags
        for i in list_of_tags:
            count = 0

            for j in range(0, len(self.processed_list)):
                tag = re.split(r'\t+', self.processed_list[j])
                try:
                    if i == tag[1]:
                        count += 1
                except IndexError:
                    #start or end of line
                    pass

            self.total_count[i] = count


        #we create a dictionary of dictionaries to hold our
        #transition counts


        for i in list_of_tags:
            self.transition_count[i] = {}
            self.transition_prob_dict[i] = {}

        for i in list_of_tags:
            for j in list_of_tags:
                if j != i:
                    x = {j : 0}
                    self.transition_count[i].update(x)

        for i in list_of_tags:
            for j in range(0, len(self.processed_list)):
                tag = re.split(r'\t+', self.processed_list[j])
                try:
                    if i == tag[1]:
                        try:
                            next_line = self.processed_list[j+1]
                            tag_2 = re.split(r'\t+', next_line)

                            for k in list_of_tags:
                                try:
                                    if k == tag_2[1] and i != k:
                                        self.transition_count[i][k] += 1
                                except IndexError:
                                    #start or end of line
                                    pass

                        except KeyError:
                            pass

                except IndexError:
                    #start or end of line
                    pass

        #calculate the probabilities
        #transmission counts P(Tag_i | Tag_j) = 
        #(all instance where Tag_i appears DIRECTLY after Tag_j) / (total count of Tagj)

        for i in list_of_tags:
            for j in list_of_tags:
                if j != i:
                    self.transition_prob_dict[i] = self.transition_count[i][j] / self.total_count[i]



    def emission_probabilities(self):
        pass


