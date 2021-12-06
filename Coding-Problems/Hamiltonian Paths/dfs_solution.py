# Represent a random graph with n vertices of at least degree one (n is at least 100). 
# This graph might be undirected or directed. It could have cycles or no cycles. 
# Randomly select two vertices (x,y) from the graph, and find all of the possible hamiltonian paths in the graph.

import networkx as nx
import random
import matplotlib.pyplot as plt
from collections import defaultdict



#Helper Function
#Returns Random Boolean Value
def randBool():
	bool_val = False
	val = random.randint(0,1)
	if val == 1:
		bool_val = True
	return bool_val


#return random graph of 'N' vertices with degree 1
def generateRandomGraph(N):
	return nx.gnp_random_graph(random.randint(N, N+10), 1, seed=None, directed=False)


#Recursive Depth-First Search to find all hamiltonian paths from a given point:'vertex_point' in a graph G:'graph_g'
def dfs_hamiltonian_paths(graph_g, vertex_point, visited={}, path=[]):
	#Check vertex_point has edges 
	if ( (nx.all_neighbors(graph_g, vertex_point)) is None):
		print("No adjacent vertices found. No possible hamiltonian paths from vertex point ", vertex_point)
		return None
	else:
		#Check if path visited contains all nodes
		if len(path) == len(nx.nodes(graph_g)):
			print ("{} is a hamiltonian path ".format(path))
			return  
		for node in nx.all_neighbors(graph_g, vertex_point):
				if visited[node] == False:
					visited[node] = True
					path.append(node)
					potential_node_path = dfs_hamiltonian_paths(graph_g, node, visited, path)
					visited[node] = False
					path.pop()


#returns none. Checks and prints all possible hamiltonian paths in a random graph G
def find_all_hamiltonian_paths(graph_g, vertex_point):
	#Check graph contains nodes
	if(graph_g):
		#error handle potential stackoverflow
		if len(nx.nodes(graph_g))<=990:
			visited = defaultdict(int) #creates a dictionary defaulted to 0 since python returns True for 0==False
			visited[vertex_point] = True
			path = [vertex_point] 		#store all nodes visited
			dfs_hamiltonian_paths(graph_g, vertex_point, visited, path)
			return None
		else:
			print("graph is too large. Function call will exceed maximum recursion depth")
			return None
	else:
		print("Emtpy graph or none found")
		return None


def main():
	#Construct random graph with n vertices of at least degree one (n is at least 100).
	G = generateRandomGraph(100) 

	#Randomly select two vertices (x, y)
	x = random.randint(0, len(nx.nodes(G))-1)
	y = nx.nodes(G)[random.randint(0, len(nx.nodes(G)))]

	#find all hamiltonian paths for x, y
	find_all_hamiltonian_paths(G, x)
	find_all_hamiltonian_paths(G, y)

	#draw and plot graph
	nx.draw(G)
	plt.show()






if __name__ == '__main__':
	main()