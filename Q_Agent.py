import gym
import numpy as np
import random
import features
import helpers
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

    def find_chicken(self,state):
        for i in range(self.x-2, self.x+2):
            if np.array_equal(state[i][self.y], np.array(YELLOW)):
                self.x = i
                return

    def getQValue(self, state, action, feature_values):

        q_value = 0

        for feature, value in feature_values.items():
            q_value += value * self.feature_weights[feature]
        return q_value

    def update(self, old_q_value, new_q_value, new_features_value, reward):

        difference = reward + (self.discount * new_q_value) - old_q_value
        
        for feature, value in new_features_value.items():

##            print("feature", feature)
##            print("self.alpha", self.alpha)
##            print("difference", difference)
##            print("old_features_dict[feature]", old_features_dict[feature])

            self.feature_weights[feature] += self.alpha * difference * new_features_value[feature]

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


