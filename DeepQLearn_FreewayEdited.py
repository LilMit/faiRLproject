import gym
import numpy as np
import random
#env = gym.make('Freeway-ram-v0')
env = gym.make('Freeway-v0')
'''
env methods:
reset(self): Reset the environment's state. Returns observation.
step(self, action): Step the environment by one timestep. Returns observation, reward, done, info.
render(self, mode='human'): Render one frame of the environment. The default mode will do something human friendly, such as pop up a window.

'''

def my_prints():
    '''
    # 210 rows
    #print("rows = ", len(state))
    # 160 cols
    #print("cols (pixels/row) = ", len(state[0]))
    # each [row][col] has a list of 3 elements [r, g, b]
    #print("[row][col] len =", len(state[0][0]))
    '''
    
    '''
                                 0      1       2
    # get_action_meanings() = ['NOOP', 'UP', 'DOWN']

    # 0 == no operation/no move env.step(0)
    # 1 == up       env.step(1)
    # 2 == down     env.step(2)
    '''

    '''
    # R   G   B
    # 0   0   0   = black
    # 170 170 170 = grey
    # 228 111 111 = pink
    # 252 252 84  = yellow
    '''

def state_find_colors(state):

    # row
    for i in range(185, 210):

        #col
        for j in range(0, 80):

            #if (np.array_equal(state[i][j], np.array([241, 252, 135]))):
            if (np.array_equal(state[i][j], np.array([0, 0, 0])) == False and\
            np.array_equal(state[i][j], np.array([170, 170, 170])) == False and\
            np.array_equal(state[i][j], np.array([228, 111, 111])) == False):
               
                print(state[i][j])

            #print("state[", i, "][", j, "] = ", state[i][j])

class QAgent():

    def __init__(self, alpha=1.0, epsilon=0.05, gamma=0.8, numTraining = 10):

        self.feature_weights = {"grey_pixels": 1.0}
        
        self.discount = .3
        self.alpha = float(alpha)
        self.epsilon = float(epsilon)
        self.discount = float(gamma)
        self.numTraining = int(numTraining)
    
    # sums grey tiles only on the left half of map
    def sum_grey(self, state):

        sum = 0

        for i in range(185, 210):
            for j in range(0, 80):
                if np.array_equal(state[i][j], np.array([170, 170, 170])):
                    sum += 1

        return sum

    def getFeatures(self, state, action):

        #if action is stay still = return -1

        feature_dict = {}
        feature_dict["grey_pixels"] = self.sum_grey(state)
        
        return feature_dict

    def getQValue(self, state, action):

        q_value = 0

        #dictionary
        features_dict = self.getFeatures(state, action)

        for feature in features_dict:

            q_value += features_dict[feature] * self.feature_weights[feature]

        return q_value

    def update(self, old_q_value, old_features_dict, new_q_value, reward):

        difference = reward + (self.discount * new_q_value) - old_q_value
        
        for feature in old_features_dict:

            print("feature", feature)
            print("self.alpha", self.alpha)
            print("difference", difference)
            print("old_features_dict[feature]", old_features_dict[feature])

            self.feature_weights[feature] += self.alpha * difference * old_features_dict[feature]
    
def main():

    q_agent = QAgent()
    
    env.reset()

    action = 0
    state, reward, done, _ = env.step(action)
    print(q_agent.getQValue(state, action))
    print(q_agent.feature_weights)
    print("====")

    for i in range(1000):
        action = random.choice([0,1,2])
        obs = env.render()
        
        old_q_value = q_agent.getQValue(state, action)
        old_features_dict = q_agent.getFeatures(state, action)
        
        state, reward, done, _ = env.step(action)
        print("action=", action, "reward=", reward)
        
        new_q_value = q_agent.getQValue(state, action)

        
        q_agent.update(old_q_value, old_features_dict, new_q_value, reward)

        
    print(q_agent.feature_weights)
    print(q_agent.getQValue(state, action))
    

    env.close()

main()


