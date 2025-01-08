from queue import PriorityQueue

class Node:

  def __init__(self, jug3L, jug5L,):
    self.state = (jug3L, jug5L)
    self.neighbors = []

  def __eq__(self, other):
    return self.__class__ == other.__class__ and self.state == other.state

  def __lt__(self, other):
    return self.state < other.state

  # change string of both jug values to an int
  def __hash__(self): 
    return int(str(self.state[0])+str(self.state[1]))

  def __str__(self):
    return '3 Liter Jug: ' + str(self.state[0]) + ' | 5 Liter Jug: ' + str(self.state[1])

  # puzzle is solved if 5L Jug has 4L of water
  def is_solved(self):
    return self.state[1] == 4

  def get_heuristic(self):
    # if board is solved board, don't need to keep going
    # so we return the lowest possible heuristic value
    if self.is_solved():
      return 0
    
    # get the difference between the 4 (the amount we want) and the total number of liters of water in the the two jugs
    diff = abs(4 - (self.state[0] + self.state[1]))

    # if diff is 0, you are 1 move away from winning so return 1. Otherwise return the difference (assume that closer to value we want is closer to correct state)
    if diff == 0:
      return 1
    else:
      return diff

  # generate all possible neighbors of current node
  def generate_neighbors(self):
    neighbors = []

    # 6 possible actions from each Node
    # pour from 3L to 5L
    if self.state[0] + self.state[1] <= 5:
      neighbors.append(Node(0, self.state[0] + self.state[1]))
    else:
      neighbors.append(Node(self.state[0] - (5 - self.state[1]), 5))

    # pour from 5L to 3L
    if self.state[0] + self.state[1] <= 3:
      neighbors.append(Node(self.state[0] + self.state[1], 0))
    else:
      neighbors.append(Node(3, self.state[1] - (3 - self.state[0])))

    # fill up 5L
    neighbors.append(Node(self.state[0], 5))

    # fill up 3L
    neighbors.append(Node(3, self.state[1]))

    # empty 5L
    neighbors.append(Node(self.state[0], 0))

    # empty 3L
    neighbors.append(Node(0, self.state[1]))

    self.neighbors = neighbors

class Graph:

  def __init__(self,start_node):
    self.start_node = start_node

  # solve the riddle using greedy search
  def greedy_solve(self):
    visited = set()
    q = PriorityQueue()
    count = 0 # stores number of nodes visited

    # calculate h for the start node
    h = self.start_node.get_heuristic()
    # queue takes a tuple: (h, node, path so far)
    q.put((h, self.start_node, [self.start_node]))

    while not q.empty():
      h, n, path = q.get()

      # only search node if it hasn't been visited
      if n not in visited:
        count += 1
        visited.add(n)

        # if board is solved, return
        if n.is_solved():
          return path, count

        # if board not solved, generate neighbors and keep searching
        n.generate_neighbors()
        for neighbor in n.neighbors:
          if neighbor not in visited:
            h = neighbor.get_heuristic()
            q.put((h, neighbor, path + [neighbor])) 

  # solve the riddle using A* search
  def a_star_solve(self):
    visited = set()
    q = PriorityQueue()
    count = 0 # stores number of nodes visited

    # calculate h and g for the root
    h = self.start_node.get_heuristic()
    g = 0  
    f = g + h
    # queue takes a tuple: (f, depth, node, path so far)
    q.put((f,g,self.start_node, [self.start_node]))

    while not q.empty():
      f, depth, n, path = q.get()

      # only search node if it hasn't been visited
      if n not in visited:
        count += 1
        visited.add(n)

        # if board is solved, return
        if n.is_solved():
          return path, count

        # if board not solved, generate neighbors and keep searching
        n.generate_neighbors()
        for neighbor in n.neighbors:
          if neighbor not in visited:
            h = neighbor.get_heuristic()
            g = depth+1
            f = g+h
            q.put((f, g, neighbor, path + [neighbor])) 

start = Node(0,0)
g = Graph(start)

print('Running Greedy Search...')
path, num_states = g.greedy_solve()
print('Number of States Searched: ' + str(num_states))
print('Solution: ')
for node in path:
  print(node)
print()

print('Running A* Search...')
path, num_states = g.a_star_solve()
print('Number of States Searched: ' + str(num_states))
print('Solution: ')
for node in path:
  print(node)
