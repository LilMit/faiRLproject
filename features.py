import gym
import numpy as np

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

def sum_grey(state):

    sum_grey = 0

    for i in range(0, 210):
        for j in range(44, 50):
            if np.array_equal(state[i][j], np.array([142, 142, 142])):
                sum_grey += 1

    return sum_grey

def grey_ahead(state, chicken_x, chicken_y):
    
    return np.array_equal(state[chicken_x + 3][chicken_y], np.array(ROADGRAY))

def getLives(self,env):
    
    return env.ale.lives() 

def getFeatures(self,state,action,env):
    features = util.Counter()
    lives = self.getLives(env)
    env.step(action)


'''
Calculates the value for all features
Input: state
Returns: a dictionary of {feature1: value1, feature2: value2, featureN, valueN}
'''
def calc_feature_values(state, chicken_x, chicken_y):

    # manually add features and call the method to get its value below:
    return {"grey_pixels": sum_grey(state), "grey_ahead": grey_ahead(state, chicken_x, chicken_y)}
    
