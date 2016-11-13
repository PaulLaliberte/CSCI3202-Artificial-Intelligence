

from ValueIteration import *

def solution_value(curr_state = (0,0), solution_path = [(0,0)]):

    """
    myMDP = GridMDP( [[-0.04, -0.04, -0.04,   +1 ],
                     [-0.04, None,  -0.04,   -1  ],
                     [-0.04, -0.04, -0.04, -0.04]],
                    terminals=[(3,1),(3,2)])
    """

 


    
    try:
    
        utility = value_iteration(myMDP)
        bp = best_policy(myMDP, utility)

        while curr_state not in myMDP.terminals:
            next_state = bp[curr_state]

            curr_state = tuple(map(lambda x, y: x+y, curr_state, next_state))

            solution_path.append(curr_state)


        return (solution_path, len(solution_path))

    except KeyError:
        solution_path.append("Hit wall - stay at current position")
        return solution_path




def solution_policy(curr_state = (0,0), solution_path = [(0,0)]):

    """
    myMDP = GridMDP( [[-0.04, -0.04, -0.04,   +1 ],
                     [-0.04, None,  -0.04,   -1  ],
                     [-0.04, -0.04, -0.04, -0.04]],
                    terminals=[(3,1),(3,2)])
    """



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
    

    
    myMDP = GridMDP([[-.1, -.1, -.1, -.1, -1, -.1, -1, -1, 0, 75],
                    [None, None, -1, -1, -.1, -.5, None, -.1, None, -.1],
                    [-.1, -.1, -.1, -.1, -.1, -.5, None, -.1, -.1, -.1],
                    [None, 2, None, None, None, -.5, -.1, 2, None, -.1],
                    [None, -.1, -.1, -.1, -.1, None, -1, -.5, -1, -.1],
                    [-.1, -.5, None, -.1, -.1, None, -.1, -.1, None, -.1],
                    [-.1, -.5, None, -.1, -1, None, -.1, -1, None, None],
                    [-.1, -.1, -.1, -.1, -.1, -.1, -.1, -.1, -.1, -.1]],
                    terminals=[(9,7)])


    
    myMDP = GridMDP([[-.2, -.2, -.2, -.2, -1, -.2, -1, -1, 0, 75],
                    [None, None, -1, -1, -.2, -.5, None, -.2, None, -.2],
                    [-.2, -.2, -.2, -.2, -.2, -.5, None, -.2, -.2, -.2],
                    [None, 2, None, None, None, -.5, -.2, 2, None, -.2],
                    [None, -.2, -.2, -.2, -.2, None, -1, -.5, -1, -.2],
                    [-.2, -.5, None, -.2, -.2, None, -.2, -.2, None, -.2],
                    [-.2, -.5, None, -.2, -1, None, -.2, -1, None, None],
                    [-.2, -.2, -.2, -.2, -.2, -.2, -.2, -.2, -.2, -.2]],
                    terminals=[(9,7)])

    
    myMDP = GridMDP([[-.3, -.3, -.3, -.3, -1, -.3, -1, -1, 0, 75],
                    [None, None, -1, -1, -.3, -.5, None, -.3, None, -.3],
                    [-.3, -.3, -.3, -.3, -.3, -.5, None, -.3, -.3, -.3],
                    [None, 2, None, None, None, -.5, -.3, 2, None, -.3],
                    [None, -.3, -.3, -.3, -.3, None, -1, -.5, -1, -.3],
                    [-.3, -.5, None, -.3, -.3, None, -.3, -.3, None, -.3],
                    [-.3, -.5, None, -.3, -1, None, -.3, -1, None, None],
                    [-.3, -.3, -.3, -.3, -.3, -.3, -.3, -.3, -.3, -.3]],
                    terminals=[(9,7)])

    
    myMDP = GridMDP([[-.4, -.4, -.4, -.4, -1, -.4, -1, -1, 0, 75],
                    [None, None, -1, -1, -.4, -.5, None, -.4, None, -.4],
                    [-.4, -.4, -.4, -.4, -.4, -.5, None, -.4, -.4, -.4],
                    [None, 2, None, None, None, -.5, -.4, 2, None, -.4],
                    [None, -.4, -.4, -.4, -.4, None, -1, -.5, -1, -.4],
                    [-.4, -.5, None, -.4, -.4, None, -.4, -.4, None, -.4],
                    [-.4, -.5, None, -.4, -1, None, -.4, -1, None, None],
                    [-.4, -.4, -.4, -.4, -.4, -.4, -.4, -.4, -.4, -.4]],
                    terminals=[(9,7)])


    

    myMDP = GridMDP([[-.5, -.5, -.5, -.5, -1, -.5, -1, -1, 0, 75],
                    [None, None, -1, -1, -.5, -.5, None, -.5, None, -.5],
                    [-.5, -.5, -.5, -.5, -.5, -.5, None, -.5, -.5, -.5],
                    [None, 2, None, None, None, -.5, -.5, 2, None, -.5],
                    [None, -.5, -.5, -.5, -.5, None, -1, -.5, -1, -.5],
                    [-.5, -.5, None, -.5, -.5, None, -.5, -.5, None, -.5],
                    [-.5, -.5, None, -.5, -1, None, -.5, -1, None, None],
                    [-.5, -.5, -.5, -.5, -.5, -.5, -.5, -.5, -.5, -.5]],
                    terminals=[(9,7)])

    

    myMDP = GridMDP([[-.6, -.6, -.6, -.6, -1, -.6, -1, -1, 0, 75],
                    [None, None, -1, -1, -.6, -.5, None, -.6, None, -.6],
                    [-.6, -.6, -.6, -.6, -.6, -.5, None, -.6, -.6, -.6],
                    [None, 2, None, None, None, -.5, -.6, 2, None, -.6],
                    [None, -.6, -.6, -.6, -.6, None, -1, -.5, -1, -.6],
                    [-.6, -.5, None, -.6, -.6, None, -.6, -.6, None, -.6],
                    [-.6, -.5, None, -.6, -1, None, -.6, -1, None, None],
                    [-.6, -.6, -.6, -.6, -.6, -.6, -.6, -.6, -.6, -.6]],
                    terminals=[(9,7)])

    myMDP = GridMDP([[-.7, -.7, -.7, -.7, -1, -.7, -1, -1, 0, 75],
                    [None, None, -1, -1, -.7, -.5, None, -.7, None, -.7],
                    [-.7, -.7, -.7, -.7, -.7, -.5, None, -.7, -.7, -.7],
                    [None, 2, None, None, None, -.5, -.7, 2, None, -.7],
                    [None, -.7, -.7, -.7, -.7, None, -1, -.5, -1, -.7],
                    [-.7, -.5, None, -.7, -.7, None, -.7, -.7, None, -.7],
                    [-.7, -.5, None, -.7, -1, None, -.7, -1, None, None],
                    [-.7, -.7, -.7, -.7, -.7, -.7, -.7, -.7, -.7, -.7]],
                    terminals=[(9,7)])


    myMDP = GridMDP([[-.8, -.8, -.8, -.8, -1, -.8, -1, -1, 0, 75],
                    [None, None, -1, -1, -.8, -.5, None, -.8, None, -.8],
                    [-.8, -.8, -.8, -.8, -.8, -.5, None, -.8, -.8, -.8],
                    [None, 2, None, None, None, -.5, -.8, 2, None, -.8],
                    [None, -.8, -.8, -.8, -.8, None, -1, -.5, -1, -.8],
                    [-.8, -.5, None, -.8, -.8, None, -.8, -.8, None, -.8],
                    [-.8, -.5, None, -.8, -1, None, -.8, -1, None, None],
                    [-.8, -.8, -.8, -.8, -.8, -.8, -.8, -.8, -.8, -.8]],
                    terminals=[(9,7)])



    myMDP = GridMDP([[-.9, -.9, -.9, -.9, -1, -.9, -1, -1, 0, 75],
                    [None, None, -1, -1, -.9, -.5, None, -.9, None, -.9],
                    [-.9, -.9, -.9, -.9, -.9, -.5, None, -.9, -.9, -.9],
                    [None, 2, None, None, None, -.5, -.9, 2, None, -.9],
                    [None, -.9, -.9, -.9, -.9, None, -1, -.5, -1, -.9],
                    [-.9, -.5, None, -.9, -.9, None, -.9, -.9, None, -.9],
                    [-.9, -.5, None, -.9, -1, None, -.9, -1, None, None],
                    [-.9, -.9, -.9, -.9, -.9, -.9, -.9, -.9, -.9, -.9]],
                    terminals=[(9,7)])


    myMDP = GridMDP([[-1, -1, -1, -1, -1, -1, -1, -1, 0, 75],
                    [None, None, -1, -1, -1, -.5, None, -1, None, -1],
                    [-1, -1, -1, -1, -1, -.5, None, -1, -1, -1],
                    [None, 2, None, None, None, -.5, -1, 2, None, -1],
                    [None, -1, -1, -1, -1, None, -1, -.5, -1, -1],
                    [-1, -.5, None, -1, -1, None, -1, -1, None, -1],
                    [-1, -.5, None, -1, -1, None, -1, -1, None, None],
                    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]],
                    terminals=[(9,7)])
    

                

    myMDP = GridMDP([[.1, .1, .1, .1, -1, .1, -1, -1, 0, 75],
                    [None, None, -1, -1, .1, -.5, None, .1, None, .1],
                    [.1, .1, .1, .1, .1, -.5, None, .1, .1, .1],
                    [None, 2, None, None, None, -.5, .1, 2, None, .1],
                    [None, .1, .1, .1, .1, None, -1, -.5, -1, .1],
                    [.1, -.5, None, .1, .1, None, .1, .1, None, .1],
                    [.1, -.5, None, .1, -1, None, .1, -1, None, None],
                    [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]],
                    terminals=[(9,7)])

    

    
    myMDP = GridMDP([[.2, .2, .2, .2, -1, .2, -1, -1, 0, 75],
                    [None, None, -1, -1, .2, -.5, None, .2, None, .2],
                    [.2, .2, .2, .2, .2, -.5, None, .2, .2, .2],
                    [None, 2, None, None, None, -.5, .2, 2, None, .2],
                    [None, .2, .2, .2, .2, None, -1, -.5, -1, .2],
                    [.2, -.5, None, .2, .2, None, .2, .2, None, .2],
                    [.2, -.5, None, .2, -1, None, .2, -1, None, None],
                    [.2, .2, .2, .2, .2, .2, .2, .2, .2, .2]],
                    terminals=[(9,7)])

    
    
    myMDP = GridMDP([[.3, .3, .3, .3, -1, .3, -1, -1, 0, 75],
                    [None, None, -1, -1, .3, -.5, None, .3, None, .3],
                    [.3, .3, .3, .3, .3, -.5, None, .3, .3, .3],
                    [None, 2, None, None, None, -.5, .3, 2, None, .3],
                    [None, .3, .3, .3, .3, None, -1, -.5, -1, .3],
                    [.3, -.5, None, .3, .3, None, .3, .3, None, .3],
                    [.3, -.5, None, .3, -1, None, .3, -1, None, None],
                    [.3, .3, .3, .3, .3, .3, .3, .3, .3, .3]],
                    terminals=[(9,7)])

    

    
    myMDP = GridMDP([[.4, .4, .4, .4, -1, .4, -1, -1, 0, 75],
                    [None, None, -1, -1, .4, -.5, None, .4, None, .4],
                    [.4, .4, .4, .4, .4, -.5, None, .4, .4, .4],
                    [None, 2, None, None, None, -.5, .4, 2, None, .4],
                    [None, .4, .4, .4, .4, None, -1, -.5, -1, .4],
                    [.4, -.5, None, .4, .4, None, .4, .4, None, .4],
                    [.4, -.5, None, .4, -1, None, .4, -1, None, None],
                    [.4, .4, .4, .4, .4, .4, .4, .4, .4, .4]],
                    terminals=[(9,7)])

    
    

    myMDP = GridMDP([[.5, .5, .5, .5, -1, .5, -1, -1, 0, 75],
                    [None, None, -1, -1, .5, -.5, None, .5, None, .5],
                    [.5, .5, .5, .5, .5, -.5, None, .5, .5, .5],
                    [None, 2, None, None, None, -.5, .5, 2, None, .5],
                    [None, .5, .5, .5, .5, None, -1, -.5, -1, .5],
                    [.5, -.5, None, .5, .5, None, .5, .5, None, .5],
                    [.5, -.5, None, .5, -1, None, .5, -1, None, None],
                    [.5, .5, .5, .5, .5, .5, .5, .5, .5, .5]],
                    terminals=[(9,7)])

    

    myMDP = GridMDP([[.6, .6, .6, .6, -1, .6, -1, -1, 0, 75],
                    [None, None, -1, -1, .6, -.5, None, .6, None, .6],
                    [.6, .6, .6, .6, .6, -.5, None, .6, .6, .6],
                    [None, 2, None, None, None, -.5, .6, 2, None, .6],
                    [None, .6, .6, .6, .6, None, -1, -.5, -1, .6],
                    [.6, -.5, None, .6, .6, None, .6, .6, None, .6],
                    [.6, -.5, None, .6, -1, None, .6, -1, None, None],
                    [.6, .6, .6, .6, .6, .6, .6, .6, .6, .6]],
                    terminals=[(9,7)])



    myMDP = GridMDP([[.7, .7, .7, .7, -1, .7, -1, -1, 0, 75],
                    [None, None, -1, -1, .7, -.5, None, .7, None, .7],
                    [.7, .7, .7, .7, .7, -.5, None, .7, .7, .7],
                    [None, 2, None, None, None, -.5, .7, 2, None, .7],
                    [None, .7, .7, .7, .7, None, -1, -.5, -1, .7],
                    [.7, -.5, None, .7, .7, None, .7, .7, None, .7],
                    [.7, -.5, None, .7, -1, None, .7, -1, None, None],
                    [.7, .7, .7, .7, .7, .7, .7, .7, .7, .7]],
                    terminals=[(9,7)])

    

    myMDP = GridMDP([[.8, .8, .8, .8, -1, .8, -1, -1, 0, 75],
                    [None, None, -1, -1, .8, -.5, None, .8, None, .8],
                    [.8, .8, .8, .8, .8, -.5, None, .8, .8, .8],
                    [None, 2, None, None, None, -.5, .8, 2, None, .8],
                    [None, .8, .8, .8, .8, None, -1, -.5, -1, .8],
                    [.8, -.5, None, .8, .8, None, .8, .8, None, .8],
                    [.8, -.5, None, .8, -1, None, .8, -1, None, None],
                    [.8, .8, .8, .8, .8, .8, .8, .8, .8, .8]],
                    terminals=[(9,7)])


    """
    


    myMDP = GridMDP([[.9, .9, .9, .9, -1, .9, -1, -1, 0, 75],
                    [None, None, -1, -1, .9, -.5, None, .9, None, .9],
                    [.9, .9, .9, .9, .9, -.5, None, .9, .9, .9],
                    [None, 2, None, None, None, -.5, .9, 2, None, .9],
                    [None, .9, .9, .9, .9, None, -1, -.5, -1, .9],
                    [.9, -.5, None, .9, .9, None, .9, .9, None, .9],
                    [.9, -.5, None, .9, -1, None, .9, -1, None, None],
                    [.9, .9, .9, .9, .9, .9, .9, .9, .9, .9]],
                    terminals=[(9,7)])


    """


    myMDP = GridMDP([[1, 1, 1, 1, -1, 1, -1, -1, 0, 75],
                    [None, None, -1, -1, 1, -.5, None, 1, None, 1],
                    [1, 1, 1, 1, 1, -.5, None, 1, 1, 1],
                    [None, 2, None, None, None, -.5, 1, 2, None, 1],
                    [None, 1, 1, 1, 1, None, -1, -.5, -1, 1],
                    [1, -.5, None, 1, 1, None, 1, 1, None, 1],
                    [1, -.5, None, 1, -1, None, 1, -1, None, None],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
                    terminals=[(9,7)])
    """

    try:
        bp = policy_iteration(myMDP)

        while curr_state not in myMDP.terminals:
            next_state = bp[curr_state]

            curr_state = tuple(map(lambda x, y: x+y, curr_state, next_state))

            solution_path.append(curr_state)


        return (solution_path, len(solution_path))

    except KeyError:
        solution_path.append('Hit wall - stay at current position')
        return solution_path

    

    


    
