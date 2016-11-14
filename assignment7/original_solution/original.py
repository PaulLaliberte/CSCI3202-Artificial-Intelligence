"""Solves for given matrix and gridWorld matrix for assignment7"""

#from ValueIteration import *

from ValueIteration import *
import time


def solution_value():
    """
    myMDP = GridMDP( [[-0.04, -0.04, -0.04,   +1 ],
                     [-0.04, None,  -0.04,   -1  ],
                     [-0.04, -0.04, -0.04, -0.04]],
                    terminals=[(3,1),(3,2)])
    """

    myMDP = GridMDP([[0, 0, 0, 0, -1, 0, -1, -1, 0, 75],
                    [None, None, -1, -1, 0, -.5, None, 0, None, 0],
                    [0, 0, 0, 0, 0, -.5, None, 0, 0, 0],
                    [None, 2, None, None, None, -.5, 0, 2, None, 0],
                    [None, 0, 0, 0, 0, None, -1, -.5, -1, 0],
                    [0, -.5, None, 0, 0, None, 0, 0, None, 0],
                    [0, -.5, None, 0, -1, None, 0, -1, None, None],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
                    terminals=[(9,7)])



    curr_state = (0,0)
    solution_path = []

    solution_path.append(curr_state)

    try:
        utility = value_iteration(myMDP)
        bp = best_policy(myMDP, utility)


        while curr_state not in myMDP.terminals:
            next_state = bp[curr_state]

            curr_state = tuple(map(lambda x,y: x+y, curr_state, next_state))

            solution_path.append(curr_state)

        print solution_path


    except KeyError:
        solution_path.append("Hit wall - stay at current position")

        print solution_path




def solution_policy():
    """
    myMDP = GridMDP( [[-0.04, -0.04, -0.04,   +1 ],
                     [-0.04, None,  -0.04,   -1  ],
                     [-0.04, -0.04, -0.04, -0.04]],
                    terminals=[(3,1),(3,2)])
    """ 


    myMDP = GridMDP([[0, 0, 0, 0, -1, 0, -1, -1, 0, 75],
                    [None, None, -1, -1, 0, -.5, None, 0, None, 0],
                    [0, 0, 0, 0, 0, -.5, None, 0, 0, 0],
                    [None, 2, None, None, None, -.5, 0, 2, None, 0],
                    [None, 0, 0, 0, 0, None, -1, -.5, -1, 0],
                    [0, -.5, None, 0, 0, None, 0, 0, None, 0],
                    [0, -.5, None, 0, -1, None, 0, -1, None, None],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
                    terminals=[(9,7)])

    curr_state = (0,0)
    solution_path = []

    solution_path.append(curr_state)

    try:

        bp = policy_iteration(myMDP)


        while curr_state not in myMDP.terminals:
            next_state = bp[curr_state]

            curr_state = tuple(map(lambda x,y: x+y, curr_state, next_state))

            solution_path.append(curr_state)

        print solution_path



    except KeyError:
        solution_path.append("Hit wall - stay at current position")

        print solution_path


if "__main__" == __name__:
    
    print "Value Iteration - Original Solution"
    print "************************************\n"
    time.sleep(2)

    solution_value()

    print "\n"

    print "Policy Iteration - Original Solution"
    print "************************************\n"
    time.sleep(2)

    solution_policy()

