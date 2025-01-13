class Stack:

  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def peek(self):
    return self.stack[len(self.stack) - 1]

  def pop(self):
    return self.stack.pop()

  def isEmpty(self):
    return len(self.stack) == 0

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

class Graph:

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

  # iterative dfs using stack class
  def dfs_with_stack_class(self, start_node):
    # check if nodes exist in graph
    if len(self.graph) == 0:
      return
    else:
      visited = {start_node}
      stack = Stack()
      stack.push(start_node)
      while (not stack.isEmpty()):
        n = stack.pop()
        print(n.key + " ", end = "")
        for neighbor in n.neighbors:
          if neighbor not in visited:
            visited.add(neighbor)
            stack.push(neighbor)

# test the Stack class
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.isEmpty())
print()

# construct graph
g = Graph()

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")

g.add_node(a)
g.add_node(b)
g.add_node(c)
g.add_node(d)
g.add_node(e)

g.add_edge(a, b)
g.add_edge(a, c)
g.add_edge(b, d)
g.add_edge(b, e)

# run DFS with stack class
# expected output: a c b e d
g.dfs_with_stack_class(a)
print()