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

class MapGraph:

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

  # get smallest number of portals required to get from city start to city end
  def get_min_num_portals(self, start, end):
    # check if nodes exist in graph
    if start.key not in self.graph or end.key not in self.graph:
      print("one or both of your cities don't exist")
      return
    else:
      visited = {start}
      queue = [(start, 0)]
      while (len(queue) != 0):
        queue_val = queue.pop(0)
        node = queue_val[0]
        num_portals = queue_val[1]

        if node == end:
          return num_portals

        for neighbor in node.neighbors:
          if neighbor not in visited:
            visited.add(neighbor)
            queue.append((neighbor, num_portals+1))

# initialize graph
g = MapGraph()

# construct graph
ny = Node("New York")
sf = Node("San Francisco")
dc = Node("Washington D.C")
p = Node("Paris")
t = Node("Tokyo")
l = Node("London")
d = Node("Dubai")

g.add_node(ny)
g.add_node(sf)
g.add_node(dc)
g.add_node(p)
g.add_node(t)
g.add_node(l)
g.add_node(d)

g.add_edge(ny, sf)
g.add_edge(ny, dc)
g.add_edge(sf, dc)
g.add_edge(sf, d)
g.add_edge(sf, t)
g.add_edge(dc, p)
g.add_edge(dc, l)
g.add_edge(p, l)

# calculate travel times
print("San Franciso to Dubai: " + str(g.get_min_num_portals(sf, d))) # returns 1
print("Tokyo to Dubai: " + str(g.get_min_num_portals(t, d))) # returns 2
print("New York to Dubai: " + str(g.get_min_num_portals(ny, d))) # returns 2
print("Tokyo to London: " + str(g.get_min_num_portals(t, l))) # returns 3