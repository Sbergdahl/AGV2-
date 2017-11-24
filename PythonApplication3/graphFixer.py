import networkx as nx
# takes a directed graph and returns a new graph,
#  that is exanded to indlude a time dimension and "self loops"

# expands the graph in a second dimensions for time, note that the graph is directed so that it is only possible to go forward in time 
def addTimeDimension(graph,nodes,edges,timeSteps):
		addSelfLoops(graph,nodes,edges)
		addTimeNodes(graph,nodes,timeSteps)
		addTimeEdges(graph,edges,timeSteps)
		return graph


# adds self loops to the inputted graph, this is to allow for waiting in a node 
def addSelfLoops(graph,nodes,edges):
	for i in range(0,len(nodes)):
		new_edge=(nodes[i],nodes[i])
		edges.append(new_edge)
	return edges

# adds nodes for next timestep 
def addTimeNodes(graph,nodes,timeSteps):
	timestr='.0'
	for i in range(0,timeSteps):
		for j in range(0,len(nodes)):
			nodes[j]+=timestr
		graph.add_nodes_from(nodes)
	return nodes

# adds edges forward in time. also changes the edges of the graph in order to make it directed forward in time 
def addTimeEdges(graph,edges,timeSteps):
	timestr='.1'
	for i, line in enumerate(edges):

		new_edge= edges[i][1].split('.')
		new_edge= new_edge+timestr
		edges[i]=(edges[i][0]),edges[i][1]=new_edge
	graph.add_edges_from(edges)

	for time in range(0,timeSteps):
		timenr=1*i
		timestr=str(timenr)
		for i, line in enumerate(edges):
			edges[i]=(edges[i][0]+timestr),edges[i][1]+timestr
		graph.add_edges_from(edges)
	return edges

def addTimeSuffixes(graph,nodes,edges):
	graph = addNodeTimeSuffix(nodes,graph)
	graph = addEdgeTimeSuffix(edges,graph)
	return graph

#adds the time suffix to inputed nodes 
def addNodeTimeSuffix(nodes,graph):
	graph.remove_nodes_from(nodes)
	timestr='.0'
	for i in range(0,len(nodes)):
		nodes[i]+=timestr
	graph.add_nodes_from(nodes)
	return graph
#adds the time suffix to inputed edges
def addEdgeTimeSuffix(edges,graph):
	graph.remove_edges_from(edges)
	timestr='.0'
	for i in range(0,len(edges)):
		
		edges[i]=(edges[i][0]+timestr),edges[i][1]+timestr
		
	graph.add_edges_from(edges)
	return graph
	