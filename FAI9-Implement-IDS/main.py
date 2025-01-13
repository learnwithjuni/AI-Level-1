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

  # IDS
  def ids(self, start_node, max_depth):
    for i in range(0, max_depth+1):
      self.dls(start_node, i)
      print()

  # DLS
  def dls(self, start_node, depth_limit):
    if depth_limit < 0:
      return

    visited = {start_node}
    stack = [(start_node, 0)] # track depth in stack
    while (len(stack) != 0):
      node, depth = stack.pop()
      print(node.key, end = " ")
      for neighbor in node.neighbors:
        # visit a node's neighbor only if it is below depth limit and has not yet been visited
        if neighbor not in visited and depth + 1 <= depth_limit: 
            visited.add(neighbor)
            stack.append((neighbor, depth+1))


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
g.add_edge(b, e)
g.add_edge(c, d)
g.add_edge(d, e)

# run IDS with max_depth of 4
# expected output:
# a
# a c b
# a c d b e
# a c d e b
# a c d e b
g.ids(a, 4)