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
    """
    frontier = util.Stack()
    start_state = problem.getStartState()
    frontier.push((start_state, []))  # Storing the state and an empty list of actions

    explored = set()

    #DFS
    while not frontier.isEmpty():
        state, actions = frontier.pop()
        if state in explored:
            continue
        explored.add(state)

        if problem.isGoalState(state):
            return actions  # Return the list of actions when the goal is reached

        for successor, action, cost in problem.getSuccessors(state):
            if successor not in explored:
                new_actions = actions + [action]
                frontier.push((successor, new_actions))
    print("no path found")
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    frontier = util.Queue()
    start_state = problem.getStartState()
    frontier.push((start_state, []))  # Storing the state and an empty list of actions

    explored = set()

    #BFS
    while not frontier.isEmpty():
        state, actions = frontier.pop()
        if state in explored:
            continue
        explored.add(state)

        if problem.isGoalState(state):
            return actions  # Return the list of actions when the goal is reached

        for successor, action, cost in problem.getSuccessors(state):
            if successor not in explored:
                new_actions = actions + [action]
                frontier.push((successor, new_actions))
    print("no path found")
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    frontier = util.PriorityQueue()
    start_state = problem.getStartState()
    frontier.push((start_state, []), 0)  # Storing the state and an empty list of actions
    costs = {}
    costs[start_state] = 0
    explored = set()

    #UCS
    while not frontier.isEmpty():
        state, actions = frontier.pop()
        if state in explored:
            continue
        explored.add(state)

        if problem.isGoalState(state):
            return actions  # Return the list of actions when the goal is reached

        for successor, action, cost in problem.getSuccessors(state):
            if successor not in explored:
                new_actions = actions + [action]
                costs[successor] = costs[state] + cost
                frontier.push((successor, new_actions), costs[successor])
    print("no path found")
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    frontier = util.PriorityQueue()
    start_state = problem.getStartState()
    frontier.push((start_state, []), 0 + heuristic(start_state, problem))  # Storing the state and an empty list of actions
    costs = {}
    costs[start_state] = 0
    explored = set()

    #UCS
    while not frontier.isEmpty():
        state, actions = frontier.pop()
        if state in explored:
            continue
        explored.add(state)

        if problem.isGoalState(state):
            return actions  # Return the list of actions when the goal is reached

        for successor, action, cost in problem.getSuccessors(state):
            if successor not in explored:
                new_actions = actions + [action]
                costs[successor] = costs[state] + cost
                frontier.push((successor, new_actions), costs[successor] + heuristic(successor, problem))
    print("no path found")
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
