"""Read in file"""

import sys
import random

myFile = None



with open(sys.argv[1], 'r') as my_file:
    myFile = my_file.read()

class Matrix(object):
    def __init__(self, matrix, d_dict, r_dict):
        self.matrix = matrix
        self.d_dict = d_dict
        self.r_dict = r_dict



def file_to_matrix(myFile):
    l = list(myFile)
    a = []
    demo_dict = {}
    repub_dict = {}
    matrix = []
    x = 1
    y = 1


    for i in l:
        if i == 'D' or i == 'R':
            if i == 'D':
                demo_dict[(x,y)] = 'D'
                a.append((x,y))
                y += 1
            else:
                repub_dict[(x,y)] = 'R'
                a.append((x,y))
                y += 1
        elif i == '\n':
            matrix.append(a)
            x += 1
            y = 1
            a = []
        else:
            pass

    matrix.append(a)

    return Matrix(matrix, demo_dict, repub_dict)


