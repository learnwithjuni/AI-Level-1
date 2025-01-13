import networkx as nx
import matplotlib.pyplot as plt

# weighted graph
G4=nx.Graph()
nodes = ["a", "b", "c", "d"]
edges = [("a", "b"),("a", "c"), ("c", "d"), ("d", "a")]
G4.add_nodes_from(nodes)
for i in range(len(edges)):
  G4.add_edge(edges[i][0],edges[i][1],weight = i)
pos=nx.spring_layout(G4)
nx.draw(G4,pos, with_labels = True)
labels = nx.get_edge_attributes(G4,'weight')
nx.draw_networkx_edge_labels(G4,pos,edge_labels=labels)
plt.savefig("weighted_graph.png")
plt.clf()

# directed graph
G5=nx.DiGraph()
nodes = ["a", "b", "c", "d"]
edges = [("a", "b"),("a", "c"), ("c", "d"), ("d", "a")]
G5.add_nodes_from(nodes)
G5.add_edges_from(edges)
pos=nx.spring_layout(G5)
nx.draw(G5,pos, with_labels = True)
labels = nx.get_edge_attributes(G5,'weight')
nx.draw_networkx_edge_labels(G5,pos,edge_labels=labels)
plt.savefig("directed_graph.png")
plt.clf()

# tree
# G5=nx.DiGraph()
# nodes = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# edges = [("a", "b"),("a", "c"), ("a", "d"), ("b", "e"),("b", "f"), ("c", "g"), ("c", "h"),("d", "i"), ("d", "j")]
# G5.add_nodes_from(nodes)
# G5.add_edges_from(edges)
# pos=nx.spring_layout(G5)
# nx.draw(G5,pos, with_labels = True)
# labels = nx.get_edge_attributes(G5,'weight')
# nx.draw_networkx_edge_labels(G5,pos,edge_labels=labels)
# plt.savefig("tree.png")
# plt.clf()