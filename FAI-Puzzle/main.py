# main.py

import queue
import copy

class Node:

  def __init__(self,board):
    self.neighbors = []
    self.board = board

  def __str__(self):
    ret = ''
    for row in self.board:
      for space in row:
        ret += space + ' '
      ret += '\n'
    return ret

  def __lt__(self, other):
    return self.board < other.board
  def __eq__(self, other):
    return self.board == other.board
  def __hash__(self):
    ret = ""
    for row in self.board:
      for value in row:
        if value == " ":
          ret += "0"
        else:
          ret += value
    return int(ret)
  def solved(self):
    if self.__hash__() == 123456780:
      return True
    else:
      return False

  def manhattan_distance(self,x1,y1,x2,y2):
    return (abs(x1-x2) + abs(y1-y2))

  def heuristic(self):

    solution_board = [
      ['1', '2', '3'],
      ['4', '5', '6'],
      ['7', '8', ' '],
    ]

    positions = {}

    for i in range(0,3):
      for j in range(0,3):
        positions[solution_board[i][j]] = (i,j)
    #print(positions)
    #print(positions[self.board[0][2]][0])

    sumofmd = 0
    for i in range(0,3):
      for j in range(0,3):
        sumofmd += self.manhattan_distance(i,j,positions[self.board[i][j]][0], positions[self.board[i][j]][1])
    return sumofmd
  def generate_neighbors(self):
    neighbors = []


    #first, find the coordinates of the empty spot
    # hint: search for it
    coordforspace = (0,0)
    for i in range(0,3):
      for j in range(0,3):
        if self.board[i][j] == " ":
          coordforspace = (i,j)


    #second: add/subtract in all of the possible directions it can go 
    #example, lets say the ' ' is at [0,1] we can do [0+1][1] and [0-1][1] (not possible)
    # we can also do: [0][1+1] and [0][1-1]
    #store possibilities inside of a list
    #next, create a conditional that checks what results are possible 
    #next, create a new board for each new neighbor

    if coordforspace[0] + 1 < 3:
      neighbors_grid = copy.deepcopy(self.board)

      neighbors_grid[coordforspace[0]][coordforspace[1]] = neighbors_grid[coordforspace[0]+1][coordforspace[1]]
      neighbors_grid[coordforspace[0]+1][coordforspace[1]] = " "

      node1 = Node(neighbors_grid)
      #print("down")
      #print(node1)
      neighbors.append(node1)

    if coordforspace[0] - 1 > -1:

      neighbors_grid2 = copy.deepcopy(self.board)

      neighbors_grid2[coordforspace[0]][coordforspace[1]] = neighbors_grid2[coordforspace[0]-1][coordforspace[1]]
      neighbors_grid2[coordforspace[0]-1][coordforspace[1]] = " "

      node2 = Node(neighbors_grid2)
      #print("up")
      #print(node2)
      neighbors.append(node2)

    if coordforspace[1] + 1 < 3:

      neighbors_grid3 = copy.deepcopy(self.board)

      neighbors_grid3[coordforspace[0]][coordforspace[1]] = neighbors_grid3[coordforspace[0]][coordforspace[1]+1]
      neighbors_grid3[coordforspace[0]][coordforspace[1]+1] = " "

      node3 = Node(neighbors_grid3)
      #print("right")
      #print(node3)
      neighbors.append(node3)

    if coordforspace[1] - 1 > -1:

      neighbors_grid4 = copy.deepcopy(self.board)

      neighbors_grid4[coordforspace[0]][coordforspace[1]] = neighbors_grid4[coordforspace[0]][coordforspace[1]-1]
      neighbors_grid4[coordforspace[0]][coordforspace[1]-1] = " "

      node4 = Node(neighbors_grid4)
      #print("left")
      #print(node4)
      neighbors.append(node4)


    self.neighbors = neighbors

class PuzzleGraph:
# A* search
  def __init__(self,node):
    self.start_node = node
  def astarsearch(self):
    visited = set()
    pq = queue.PriorityQueue()
    f = 0 + self.start_node.heuristic()
    pq.put((f,self.start_node,0,[self.start_node]))

    while not pq.empty():
      func,node,level,path = pq.get()

      if node.solved():
        return path


      print(level)
      print(node)


      if node not in visited:
        visited.add(node)


        node.generate_neighbors()

        print("neighbors")

        for neighbor in node.neighbors:
          if neighbor not in visited:
            level += 1
            #cost = level
            f = level + neighbor.heuristic()
            pq.put((f,neighbor,level,path + [neighbor]))

    return "didn't work"
  def bfs(self):
    queue = [(self.start_node,[self.start_node])]
    visited = set()


    while len(queue) != 0:
      n,path = queue.pop(0)
      if n not in visited:
        print(n)
        if n.solved():
          return "solved",path

        visited.add(n)

        n.generate_neighbors()


        for neighbor in n.neighbors:
          queue.append((neighbor,path+[neighbor]))


start_board = [
    ['3', '2', '1'],
    ['4', '8', '6'],
    ['7', ' ', "5"],
  ]  

n = Node(start_board)
n1 = PuzzleGraph(n)

#print(n.__hash__())
#print(n.solved())
n.heuristic()
#print(n.heuristic())
#n.generate_neighbors()
#print(n.neighbors)

#print("Correct A* route")
#route = n1.astarsearch()
#for r in route:
  #print(r)
n1.bfs()    











