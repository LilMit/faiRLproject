import gym
import numpy as np
import random
import features
import helpers
import util

env = gym.make('Freeway-v0')

YELLOW = [252,252,84]
PINK = [228,111,111]
BLACK = [0,0,0]
SIDEWALKGRAY = [170,170,170]
ROADGRAY = [142,142,142]
DARKBLUE = [24,26,167]
UGLYYELLOW = [105,105,15]
WHITELINES = [214,214,214]
GOALROW=0
STARTROW = 191

class QAgent():

    def __init__(self, alpha=1.0, epsilon=0.05, gamma=0.8, numTraining = 10):
        
        self.discount = .3
        self.alpha = float(alpha)
        self.epsilon = float(epsilon)
        self.discount = float(gamma)
        self.numTraining = int(numTraining)
        self.chicken_x = STARTROW
        self.chicken_y = 48
        self.distanceFromGoal = self.chicken_x - GOALROW
        self.feature_weights = {"grey_pixels": .1, "grey_ahead": .5}
        self.actions = [0,1,2]
        self.weights = util.Counter()

    def find_chicken(self,state):
        for i in range(10,194):
            if np.array_equal(state[i][self.chicken_y], np.array(YELLOW)):
                self.chicken_x = i
                return (i)

    def getWeights(self):
        return self.weights     

    def getQValue(self, state, action):

        total = 0.0
        feats = features.getFeatures(state, action)

        if not feats:
            return 0.0

        for key in feats.keys():
            if key in self.weights:
                total += (self.weights[key] * feats[key])
        return total
    
    def computeValueFromQValues(self, state):
        action = self.computeActionFromQValues(state)
        if action == None:
          return 0.0
          
        return self.getQValue(state,action)

    def computeActionFromQValues(self, state):
        maximum = -9999999999

        bestAction = None
        for action in self.actions:
          value = self.getQValue(state,action)
          if value > maximum:
            maximum = value
            bestAction = action
          elif value == maximum:
            bestAction = random.choice([action, bestAction])
          
        return bestAction

    def update(self, state, action, nextState, reward):

        value = self.getQValue(state,action)
        maxNext = self.computeValueFromQValues(nextState)
        difference = (reward + (self.discount*maxNext)-value)
        feats = features.getFeatures(state,action)
        if not feats:
          return

        for feature in feats:
          if feature not in self.weights:
            self.weights[feature] = 0.0
          temp = self.weights[feature] + (self.alpha * difference * feats[feature])
          self.weights[feature] = temp

#         difference = reward + (self.discount * new_q_value) - old_q_value
        
#         for feature, value in new_features_value.items():

# ##            print("feature", feature)
# ##            print("self.alpha", self.alpha)
# ##            print("difference", difference)
# ##            print("old_features_dict[feature]", old_features_dict[feature])

#             self.feature_weights[feature] += self.alpha * difference * new_features_value[feature]

    def artificial_reward(old_row, new_row):
        return
         
def main():

    q_agent = QAgent()
    env.reset()
    
    # 0/stay in place action to calculate initial Q value
    state, reward, done, _ = env.step(0)

    for i in range(1000):
        
        action = random.choice([0,1,2])
        obs = env.render()        

        # calculate old/initial feature values and q value
        old_features_values = features.calc_feature_values(state, q_agent.chicken_x, q_agent.chicken_y)
        old_q_value = q_agent.getQValue(state, action, old_features_values)

        # take action
        state, reward, done, _ = env.step(action)

        # calculate new/current feature values and q value
        new_features_values = features.calc_feature_values(state, q_agent.chicken_x, q_agent.chicken_y)
        new_q_value = q_agent.getQValue(state, action, new_features_values)
        
        # update weights of features based on the the difference of q value
        q_agent.update(old_q_value, new_q_value, new_features_values, reward)
     
    env.close()

main()


