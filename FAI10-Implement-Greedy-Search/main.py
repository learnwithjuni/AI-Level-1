import queue

class Node:

  # modified to store Node state and dictionary of neighbors mapping neighbor node's keys to the weight from the current node to that neighbor
  def __init__(self, key):
    self.key = key
    self.neighbors = {}

  # modified to take in edge weight and update neighbors dictionary
  def add_neighbor(self, node, weight):
    self.neighbors[node.key] = weight
    
  # modified to print state and key value pairs in neighbors
  def __str__(self):
    s = "ID: " + self.key + "\nNeighbors: "
    for n in self.neighbors:
      s += n + ":" + str(self.neighbors[n]) + "  "
    return s

  # a less than comparison method to compare an instance of Node with another instance of Node
  def __lt__(self, other):
    return self.key < other.key

class Graph:

  def __init__(self):
    self.graph = {}

  def add_node(self, node):
    self.graph[node.key] = node

  # modified to create directed edges and take in a weight for the edge
  def add_edge(self, node1, node2, weight):
    if not node1.key in self.graph:
      print("Node with ID " + node1.key + " is not in the graph")
    elif not node2.key in self.graph:
      print("Node with ID " + node2.key + " is not in the graph")
    else:
      node1.add_neighbor(node2, weight)
      node2.add_neighbor(node1, weight)

  def __str__(self):
    s = ""
    for node in self.graph:
      s += self.graph[node].__str__() + "\n\n"
    return s

  # Greedy Search
  def greedy_search(self, start_node):
    visited = set()
    q = queue.PriorityQueue()
    q.put((0,start_node))

    while not q.empty():
      cost, n = q.get()

      if n not in visited:
        visited.add(n)
        print(n.key, end = " ")

        for neighbor_key in n.neighbors:
          neighbor = self.graph[neighbor_key]
          if neighbor not in visited:
            # heuristic is cost to get to neighboring node
            q.put((n.neighbors[neighbor.key], neighbor))

# construct Graph
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")

g = Graph()
g.add_node(a)
g.add_node(b)
g.add_node(c)
g.add_node(d)
g.add_node(e)

g.add_edge(a, b, 3)
g.add_edge(a, c, 5)
g.add_edge(a, e, 15)
g.add_edge(b, d, 2)
g.add_edge(b, e, 6)

# run greedy search
# expected output: a b d c e
g.greedy_search(a)
