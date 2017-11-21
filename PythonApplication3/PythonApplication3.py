import networkx as nx
import matplotlib.pyplot as plt
from helpers import * 
from graphFixer import * 


G = nx.Graph()
nodes_of_graph = [1,2,3,4,5,6]
G.add_nodes_from(nodes_of_graph)
edges = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,1),(2,6),(3,5)]
G.add_edges_from(edges)




# function for adding timesteps automatically


addSelfLoops(G,nodes_of_graph,edges)
addTimeEdges(edges,10)



#plt.plot() # Create a plot
#nx.draw(G, with_labels=True, font_weight='bold',node_size=10)
#nx.draw(G)  # Draws all nodes at correct position
#plt.show() # Need this to see a plot


edges_in_g2= [(1, 11),(1,12),(1,16),(2,11),(2,12),(2,13),(2,16),(3,12),(3,13),(3,14),(3,15),(4,13),(4,14),(4,15),(5,13),(5,14),(5,15),(5,16),(6,11),(6,12),(6,15),(6,16)]
G2 = nx.DiGraph()
G2.add_nodes_from(nodes_of_graph)
G2.add_edges_from(edges_in_g2)
for nodes, line in enumerate(nodes_of_graph):
   nodes_of_graph[nodes]=nodes_of_graph[nodes]+10


time=10
# lägger till tidsdimensionen i grafen
G2= addTimeDimension(G2,nodes_of_graph,edges_in_g2,time)

# plotta den två djupa G2
#plotGraph(G2)


# funkar loopar igenom G2 och hittar en väg genom tid och rum för båda agenterna
#for i in range(0,4):
#	try:
#		resA1 =  nx.astar_path(G2,1,5+10*i)
#		print nx.astar_path(G2,1,5+10*i)
#		break
#	   
#	except: 
#		pass
resA1 =  throughTimeAndSpace(G2,1,5,time)
print "path for A1 is:"
print resA1

resA2 = throughTimeAndSpace(G2,4,6,time)
print "path for A2 is:"
print resA2



#lägg till alla reserverade noder i t+1
stop = len(resA1)
for i in range(0,stop-1):
	resA1.append(resA1[i]+10)
# samma för A2
stop = len(resA2)
for i in range(0,stop-1):
	resA2.append(resA2[i]+10)

print "resA1:"
print resA1
print "resA2:"
print resA2
# ta bort de noder som finns i resA2 och resA1

G2tmp= G2.copy(as_view=False)

#ta bort de noder som finns i A1 
for i in range(0,len(resA1)):
	G2tmp.remove_node(resA1[i])



# find the path for A2 with reservations made for A1 
resA2 = throughTimeAndSpace(G2tmp,4,6,10)
print "path for A2 is:"
print resA2


stop = len(resA2)
for i in range(0,stop-1):
	resA2.append(resA2[i]+10)

for i in range(0,len(resA2)):
	G2tmp.remove_node(resA2[i])

for i in range(0,10):
	try:
		resA3 =  nx.astar_path(G2tmp,2,4+10*i)
		print nx.astar_path(G2tmp,2,4+10*i)
		break
	except: 
		pass

# ta bort de noder som är reserverade, 
# gör sedan a* med dem borttagna!	



