import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

width = 10
height = 10
exits = ( (0,0), (2, 9), (7,9), (9,0) )
city = np.zeros((width, height))
traffic = np.zeros((width, height))
#calculate edge weight based on difference from current pos to next square
#for each block, calculate all the edge weights and pick the shortest path
#Djikstra? complex
#each road is a queue
#network of queues of people waiting to get on and off

#At simulation start, each queue is empty and begins filling based on each person's decisions
#Some people will be greedy and pick each least congested path
#Some people will take the path that the city has suggested
#When do people start evacuating? Does everyone leave at the exact same moment?
#If the queue reaches a certain size, does the speed of throughput decrease?

g = nx.complete_graph(100, nx.DiGraph())
pos = nx.spring_layout(g, seed=7)

nx.draw_networkx_nodes(g, pos, node_size=100)
nx.draw_networkx_edges(g, pos, edgelist=g.edges(), width=4)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
#for (x,y) in exits:
#    city[x][y] = -1
#print(city)
