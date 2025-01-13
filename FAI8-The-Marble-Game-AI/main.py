import math
import time

class TreeNode:
  
  def __init__(self, num_marbles, is_AI):
    self.num_marbles = num_marbles
    self.is_AI = is_AI
    self.score = 0
    self.children = []
    self.best_child = None

  def add_child(self, child):
    self.children.append(child)

  def __str__(self): 
    st = "Value: " + str(self.num_marbles) 
    return st

  def set_best_child(self):
    if self.num_marbles == 0 and self.is_AI:
      self.score = 10
      self.best_child = None
      return
    elif self.num_marbles == 0 and not self.is_AI:
      self.score = -10
      self.best_child = None
      return

    for child in self.children:
      child.set_best_child()
    
    best_child = None
    if self.is_AI:
      best_score = math.inf
      for child in self.children:
        if child.score < best_score:
          best_score = child.score
          best_child = child
    else:
      best_score = -math.inf
      for child in self.children:
        if child.score > best_score:
          best_score = child.score
          best_child = child

    self.best_child = best_child
    self.score = best_score

class Tree:

  def __init__(self, rootNode):
    self.root = rootNode
    self.build_tree(root)
    root.set_best_child()

  def build_tree(self, node):
    if node.num_marbles == 0:
      return

    possible_states = []
    for i in range(1, 4):
      potential_state = node.num_marbles - i
      if potential_state >= 0:
        possible_states.append(potential_state)

    child_is_AI = not node.is_AI

    for state in possible_states:
      childNode = TreeNode(state, child_is_AI)
      node.add_child(childNode)
      if (state > 0):
        self.build_tree(childNode)

  def play_game(self):
    curr = self.root
    input("Welcome to the Marble Game! In this game, you have a pile of n marbles and you must take turns with the AI. During your turn, you can choose to pick up 1, 2, or 3 marbles. A player wins if the opponent doesn't have any marbles to pick up. Press Enter to play!")
    print()
    print("Number of Marbles Remaining: " + str(curr.num_marbles))
    print()

    while curr.num_marbles > 0:
      print("It's your turn!")

      while True:
        move = int(input("How many marbles would you like to pick up? "))
        valid_move = False
        for child in curr.children:
          if child.num_marbles == curr.num_marbles - move:
            curr = child
            valid_move = True
            break
        if not valid_move:
          print("The number of marbles you selected is invalid! Try again!")
        else:
          break

      print()
      print("Number of Marbles Remaining: " + str(curr.num_marbles))
      if curr.num_marbles == 0:
        print("Game Over! You have won!")
        break

      print()
      print("It's the AI's turn!")
      time.sleep(1)
      ai_move = curr.num_marbles - curr.best_child.num_marbles
      print("The AI has chosen to remove " + str(ai_move) + " marbles")
      curr = curr.best_child

      print()
      print("Number of Marbles Remaining: " + str(curr.num_marbles))
      print()
      if curr.num_marbles == 0:
        print("Game Over! The AI has won!")
        break

marble_count = 5
root = TreeNode(marble_count, False)
tree = Tree(root)
tree.play_game()