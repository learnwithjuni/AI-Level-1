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

  # BFS
  def bfs(self, start_node):
    visited = {start_node}
    queue = [start_node]
    while (len(queue) != 0):
      n = queue.pop(0)
      print(n.key + " ", end = "")
      for neighbor in n.neighbors:
        if neighbor not in visited:
          visited.add(neighbor)
          queue.append(neighbor)

# initialize graph
g = Graph()

# construct graph
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")

g.add_node(a)
g.add_node(b)
g.add_node(c)
g.add_node(d)
g.add_node(e)

g.add_edge(a, b)
g.add_edge(a, c)
g.add_edge(b, d)
g.add_edge(b, e)

# run BFS
# expected output: a b c d e
g.bfs(a)
print()