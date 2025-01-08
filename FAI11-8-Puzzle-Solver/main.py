import time
from queue import PriorityQueue

# Node stores state of the game (board)
class Node:

  def __init__(self, board):
    self.board = board
    self.neighbors = []

  def __eq__(self, other):
    return self.__class__ == other.__class__ and self.board == other.board

  def __lt__(self, other):
    return self.board < other.board

  def __str__(self):
    ret = ''
    for row in self.board:
      for space in row:
        ret += space + ' '
      ret += '\n'
    return ret

  # board's hash code is it's sequence of values from
  # top left to bottom right as an int (empty space is 0)
  def __hash__(self):
    total = ''
    for row in self.board:
      for space in row:
        if space != ' ':
          total += space
        else:
          total += '0'
    return int(total)

  # returns True if board is solved, False otherwise
  def is_solved(self):
    correct = [
      ['1', '2', '3'],
      ['4', '5', '6'],
      ['7', '8', ' '],
    ]
    return self.board == correct

  # calculate the heuristic for the A* search
  # heuristic is the sum of the manhattan distances of each tile from its correct positions
  def get_heuristic(self):
    total = 0
    correct = [
      ['1', '2', '3'],
      ['4', '5', '6'],
      ['7', '8', ' '],
    ]

    # maps each value in correct to its coordinate
    correct_coords = {}
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        correct_coords[correct[i][j]] = (i,j)

    # calculate distance of each tile from the 
    # correct position and add it to total
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        num = self.board[i][j]
        x_dist = abs(i - correct_coords[num][0])
        y_dist = abs(j - correct_coords[num][1])
        total += x_dist + y_dist

    return total
  
  # generates all neighbors of a node by expanding it
  def generate_neighbors(self):
    neighbors = []

    # find and store coordinates of empty space in the board
    row = -1
    col = -1
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        if self.board[i][j] == ' ':
          row = i
          col = j
          break

    # list of possible directions space can move
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    # loop through each possible movement
    for r,c in dirs:
      new_row = row+r
      new_col = col+c

      # if move is valid (new row and column are within bounds of the board), create and add child node to children
      if 0 <= new_row <= 2 and 0 <= new_col <= 2:

        # make copy of board
        new_board = []
        for line in self.board:
          board_row = []
          for space in line:
            board_row.append(space)
          new_board.append(board_row)

        # switch space to new location and switch number to space's old location
        new_board[new_row][new_col] = ' '
        new_board[row][col] = self.board[new_row][new_col]

        # create and add child to neighbors
        node = Node(new_board)
        neighbors.append(node)

    self.neighbors = neighbors

# stores the start node of the puzzle and methods to solve it
class PuzzleGraph:

  def __init__(self, start_node):
    self.start_node = start_node

  # solve puzzle with BFS
  def bfs_solve(self):
    visited = {self.start_node}
    # stores tuples containing (node, path)
    queue = [(self.start_node, [self.start_node])]
    count = 0 # stores number of nodes visited

    while (len(queue) != 0):
      n, path = queue.pop(0)
      count += 1

      # if board is solved, return
      if n.is_solved():
        return path, count

      # if board not solved, generate children and continue searching
      n.generate_neighbors()
      for neighbor in n.neighbors:
        if neighbor not in visited:
          visited.add(neighbor)
          queue.append((neighbor, path+[neighbor]))
 
  # solve puzzle with A* Search
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


start_board = [
  ['8', '6', '5'],
  ['1', '4', '2'],
  ['7', ' ', '3'],
]

startNode = Node(start_board)
g = PuzzleGraph(startNode)

# run bfs to solve 8 puzzle
print('Running BFS...')
bfs_start = time.time()
bfs_path, bfs_count = g.bfs_solve()
bfs_end = time.time()
print('Time: ' + str(bfs_end - bfs_start))
print('Number of States Searched: ' + str(bfs_count))
print('Solution Length: ' + str(len(bfs_path)))
print('Solution: ')
for node in bfs_path:
  print(node)
print()

# run a* search to solve 8 puzzle
print('Running A* Search...')
a_start = time.time()
a_path, a_count = g.a_star_solve()
a_end = time.time()
print('Time: ' + str(a_end - a_start))
print('Number of States Searched: ' + str(a_count))
print('Solution Length: ' + str(len(a_path)))
print('Solution: ')
for node in a_path:
  print(node)
