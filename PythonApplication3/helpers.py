import networkx as nx
import matplotlib.pyplot as plt

def plotGraph(graph):
	plt.plot() # Create a plot
	nx.draw(graph, with_labels=True, font_weight='bold',node_size=10)
	#nx.draw(G)  # Draws all nodes at correct position
	plt.show() # Need this to see a plot
	return

def addTimeDimension(graph,nodesInGraph,edgesInGraph,timesteps):
	for time in range(0,timesteps):	
	   for nodes, line in enumerate(nodesInGraph):
	      nodesInGraph[nodes]=nodesInGraph[nodes]+10
	   graph.add_nodes_from(nodesInGraph)

	   for edges, line in enumerate(edgesInGraph):
	      edgesInGraph[edges]=(edgesInGraph[edges][0]+10),edgesInGraph[edges][1]+10
	   graph.add_edges_from(edgesInGraph)
	return graph

def throughTimeAndSpace(graph,start,end,timesteps):
	for i in range(0,timesteps):
		try: 
			resA1 =  nx.astar_path(graph,start,end+10*i)
			break 
	   	except: 
			pass
	return resA1



