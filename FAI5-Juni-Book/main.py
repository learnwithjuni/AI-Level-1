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

class FriendGraph:

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

  # counts the number of distinct friend groups in the graph
  def count_groups(self):

    num_groups = 0
    visited = set()
    for node in self.graph.values():
      if node not in visited:
        num_groups += 1
        visited.add(node)
      stack = [node]
      while (len(stack) != 0):
        n = stack.pop()
        for neighbor in n.neighbors:
          if neighbor not in visited:
            visited.add(neighbor)
            stack.append(neighbor)

    return num_groups


# construct graph where everyone is in one group
g1 = FriendGraph()
a1 = Node("a")
b1 = Node("b")
c1 = Node("c")
d1 = Node("d")
e1 = Node("e")

g1.add_node(a1)
g1.add_node(b1)
g1.add_node(c1)
g1.add_node(d1)
g1.add_node(e1)

g1.add_edge(a1, b1)
g1.add_edge(a1, c1)
g1.add_edge(b1, d1)
g1.add_edge(b1, c1)
g1.add_edge(d1, e1)

# construct graph with three groups of friends
g2 = FriendGraph()
a2 = Node("a")
b2 = Node("b")
c2 = Node("c")
d2 = Node("d")
e2 = Node("e")

g2.add_node(a2)
g2.add_node(b2)
g2.add_node(c2)
g2.add_node(d2)
g2.add_node(e2)

g2.add_edge(a2, b2)
g2.add_edge(a2, c2)

# test the count_groups() method
print(g1.count_groups()) # return 1
print(g2.count_groups()) # retuns 3