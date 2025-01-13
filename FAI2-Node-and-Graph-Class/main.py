class Node:

  def __init__(self, key):
    self.key = key
    self.neighbors = []

  def add_neighbor(self, node):
    self.neighbors.append(node)
    
  def __str__(self):
    s = "ID: " + self.key + "\nNeighbors: "
    for n in self.neighbors:
      s += n.key + "  "
    return s

class Graph:

  def __init__(self):
    self.graph = {}

  def add_node(self, node):
    self.graph[node.key] = node

  def add_edge(self, node1, node2):
    if not node1.key in self.graph:
      print("Node with ID " + node1.key + " is not in the graph")
    elif not node2.key in self.graph:
      print("Node with ID " + node2.key + " is not in the graph")
    else:
      node1.add_neighbor(node2)
      node2.add_neighbor(node1)

  def __str__(self):
    s = ""
    for node in self.graph:
      s += self.graph[node].__str__() + "\n\n"
    return s

# initialize graph
g = Graph()

# create nodes for the graph
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

# add nodes to the graph
g.add_node(a)
g.add_node(b)
g.add_node(c)
g.add_node(d)

# add edges to the graph
g.add_edge(a, b)
g.add_edge(a, c)
g.add_edge(a, d)
g.add_edge(b, c)

# print entire graph
print("Print graph: ")
print(g)
    