import gym
import numpy as np

'''
env methods:
reset(self): Reset the environment's state. Returns observation.
step(self, action): Step the environment by one timestep. Returns observation, reward, done, info.
render(self, mode='human'): Render one frame of the environment. The default mode will do something human friendly, such as pop up a window.

'''

# use to find a specific color (yellow/chicken) and to print out the i/j value
# change i,j values to find the area to search. bottom left quadrant is ~approx i=185-210, j=0-80
# (left) chicken lives within j=44-48
def state_find_colors(state):

    # row
    for i in range(0, 210):

        #col
        for j in range(40, 55):

            #YELLOW find
            #if (np.array_equal(state[i][j], np.array([252, 252, 84]))):
            #BLACK exclude
            if (np.array_equal(state[i][j], np.array([0, 0, 0])) == False and\
            #whiteGREY exclude
            np.array_equal(state[i][j], np.array([214, 214, 214])) == False and\
            #lightGREY exclude
            np.array_equal(state[i][j], np.array([170, 170, 170])) == False and\
            #darkGREY exclude
            np.array_equal(state[i][j], np.array([142, 142, 142])) == False and\
            #YELLOW exclude
            np.array_equal(state[i][j], np.array([252, 252, 84])) == False and\
            #PINK exclude               
            np.array_equal(state[i][j], np.array([228, 111, 111])) == False): 
               
                print("color= ", state[i][j], "i= ", i, "j=", j)
 
            #print("state[", i, "]["    , j, "] = ", state[i][j])

    print("========================================")

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

z    # 0 == no operation/no move env.step(0)
    # 1 == up       env.step(1)
    # 2 == down     env.step(2)
    '''

    '''
    # R   G   B
    # 0   0   0   = black
    # 214 214 214 = white grey (dashed lines)
    # 170 170 170 = light grey (bottom/top chicken begin/goal location)
    # 142 142 142 = dark grey (ROAD)
    # 228 111 111 = pink
    # 252 252 84  = yellow (chicken)
    # 142 142 142 = dotted lines
    # Row 195+ = bottom black border

    Activision logo: 196,25-196,43: T and V stripe at top of activision logo
    # 194, 111 - 194,112 right chicken
    # 194 0-7 left border
    # row 187-194, cols 44-49 left chicken
    # road lines at 102 44-47, 104 44-47, cars change direction here
    # left chicken center point: 191, 48
    # road : 184-
    # lane dividers, top to bottom:
    # 39, 55, 71, 87, 102-104 MIDDLE, 119, 135, 151, 167
    '''
