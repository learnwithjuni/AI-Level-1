class TreeNode:

  def __init__(self, board, player):
    self.board = board
    self.player = player
    self.children = []

  def add_child(self, child):
    self.children.append(child)

  def print_board(self):
    print("  ", end = "")
    for i in range(len(self.board)):
      print(str(i) + " ", end = "")
    print()
    for i in range(len(self.board)):
      print(str(i) + " ", end = "")
      for j in range(len(self.board[i])):
        print(self.board[i][j] + " ", end = "")
      print()

  def check_win(self):
    # check each row for a winner
    if self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] != '-':
      return self.board[0][0], True
    elif self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] != '-' :
      return self.board[1][0], True
    elif self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] != '-':
      return self.board[2][0], True

    # check each column for a winner
    if self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] != '-':
      return self.board[0][0], True
    elif self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != '-':
      return self.board[0][1], True
    elif self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] != '-':
      return self.board[0][2], True

    # check each diagonal for a winner
    if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '-':
      return self.board[0][0], True
    elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '-':
      return self.board[0][2], True

    # check for a draw (no winners and board is full)
    for row in self.board:
      for space in row:
        if space == "-":
          return None, False
    
    # game is a draw
    return "draw", True

start_board = [
  ['-', '-', '-'],
  ['-', '-', '-'],
  ['-', '-', '-']
]

child_board = [
  ['-', '-', '-'],
  ['-', 'X', '-'],
  ['-', '-', '-']
]

win_board = [
  ['X', '-', 'O'],
  ['-', 'X', '-'],
  ['O', '-', 'X']
]

# create TreeNodes
root = TreeNode(start_board, "X")
child = TreeNode(child_board, "O")
win = TreeNode(win_board, "O")

# add children
root.add_child(child)

# print board
root.print_board()
print()
child.print_board()
print()

# print instance attributes
print(root.children)
print(root.player)
print(child.player)
print(root.board)
print()

# check_win()
print(root.check_win())
print(child.check_win())
print(win.check_win())