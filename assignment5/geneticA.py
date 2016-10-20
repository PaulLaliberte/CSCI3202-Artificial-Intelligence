
from readfile1 import *
import random
import copy


DEF_INITIAL_POP= 60
DEF_GENERATIONS= 80

def gene(some_matrix):
    """takes matrix and creates gene"""
    geneArray = []
    for i in some_matrix:
        for j in i:
            geneArray.append(j)
    return geneArray


def solutions(geneArray, some_matrix, height):
    district_count = 0
    matrix = []
    while district_count < 8:
        a = []
        point = random.choice(geneArray)
        a.append(point)
        geneArray.remove(point)
        neighbors = get_neighbors(point[1], point[0], len(some_matrix[0]))

        for i in neighbors:
            if i in geneArray:
                a.append(i)
                geneArray.remove(i)

        a.sort()
        matrix.append(a)
        district_count += 1



    for i in geneArray:
        found = False
        neighbors = get_neighbors(i[1], i[0], height)
        for j in matrix:
            for k in neighbors:
                if k in j and found is False:
                    j.append(i)
                    found = True
                else:
                    continue

 
    return matrix




def get_neighbors(x, y, height):

    neighbors = [(y + yi, x + xi)
                     for xi in range(-1, 2)
                     for yi in range(-1, 2)
                     if (0 <= y + yi <= height) and
                     (0 <= x + xi <= height) and
                     not (xi == 0 and yi == 0)]

    return neighbors


def grade(some_matrix, r_dict, d_dict, length):
    how_many_Rs = len(r_dict)
    how_many_Ds = len(d_dict)
    Rs_percentage = how_many_Rs / (how_many_Rs + how_many_Ds)
    Ds_percentage = how_many_Ds / (how_many_Rs + how_many_Ds)
    
    district_scores = []

    for i in some_matrix:
        rep_count = 0
        demo_count = 0
        district_size_score = 0

        if len(i) < length or len(i) > length:
            district_size_score = -1


        for j in i:
            if j in r_dict:
                rep_count += 1
            else:
                demo_count += 1

        if demo_count + rep_count == 0:
            pass
        else:
            cR = rep_count / (demo_count + rep_count)
            cD = demo_count / (demo_count + rep_count)

        gradeR = 0
        gradeD = 0

        if cR > Rs_percentage + .10 or cR < Rs_percentage - .10:
            gradeR -= 1
        else:
            gradeR += 1

        if cD > Ds_percentage + .10 or cD < Ds_percentage - .10:
            gradeD -= 1
        else:
            gradeD += 1

        district_scores.append(gradeR + gradeD + district_size_score)

        #contiguous score
        
    c_score = 0
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    m = copy.deepcopy(some_matrix[:])


    for i in m:
        i.sort()
        for k in i:
            for l in directions:
                if k == 'Connect':
                    pass
                else:
                    c = tuple(map(lambda x,y: x+y, k, l))
                    if c in i and k in i:
                        i[i.index(k)] = 'Connect'
                        break
        length = len(i)
        try:
            if i[length-1] != 'Connect' and i[length-2] == 'Connect':
                i[length-1] = 'Connect'
        except IndexError:
            pass

    solution = True

    for i in m:
        for k in i:
                if k != 'Connect':
                    solution = False

        if solution is True:
            c_score = 50
            break
        

    district_scores[0] = district_scores[0] + c_score #add c_score

    score = sum(district_scores)
    return score


def crossover(matrix1, matrix2):
    #Cross over two matrices
    codons_to_cross = []
    gene1 = gene(matrix1)
    c = 0
    while c < 3:
        x = random.choice(gene1)
        codons_to_cross.append(x)
        c += 1

    #find smallest district
    smallest_district = 100
    for m in matrix2:
        if len(m) < smallest_district:
            smallest_district = matrix2.index(m)

    #cut out codons
    for i in codons_to_cross:
        for j in matrix2:
            if i in j:
                j.remove(i)


    #add in
    for a in codons_to_cross:
        matrix2[smallest_district].append(a)

    return matrix2



def mutate(some_matrix):
    prob = .01
    prob_we_mutate = random.uniform(.05,.0095)
    if prob_we_mutate != prob:
        return some_matrix
    gene1 = gene(some_matrix)
    points_to_swap1 = []
    points_to_swap2 = []
    size = 2
    bool1 = True
    random_pick1 = random.choice(gene1)
    random_pick2 = random.choice(gene1)
    ind1 = gene1.index(random_pick1)
    ind2 = gene1.index(random_pick2)
    if random_pick1 != random_pick2:
        try:
            gene1[ind1+1]
            gene1[ind2+1]
        except IndexError:
            bool1 = False

        try:
            gene1[ind1-1]
            gene1[ind2-1]
        except IndexError:
            return mutate(some_matrix)


        if bool1 is True:
            points_to_swap1.append(random_pick1)
            points_to_swap1.append(gene1[ind1+1])
            points_to_swap2.append(random_pick2)
            points_to_swap2.append(gene1[ind2+1])

            for i in points_to_swap1:
                if i in points_to_swap2:
                    return mutate(some_matrix)

            for a in some_matrix:
                for b in a:
                    if b == points_to_swap1[0]:
                        a.remove(b)
                        a.append((-1,-1))

                    if b == points_to_swap1[1]:
                        a.remove(b)
                        a.append((-1,-1))


                    if b == points_to_swap2[0]:
                        a.remove(b)
                        a.append((-2,-2))

                    if b == points_to_swap2[1]:
                        a.remove(b)
                        a.append((-2,-2))


            for a in some_matrix:
                for b in a:
                    if b == (-1,-1):
                        a.remove(b)
                        a.append(points_to_swap2[0])
                        if len(points_to_swap2) > 1:
                            points_to_swap2.remove(points_to_swap2[0])

                    if b == (-2,-2):
                        a.remove(b)
                        a.append(points_to_swap1[0])
                        if len(points_to_swap1) > 1:
                            points_to_swap1.remove(points_to_swap1[0])


        else:
            points_to_swap1.append(random_pick1)
            points_to_swap1.append(gene1[ind1-1])
            points_to_swap2.append(random_pick2)
            points_to_swap2.append(gene1[ind2-1])

            for a in some_matrix:
                for b in a:
                    if b == points_to_swap1[0]:
                        a.remove(b)
                        a.append((-1,-1))

                    if b == points_to_swap1[1]:
                        a.remove(b)
                        a.append((-1,-1))


                    if b == points_to_swap2[0]:
                        a.remove(b)
                        a.append((-2,-2))

                    if b == points_to_swap2[1]:
                        a.remove(b)
                        a.append((-2,-2))


            for a in some_matrix:
                for b in a:
                    if b == (-1,-1):
                        a.remove(b)
                        a.append(points_to_swap2[0])
                        if len(points_to_swap2) > 1:
                            points_to_swap2.remove(points_to_swap2[0])

                    if b == (-2,-2):
                        a.remove(b)
                        a.append(points_to_swap1[0])
                        if len(points_to_swap1) > 1:
                            points_to_swap1.remove(points_to_swap1[0])


    return some_matrix




if __name__ == '__main__':
    states_to_explore = DEF_GENERATIONS * DEF_INITIAL_POP
    solution_history = []
    solution_grades = []
    populations = []
    scores = []
    x = file_to_matrix(myFile)
    height = len(x.matrix[0])
    count = DEF_INITIAL_POP

    while DEF_GENERATIONS > 0:
        while count > 0:
            y = solutions(gene(x.matrix), x.matrix, height)
            z = grade(y, x.r_dict, x.d_dict, len(x.matrix[0]))
            scores.append(z)
            populations.append(y)
            count -= 1

        sp = zip(scores, populations)
        sp.sort()
        p_sorted = [p for s, p in sp]
        crossover(p_sorted[len(p_sorted) - 1], p_sorted[len(p_sorted)-2])
        rand_mutate = random.choice(p_sorted)
        p_sorted.remove(rand_mutate)
        m = mutate(rand_mutate)
        p_sorted.append(m)
        for i in p_sorted:
            solution_history.append(i)

        DEF_GENERATIONS -= 1


    for i in solution_history:
        z = grade(i, x.r_dict, x.d_dict, height)
        solution_grades.append(z)

    sh = zip(solution_grades, solution_history)
    sh.sort()
    s_sorted = [h for s, h in sh]
    top_score = s_sorted[len(s_sorted)-1]


    print 'Party divisions in population:'
    print '*************************************'
    r = 0
    d = 0
    mr = 0
    md = 0
    majr = 0
    majd = 0
    for p in top_score:
        for q in p:
            for key in x.r_dict:
                if key == q:
                    r == 1
                    mr += 1

        for s in p:
            for key in x.d_dict:
                if key == s:
                    d += 1
                    md += 1
        if mr > md:
            majr += 1
            mr = 0
            md = 0
        else:
            majd += 1
            me = 0
            md = 0


    print 'R: %i' % len(x.r_dict)
    print 'D: %i' % len(x.d_dict)
    print '**************************************'
    print 'Number of districts with a majority for each party:'
    print '**************************************'
    print 'R: %i' % majr
    print 'D: %i' % majd
    print '**************************************'
    print 'Locations assigned to each district:'
    print '**************************************'
    c = 1
    for i in top_score:
        print 'District %i: %s' % (c, i)
        c += 1
    print '**************************************'
    print 'Algorithm applied: GA'
    print '**************************************'
    print 'Number of search states explored: %i' % states_to_explore
    print '**************************************'






    














        







