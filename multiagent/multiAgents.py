# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        # print action
        "*** YOUR CODE HERE ***"
        minDis = float('inf')
        listFoods = currentGameState.getFood().asList()
        if action == 'Stop':
          return -minDis
        for i in range(len(listFoods)):
          dist = manhattanDistance(listFoods[i], newPos)
          if dist < minDis:
            minDis = dist
        minDis = -minDis
        for state in newGhostStates:
          if state.scaredTimer == 0 and state.getPosition() == newPos:
            return -float('inf')
        return minDis

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        action, score = self.minimax(0, 0, gameState)
        return action
        util.raiseNotDefined()
    def minimax(self, curr_depth, agent_index, gameState):
      if agent_index >= gameState.getNumAgents():
        agent_index = 0
        curr_depth += 1
      if curr_depth == self.depth:
        return None, self.evaluationFunction(gameState)
      best_action, best_score = None, None
      if agent_index == 0:
        for action in gameState.getLegalActions(agent_index):
          next_game_state = gameState.generateSuccessor(agent_index, action)
          # print next_game_state
          a_, score_temp = self.minimax(curr_depth, agent_index + 1, next_game_state)
          if best_score is None or score_temp > best_score:
            best_score = score_temp
            best_action = action
      else:
        for action in gameState.getLegalActions(agent_index):
          next_game_state = gameState.generateSuccessor(agent_index, action)
          a_, score_temp = self.minimax(curr_depth, agent_index + 1, next_game_state)
          if best_score is None or score_temp < best_score:
            best_score = score_temp
            best_action = action
      if best_score is None:
        return None, self.evaluationFunction(gameState)
      return best_action, best_score
            

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        inf = float('inf')
        action, score = self.alpha_beta(0, 0, gameState, -inf, inf)
        return action
        util.raiseNotDefined()
    def alpha_beta(self, curr_depth, agent_index, gameState, alpha, beta):
      if agent_index >= gameState.getNumAgents():
        agent_index = 0
        curr_depth += 1
      if curr_depth == self.depth:
        return None, self.evaluationFunction(gameState)
      best_action, best_score = None, None
      if agent_index == 0:
        for action in gameState.getLegalActions(agent_index):
          next_game_state = gameState.generateSuccessor(agent_index, action)
          action_, score_ = self.alpha_beta(curr_depth, agent_index + 1, next_game_state, alpha, beta)
          if best_score is None or score_ > best_score:
            best_action = action
            best_score = score_
          alpha = max(alpha, score_)
          if alpha > beta:
            break
      else:
        for action in gameState.getLegalActions(agent_index):
          next_game_state = gameState.generateSuccessor(agent_index, action)
          action_, score_ = self.alpha_beta(curr_depth, agent_index + 1, next_game_state, alpha, beta)
          if best_score is None or score_ < best_score:
            best_action = action
            best_score = score_
          beta = min(beta, score_)
          if alpha > beta:
            break
      if best_score is None:
        return None, self.evaluationFunction(gameState)
      return best_action, best_score
class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        action, score = self.expectimax(0, 0, gameState)
        return action
    def expectimax(self, curr_depth, agent_index, gameState):
        if agent_index >= gameState.getNumAgents():
          agent_index = 0
          curr_depth += 1
        if curr_depth == self.depth:
          return None, self.evaluationFunction(gameState)
        best_action, best_score = None, None
        if agent_index == 0:
          for action in gameState.getLegalActions(agent_index):
            next_state_game = gameState.generateSuccessor(agent_index, action)
            action_, score_ = self.expectimax(curr_depth, agent_index + 1, next_state_game)
            if best_score is None or best_score < score_:
              best_score = score_
              best_action = action
        else:
          ghost_actions = gameState.getLegalActions(agent_index)
          if len(ghost_actions) > 0:
            p = 1.0/len(ghost_actions)
          for action in ghost_actions:
            next_state_game = gameState.generateSuccessor(agent_index, action)
            action_, score_ = self.expectimax(curr_depth, agent_index + 1, next_state_game)
            if best_score is None:
              best_score = 0.0
            best_score += p*score_
            best_action = action
        if best_score is None:
          return None, self.evaluationFunction(gameState)
        return best_action, best_score

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

