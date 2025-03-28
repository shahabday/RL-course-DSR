# Here you create an env and let an agent interact with it. You can measure how
# successful is the random agent, i.e. how much reward it accumulates.

# 0 - Create an env
import gymnasium as gym
import random
env = gym.make("CartPole-v1", render_mode="rgb_array")

# 1 - Reset the env.

# 2 - Let a random agent interact with the env.
#
random.seed(42)

for episode in range (1000):
  env.reset()
  total_reward = 0
  for actions in range(1000):

    action = random.choice([0,1])
    observation, reward, terminated, truncated,  info = env.step(action)
    total_reward += reward
    if terminated:
        #print(f'episode : {episode} reward : {reward} done : {done} info : {info}')
        print(f'episod : {episode}')
        print(f' total reward {total_reward}')
        print(f'total actions {actions}')
        break


# 2.1. Choose a random action (with in the action space of the env.)
# 2.2. and pass it to the environment
# 2.3. How much reward did you get for that action? Keep the score!

# 2.4. Repeat the 2.{1,2,3} until the end of the episode

# 2.5. How much total reward you got? What does it mean to have large/small reward?

# 3. Repeat the whole section 2. Do you get the same total reward?