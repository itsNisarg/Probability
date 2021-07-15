
# importing required packages

from matplotlib import colors
import numpy as np
import random as rand
from matplotlib import pyplot as plt

# initializing the required variables

switch = 0                      # counter for switching strategy
stay = 0                        # counter for staying strategy
doors = [1,2,3]                 # the three doors behind one of which is your Mercedes Benz
player = 0                      # variable storing the player's choice of door
player_after_switch = 0         # variable storing the player's choice after switching
monty = 0                       # Monty knows where the car is !

# The Game Begins

num = int(input(" Enter the number of times to run the simulation : "))
switch_arr = np.zeros((num+1,), dtype=float)         # array to store resultant data points
stay_arr = np.zeros((num+1,), dtype=float)           # array to store resultant data points
x_axis = np.zeros((num+1,), dtype=int)             # array to create the x-axis

for i in range(1,num+1):

    rand.seed()                         # seeding the random number generator

    monty = rand.choice(doors)          # Monty comes to know the door
    player = rand.choice(doors)         # player chooses a door
    door_dummy = doors[:]
    door_dummy.remove(player)           # a dummy list to keep track of player's choice
    x_axis[i] = i

    if(player == monty):                                                # case where player selects the right door
        stay += 1                                                       # if player stays he wins
        door_dummy.remove(rand.choice(door_dummy))                      # Monty gets two doors to open
        player_after_switch = door_dummy[0]                             # door which player switches to
    else:
        door_dummy.remove(list(set(door_dummy)-set([monty]))[0])        # case where player selects the wrong door
        player_after_switch = door_dummy[0]                             # door which player can switch to

    if(player_after_switch == monty):                                   # if player wins after switching
        switch += 1

    stay_arr[i] = stay/i                    # noting the probabilities so far
    switch_arr[i] = switch/i
    
one_third = np.array([1/3]*(i+1))                       # a numpy array to draw the one-third line
two_third = np.array([2/3]*(i+1))                       # a numpy array to draw the two-thirds line

font1={"family":"serif","color":"navy","size":16}       # font family for the labels
font2={"fontweight":"bold"}

# plotting the graph

plt.title("Monty Hall Problem Simulation",fontdict=font1)
plt.xlabel("NUMBER OF TRIALS",fontdict=font2)
plt.ylabel("PROBABILITY",fontdict=font2)

plt.plot(x_axis, two_third, color='g', label="2/3 Line")
plt.plot(x_axis,switch_arr, color='g',label="Switching Strategy")

plt.plot(x_axis, one_third, color='r', label="1/3 Line")
plt.plot(x_axis,stay_arr, color='r', label="Staying Strategy")

plt.legend()
plt.show()
