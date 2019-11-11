import gym
import numpy as np
#env = gym.make('Freeway-ram-v0')
env = gym.make('Freeway-v0')
'''
env methods:
reset(self): Reset the environment's state. Returns observation.
step(self, action): Step the environment by one timestep. Returns observation, reward, done, info.
render(self, mode='human'): Render one frame of the environment. The default mode will do something human friendly, such as pop up a window.

'''

def my_prints():

    #print(env.get_keys_to_action())
    #print("action space = ", env.action_space)
    #print(env.get_action_meanings())


    # 210 rows
    #print("rows = ", len(state))
    # 160 cols
    #print("cols (pixels/row) = ", len(state[0]))
    # each [row][col] has a list of 3 elements [r, g, b]
    #print("[row][col] len =", len(state[0][0]))
    
    '''
                                 0      1       2
    # get_action_meanings() = ['NOOP', 'UP', 'DOWN']

    # 0 == no operation/no move env.step(0)
    # 1 == up       env.step(1)
    # 2 == down     env.step(2)
    '''

def main():

    env.reset()
    #print("lives = ", env.ale.lives())
    #print("screen dimensions = ", env.ale.getScreenDims())
    
 

    for i in range(1000):
        obs = env.render()
        state, reward, done, _ = env.step(1)
        print(reward)

 
    # row
    for i in range(185, 210):

        #col
        for j in range(0, 80):

            if (np.array_equal(state[i][j], np.array([241, 252, 135]))):
                print(state[i][j])

            #print("state[", i, "][", j, "] = ", state[i][j])
        
    
    #env.frameskip = 1

    #for i in range(1000):
        
        #env.render()
        #state, reward, done, _ = env.step(1)

        #print(state)


    #print("env.ale = ", env.ale)
    #print("difficulties = ", env.ale.getAvailableDifficulties())
        

    #print("state = ", state)
    #for i in state:
        #print("i = ", i)

    #print("reward= ", reward)
    #print("done = ", done)
    #print("_ = ", _)

    #for _ in range(100):
        
        #print("begin loop")

        #env.render(mode='human')
        #print(env.step(1))
        
    #my_prints()
    env.close()

main()


