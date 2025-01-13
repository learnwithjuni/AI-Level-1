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

# run DLS with limit of 0
# expected output: a
g.dls(a, 0)
print()

# run DLS with limit of 1
# expected output: a c b
g.dls(a, 1)
print()

# run DLS with limit of 2
# expected output: a c d b e
g.dls(a, 2)
print()

# run DLS with limit of 3 
# all DLS with depth_limit >= 3 with result in the same traversal
# expected output: a c d e b
g.dls(a, 3,)
print()

# run DLS with limit of 4
# expected output: a c d e b
g.dls(a, 4)
print()