class Node:

  # change the node to contain the prompt for the game
  def __init__(self, key, prompt):
    self.key = key
    self.prompt = prompt
    self.neighbors = []

  def add_neighbor(self, node):
    self.neighbors.append(node)
    
  def __str__(self):
    s = "ID: " + self.key + "\nNeighbors: "
    for n in self.neighbors:
      s += n.key + "  "
    return s

class AdventureGraph:

  def __init__(self):
    self.graph = {}

  def add_node(self, node):
    self.graph[node.key] = node

  # modify this method to make directed edges
  def add_edge(self, node1, node2):
    if not node1.key in self.graph:
      print("Node with ID " + node1.key + " is not in the graph")
    elif not node2.key in self.graph:
      print("Node with ID " + node2.key + " is not in the graph")
    else:
      node1.add_neighbor(node2)

  def __str__(self):
    s = ""
    for node in self.graph:
      s += self.graph[node].__str__() + "\n\n"
    return s

  # write this method for the game
  def start_adventure(self, node):
    while len(node.neighbors) != 0:
      ans = input(node.prompt)
      node = self.graph[ans]
    print(self.graph[node.key].prompt)


# build the nodes of your game
start = Node("start", "You find yourself in an abandoned theme park. Do you want to *leave* or *explore*?")
leavePark = Node("leave", "You decided to leave the park and go home.")
explorePark = Node("explore", "You walk around until you hear a scary noise. Do you *run away* or *check it out*?")
runAway = Node("run away", "You got spooked and decided to run away from the noise. The theme park is too scary! You decide you want to go home.")
checkItOut = Node("check it out", "You decide to go see what the noise is. You hear a meow and realize it was just a cat that's exploring the park too")

# build the tree for your game
g = AdventureGraph()
g.add_node(start)
g.add_node(leavePark)
g.add_node(explorePark)
g.add_node(runAway)
g.add_node(checkItOut)

g.add_edge(start, leavePark)
g.add_edge(start, explorePark)
g.add_edge(explorePark, runAway)
g.add_edge(explorePark, checkItOut)

# check that the graph is built correctly
# print(g)

# play the adventure game
g.start_adventure(start)
