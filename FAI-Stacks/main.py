# create the stack using a list
stack = []

# push elements onto the top of the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# peek at the top element of the stack
print(stack[len(stack) - 1])

# pop an element off the top of the stack
print(stack.pop())

# check if the stack is empty
print(len(stack) == 0)

# iterate through remainder of stack and print the elements
while (len(stack) != 0):
  print(stack.pop())