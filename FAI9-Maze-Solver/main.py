import maze as mz
import queue

# construct maze
# X is goal (located at (2, 0))
# O is the player (we'll start at (0, 0))
# * are cells with quicksand (higher cost to travel from this cell to another)
maze = ""
maze += "+---+---+---+\n"  
maze += "|           |\n" # row0
maze += "+   +---+   +\n"
maze += "|     * |   |\n" # row1
maze += "+---+   +   +\n"
maze += "| X         |\n" # row2
maze += "+---+---+---+\n"
      # col0 col1 col2

# row has 14 characters (including new line) so maze width is 14
maze = mz.Maze(maze, 14)

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

  def __str__(self):
    s = ""
    for node in self.graph:
      s += self.graph[node].__str__() + "\n\n"
    return s

  def get_path_cost(self, path):
    cost = 0
    for i in range(len(path)-1):
      cost += self.graph[path[i]].neighbors[path[i+1]]
    print("Path Cost: " + str(cost))

  def get_dfs_path(self, start_node, end_node):
    print("DFS Traversal: ")
    visited = {start_node}
    stack = [(start_node, [start_node.key])]
    while (len(stack) != 0):
      n,path = stack.pop()

      print(n.key)
      if n == end_node:
        print()
        return path

      for neighbor_key in n.neighbors:
        neighbor = self.graph[neighbor_key]
        if neighbor not in visited:
          visited.add(neighbor)
          stack.append((neighbor, path+[neighbor.key]))

  def get_bfs_path(self, start_node, end_node):
    print("BFS Traversal: ")
    visited = {start_node}
    queue = [(start_node, [start_node.key])]
    while (len(queue) != 0):
      n,path = queue.pop(0)
      print(n.key)
      if n == end_node:
        print()
        return path

      for neighbor_key in n.neighbors:
        neighbor = self.graph[neighbor_key]
        if neighbor not in visited:
          visited.add(neighbor)
          queue.append((neighbor, path+[neighbor.key]))

  def get_ids_path(self, start_node, end_node, max_depth):
    print("IDS Traversal: ")
    for i in range(0, max_depth+1):
      path = self.get_dls_path(start_node, end_node, i)
      if path != None:
        return path

  def get_dls_path(self, start_node, end_node, depth_limit):
    print("\nDLS Traversal with Depth of " + str(depth_limit)+ ": ")
    if depth_limit < 0:
      return []
    visited = {start_node}
    stack = [(start_node, 0, [start_node.key])] # track depth in stack
    while (len(stack) != 0):
      node, depth, path = stack.pop()
      print(node.key)
      if node == end_node:
        return path
      for neighbor_key in node.neighbors:
        neighbor = self.graph[neighbor_key]
        if neighbor not in visited and depth + 1 <= depth_limit: 
            visited.add(neighbor)
            stack.append((neighbor, depth+1, path+[neighbor.key]))

  def get_ucs_path(self, start_node, end_node):
    print("UCS Traversal: ")
    visited = set()
    q = queue.PriorityQueue()
    q.put((0,start_node, [start_node.key]))

    while not q.empty():
      cost, n, path = q.get()

      if n not in visited:
        visited.add(n)
        print(n.key)

        if (n == end_node):
          return path

        for neighbor_key in n.neighbors:
          neighbor = self.graph[neighbor_key]
          if neighbor not in visited:
            q.put((n.neighbors[neighbor.key]+cost, neighbor, path + [neighbor.key]))     
    
# construct graph of the maze
# names are "nodexy" where x is the row of the cell, y is the column of the cell
node00 = Node("(0,0)")
node01 = Node("(0,1)")
node02 = Node("(0,2)")
node10 = Node("(1,0)")
node11 = Node("(1,1)")
node12 = Node("(1,2)")
node20 = Node("(2,0)")
node21 = Node("(2,1)")
node22 = Node("(2,2)")

g = Graph()
g.add_node(node00)
g.add_node(node01)
g.add_node(node02)
g.add_node(node10)
g.add_node(node11)
g.add_node(node12)
g.add_node(node20)
g.add_node(node21)
g.add_node(node22)

g.add_edge(node00, node10, 1)
g.add_edge(node00, node01, 1)

g.add_edge(node01, node00, 1)
g.add_edge(node01, node02, 1)

g.add_edge(node02, node01, 1)
g.add_edge(node02, node12, 1)

g.add_edge(node10, node00, 1)
g.add_edge(node10, node11, 1)

g.add_edge(node11, node21, 10)
g.add_edge(node11, node10, 10)

g.add_edge(node12, node02, 1)
g.add_edge(node12, node22, 1)

g.add_edge(node20, node21, 1)

g.add_edge(node21, node20, 1)
g.add_edge(node21, node11, 1)
g.add_edge(node21, node22, 1)

g.add_edge(node22, node21, 1)
g.add_edge(node22, node12, 1)

# different types of traversals to find path to goal
dfs = g.get_dfs_path(node00, node20)
print(dfs)
maze.print_path(dfs)
g.get_path_cost(dfs)
print()

bfs = g.get_bfs_path(node00, node20)
print(bfs)
maze.print_path(bfs)
g.get_path_cost(bfs)
print()

ids = g.get_ids_path(node00, node20, 6)
print(ids)
maze.print_path(ids)
g.get_path_cost(ids)
print()

ucs = g.get_ucs_path(node00, node20)
print(ucs)
maze.print_path(ucs)
g.get_path_cost(ucs)
print()
