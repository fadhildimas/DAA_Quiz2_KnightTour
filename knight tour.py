import threading
import time

'''
    * class for defining a problem
    * a problem instance is created with board size(n) and time limit arguments
'''

class Problem:
    def __init__(self, n, timelimit):

        # initial state is set to 1, 1
        self.initialState = [1,1]

        # actions a knight can take is set
        self.actions = [[-2, 1], [-2, -1], [-1, 2], [1, 2],
                        [2, 1], [2, -1], [1, -2], [-1, -2]]
        
        # board size is set
        self.n = n

        # timeout flag for breaking the search algorithm
        self.timeout = False

        # timer initialization
        # timer works on a thread and stopExecution method will be invoked once timelimit is reached
        self.timer = threading.Timer(timelimit, self.stopExecution)
    
    # sets timeout flag to True so that search algorithm finishes with timeout
    def stopExecution(self):
        self.timeout = True
    
    # goal test implementation; checks if the state length is equal to the number of tiles on board
    # an element of a node's state indicates a unique tile that is already visited
    def goalTest(self, state):
        if len(state) == ((self.n)*(self.n)):
            return True
        else:
            return False
