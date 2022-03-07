import numpy as np

width = 10
height = 10

exits = ( (0,0), (2, 9), (7,9), (9,0) )
city = np.zeros((width, height))
traffic = np.zeros((width, height))
#calculate edge weight based on difference from current pos to next square
#for each block, calculate all the edge weights and pick the shortest path
#Djikstra? complex

for exit in exits:
    city[exit[0]][exit[1]] = -1
print(city)
