# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    frontier = util.Stack()
    visited = set()
    if problem.isGoalState(problem.getStartState()):		# check if the starting state is the goal
	return []
    visited.add(problem.getStartState())
    #next = 
    for firstlevel in problem.getSuccessors(problem.getStartState()):	# put the successors of the starter to the frontier
	actions = []
	actions.append(firstlevel[1])
	frontier.push((firstlevel, actions))
    #print "start looking for path"
    while frontier.isEmpty() == False:
    	node = frontier.pop()				# node is a pair object returned where the first element is its state and the second element is the saved actions path
	# node[0] should be the coordinates of the state (int, int)

	if node[0][0] in visited:		#do not re-explore a node on the frontier if already visited by some other path
		continue
	#actions.append(node[1])
	if problem.isGoalState(node[0][0]):
		print "The frontier is: ", frontier.list
		print "goal node is: ", node[0][0]
		print "Found path to the goal: ", node[1]
		return node[1]
	visited.add(node[0][0])
	for successor in problem.getSuccessors((node[0])[0]):
		if successor[0] not in node[1]:
			actions = []
			actions.extend(node[1])
			actions.append(successor[1])
			frontier.push((successor, actions))
			#parent[successor[0]] = node[1]
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
	
    frontier = util.Queue()
    visited = []	#set()
    #costs = {}
    if problem.isGoalState(problem.getStartState()):		# check if the starting state is the goal
	return []
    print "start state is: ", problem.getStartState()
    #visited.add(problem.getStartState())
    visited.append(problem.getStartState())
    for firstlevel in problem.getSuccessors(problem.getStartState()):	# put the successors of the starter to the frontier
	actions = []
	actions.append(firstlevel[1])
	frontier.push((firstlevel, actions))

    while frontier.isEmpty() == False:
	node = frontier.pop()
	if node[0][0] in visited:		#do not re-explore a node on the frontier if already visited by some other path
		continue
	#print "the state is: ", node[0][0]
	if problem.isGoalState(node[0][0]):
		print "The path found is: ", node[1]
		return node[1]
	#visited.add(node[0][0])
	visited.append(node[0][0])
	for successor in problem.getSuccessors(node[0][0]):
		if successor[0] not in visited:
			#print "successor of ",node[0][0], "is: ", successor[0]
			actions = []
			actions.extend(node[1])
			actions.append(successor[1])
			frontier.push((successor, actions))

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    frontier = util.PriorityQueue()
    visited = set()
    #costs = {}
    if problem.isGoalState(problem.getStartState()):		# check if the starting state is the goal
	return []
    visited.add(problem.getStartState())
    for firstlevel in problem.getSuccessors(problem.getStartState()):	# put the successors of the starter to the frontier
	actions = []
	actions.append(firstlevel[1])
	#costs[firstlevel.nextState] = 1
	frontier.push((firstlevel, actions, firstlevel[2]), firstlevel[2])

    while frontier.isEmpty() == False:
	node = frontier.pop()
	#if node[0][0] in costs and node[2] <= costs[node[0][0]]
	if node[0][0] in visited:		#do not re-explore a node on the frontier if already visited by some other path
		continue
	#print "the cost is: ", node[2]
	#print "point is: ", node[0][0]
	if problem.isGoalState(node[0][0]):
		print "The path found is: ", node[1]
		return node[1]
	visited.add(node[0][0])
	cost = node[2]
	for successor in problem.getSuccessors(node[0][0]):
		if successor[0] not in visited:
			actions = []
			actions.extend(node[1])
			actions.append(successor[1])
			frontier.push((successor, actions, cost+successor[2]), cost+successor[2])
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()

    visited = []
    #visited = set()
    #costs = {}
    if problem.isGoalState(problem.getStartState()):		# check if the starting state is the goal
	return []

    visited.append(problem.getStartState())
    #visited.add(problem.getStartState())
    for firstlevel in problem.getSuccessors(problem.getStartState()):	# put the successors of the starter to the frontier
	actions = []
	actions.append(firstlevel[1])
	#costs[firstlevel.nextState] = 1
	frontier.push((firstlevel, actions, firstlevel[2]), heuristic(firstlevel[0], problem)+firstlevel[2])

    while frontier.isEmpty() == False:
	node = frontier.pop()
	#if node[0][0] in costs and node[2] <= costs[node[0][0]]
	if node[0][0] in visited:		#do not re-explore a node on the frontier if already visited by some other path
		continue
	#print "the cost is: ", node[2]
	#print "point is: ", node[0][0]
	if problem.isGoalState(node[0][0]):
		print "The path found is: ", node[1]
		return node[1]

	visited.append(node[0][0])
	#visited.add(node[0][0])
	cost = node[2]
	for successor in problem.getSuccessors(node[0][0]):
		if successor[0] not in visited:
			actions = []
			actions.extend(node[1])
			actions.append(successor[1])
			frontier.push((successor, actions, cost+successor[2]), cost+successor[2]+heuristic(successor[0], problem))
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
