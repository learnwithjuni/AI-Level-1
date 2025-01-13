class TreeNode:
  
  def __init__(self, num_marbles):
    self.num_marbles = num_marbles
    self.children = []

  def add_child(self, child):
    self.children.append(child)

  def __str__(self):
    st = "Value: " + str(self.num_marbles) 
    return st


class Tree:

  def __init__(self, rootNode):
    self.root = rootNode
    self.build_tree(root)

  def build_tree(self, node):
    if node.num_marbles == 0:
      return

    possible_states = []
    for i in range(1, 4):
      potential_state = node.num_marbles - i
      if potential_state >= 0:
        possible_states.append(potential_state)

    for state in possible_states:
      childNode = TreeNode(state)
      node.add_child(childNode)
      if (state > 0):
        self.build_tree(childNode)

  def play_game(self):
    curr = self.root
    input("Welcome to the Marble Game! In this game, you have a pile of n marbles and two players must take turns picking up marbles. During your turn, you can choose to pick up 1, 2, or 3 marbles. A player wins if the opponent doesn't have any marbles to pick up. Press Enter to play!")
    print()
    print("Number of Marbles Remaining: " + str(curr.num_marbles))
    print()

    while curr.num_marbles > 0:
      print("It's Player 1's turn!")

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
        print("Game Over! Player 1 has won!")
        break

      print()
      print("It's the Player 2's turn!")
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
        print("Game Over! Player 2 has won!")
        break

marble_count = 5
root = TreeNode(marble_count)
tree = Tree(root)
tree.play_game()