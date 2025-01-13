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

  # iterative DFS
  def dfs_iterative(self, start_node):
    # check if nodes exist in graph
    visited = {start_node}
    stack = [start_node]
    while (len(stack) != 0):
      n = stack.pop()
      print(n.key + " ", end = "")
      for neighbor in n.neighbors:
        if neighbor not in visited:
          visited.add(neighbor)
          stack.append(neighbor)

  # recursive DFS
  def dfs_recursive(self, visited, node):
    visited.add(node)
    print(node.key + " ", end = "")
    for neighbor in node.neighbors:
      if neighbor not in visited:
        self.dfs_recursive(visited, neighbor)

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

# run DFS iteratively
# expected output: a c b e d
g.dfs_iterative(a)
print()

# run DFS recursively
# expected output: a b d e c
g.dfs_recursive(set(), a)