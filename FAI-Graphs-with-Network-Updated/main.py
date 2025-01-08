import networkx as nx
import matplotlib.pyplot as plt

# undirected, unweighted, cyclic graph
G1=nx.Graph()
nodes = ["a", "b", "c", "d"]
edges = [("a", "b"), ("a", "c"), ("c", "d"), ("d", "a")]
G1.add_nodes_from(nodes)
G1.add_edges_from(edges)
nx.draw(G1, with_labels = True)
plt.savefig("basic_graph.png")
plt.clf()

# acyclic graph
G2=nx.Graph()
nodes = ["a", "b", "c", "d"]
edges = [("a", "b"), ("a", "c"), ("d", "a")]
G2.add_nodes_from(nodes)
G2.add_edges_from(edges)
nx.draw(G2, with_labels = True)
plt.savefig("acyclic_graph.png")
plt.clf()