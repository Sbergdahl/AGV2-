import networkx as nx
import matplotlib.pyplot as plt
from helpers import * 
from graphFixer import * 
from graphNetwork import * 

# The code is in file is chaotic since it's mostly been used to 
# fin errors in the helper functions
# note that most ofthe code below is just intended for testing different help functions 

# declare  directed graph

G = nx.DiGraph()
nodes_of_graph = ['1','2','3','4','5','6']
#nodes_of_graph[0].append('.1')
G.add_nodes_from(nodes_of_graph)
edges = [('1','2'),('2','1'),('3','2'),('2','3'),('4','3'),('3','4'),('5','4'),('4','5'),('6','5'),('5','6'),('1','6'),('6','1'),('6','2'),('2','6'),('5','3'),('3','5')]
G.add_edges_from(edges)
G = addTimeSuffixes(G,nodes_of_graph,edges)

print nx.astar_path(G,'1.0','4.0')

#edges = addTimeToEdges(edges)
# how many steps are added in the time dimension? 
time= 10


# for testing with Kollmorgens graph

Gderp = graphNetworkFromFile() # kollmorgens network
GderpNodes=list(Gderp.nodes)   # nodes of kollmorgens network
GderpEdges=list(Gderp.edges)   # edges of kollmorgens network

Gorg = graphNetworkFromFile() # testting for seeing if time can be reduced by using a metric of minimum amout of steps needed

Gderp = addTimeDimension(Gderp,GderpNodes,GderpEdges,100)

resA1 =  throughTimeAndSpace(Gderp,Gorg,10060,58,100)
print resA1
Gderp=reserveAndRemove(Gderp,resA1)


resA2=throughTimeAndSpace(Gderp,Gorg,10093,10055,100)
print resA2
Gderp=reserveAndRemove(Gderp,resA2)

resA3=throughTimeAndSpace(Gderp,Gorg,409,10093,100)
print resA3
Gderp=reserveAndRemove(Gderp,resA3)

#resA3=throughTimeAndSpace(Gderp,Gorg,409,10093,100)
#print resA3
#Gderp=reserveAndRemove(Gderp,resA3)


# add the time 
G=addTimeDimension(G, nodes_of_graph,edges,time)

print G.nodes

# declare start and stop positions for each of the agents 
startA1= 1
stopA1= 5

startA2= 4
stopA2= 6 

startA3= 2
stopA3= 4 

resA1 =  throughTimeAndSpace(G,startA1,stopA1,time)
print "path for A1 is:"
print resA1

#lägg till alla reserverade noder i t+1
resA1=reserveNodes(resA1)
# ta bort de reserverade noderna
Gtmp = removeReserved(G,resA1)

# find the path for A2 with reservations made for A1 
resA2 = throughTimeAndSpace(Gtmp,startA2,stopA2,time)
print "path for A2 is:"
print resA2

resA2 = reserveNodes(resA2)
Gtmp = removeReserved(Gtmp, resA2)

# find path for A3 
resA3 = throughTimeAndSpace(Gtmp,startA3,stopA3,time)
print "path for A3 is:"
print resA3

# ta bort de noder som är reserverade, 
# gör sedan a* med dem borttagna!	



