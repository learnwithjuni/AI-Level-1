class Node:

  # modified to store Node state and dictionary of neighbors mapping neighbor node's keys to the weight from the current node to that neighbor
  def __init__(self, key, state):
    self.key = key
    self.state = state
    self.neighbors = {}

  # modified to take in edge weight and update neighborst dictionary
  def add_neighbor(self, node, weight):
    self.neighbors[node.key] = weight
    
  # modified to print state and key value pairs in neighbors
  def __str__(self):
    s = "ID: " + self.key + "\nState: " + self.state + "\nNeighbors: "
    for n in self.neighbors:
      s += n + ":" + str(self.neighbors[n]) + "  "
    return s

class StateSpaceGraph:

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

  def __str__(self):
    s = ""
    for node in self.graph:
      s += self.graph[node].__str__() + "\n\n"
    return s

  def manual_search(self, start, end):
    n = start
    time = 0
    while (n != end):
      print("You are in " + n.state + ". Here are the available flights and their travel times: ")
      for key in n.neighbors:
        print("City: " + self.graph[key].state + " | Time: " + str(n.neighbors[key]) + " | Key: " +  key)
      location = ""
      while location not in self.graph:
        print()
        location = input("Type in the key of the place you would like to go: ")
      time += n.neighbors[location]
      n = self.graph[location]
      print()
    print()
    print("You made it to " + n.state + "! It took you " + str(time) + " hours.")


# construct graph
g = StateSpaceGraph()

ny = Node("ny", "New York")
sf = Node("sf", "San Francisco")
dc = Node("dc", "Washington D.C.")
s = Node("s", "Seattle")
la = Node("la", "Los Angeles")
b = Node("b", "Boston")

g.add_node(ny)
g.add_node(sf)
g.add_node(dc)
g.add_node(s)
g.add_node(la)
g.add_node(b)

g.add_edge(b, dc, 2)
g.add_edge(b, ny, 1)
g.add_edge(ny, sf, 6)
g.add_edge(dc, s, 7)
g.add_edge(s, sf, 3)
g.add_edge(sf, la, 1)

# search the graph for a path from Boston to Los Angeles
g.manual_search(b, la)


