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


class Node:


        # location of node on board
        self.location = None    

        # problem that the node belongs to
        self.problem = problem

        # parent of the node
        self.parent = parent

        # action that is taken to reach this node
        self.action = action

        # if node doesn't have a parent, then it is the root node so its state is initialized with the initial state
        # location is set to initial state as well
        if self.parent is None:
            self.state = []
            self.state.append(self.problem.initialState)
            self.location = self.problem.initialState
        
        # if it is not the root node enters here to set its state and location
        # gets the state of its parent and then current location of the node is appended to state
        else:
            self.state = self.parent.state[:]
            new_x = self.parent.location[0] + self.action[0]
            new_y = self.parent.location[1] + self.action[1]
            self.state.append([new_x, new_y])
            self.location = [new_x, new_y]

# checks if a child node is already in the frontier or not
def isChildInFrontier(frontier, child):
    for node in frontier:
        if node.state == child.state:
            return True
    return False
