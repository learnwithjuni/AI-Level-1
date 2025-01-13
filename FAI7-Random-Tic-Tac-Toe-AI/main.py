import time
import random

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

class Tree:

  def __init__(self, rootNode):
    self.root = rootNode
    self.build_tree(self.root)

  def copy_board(self, board):
    new_board = []
    for i in range(len(board)):
      row = []
      for j in range(len(board[i])):
        row.append(board[i][j])
      new_board.append(row)
    return new_board

  def build_tree(self, node):
    if node.check_win()[1] == True:
      return

    child_player = ""
    if node.player == "X":
      child_player = "O"
    else:
      child_player = "X"

    for i in range(len(node.board)):
      for j in range(len(node.board[i])):
        if node.board[i][j] == '-':
          copy = self.copy_board(node.board)
          copy[i][j] = node.player
          child = TreeNode(copy, child_player)
          node.add_child(child)

    for child in node.children:
      self.build_tree(child)

  def play_game(self):
    input("Welcome to the Tic Tac Toe AI Game, where you can play Tic Tac Toe against a random AI. You will be player 'X' and the computer with be player 'O'. Press Enter to start")
    curr = self.root
    print()
    curr.print_board()

    while True:
      print()
      print("It is now your turn.")

      while True:
        row = int(input("Which row would you like to place your X? "))
        col = int(input("Which column would you like to place your X? "))
        if row < 0 or row > 2 or col < 0 or col > 2 or curr.board[row][col] != '-':
          print("Your row and column values are invalid. Please enter them again.")
        else:
          break
      
      for child in curr.children:
        if child.board[row][col] == curr.player:
          curr = child
          break

      print()
      curr.print_board()
      winner, gameover = curr.check_win()
      if gameover:
        break

      print()
      print("Now it's the AI's turn!")
      time.sleep(1)
      while True:
        row = random.randint(0,2)
        col = random.randint(0,2)
        if curr.board[row][col] == '-':
          break
      
      for child in curr.children:
        if child.board[row][col] == curr.player:
          curr = child
          break

      print()
      curr.print_board()
      winner, gameover = curr.check_win()
      if gameover:
        break

    print()
    if winner == "draw":
      print("Game Over! It was a draw!")
    elif winner == "X":
      print("Game over! You won!")
    else:
      print("Game over! The AI has won!")

start_board = [
  ['-', '-', '-'],
  ['-', '-', '-'],
  ['-', '-', '-']
]
root = TreeNode(start_board, "X")
tree = Tree(root)
tree.play_game()
