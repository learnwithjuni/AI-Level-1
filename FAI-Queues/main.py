# create the queue using a list
queue = []

# enqueue elements to the back of the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# peek at the front element in the queue
print(queue[0])

# dequeue an element off the front of the queue
print(queue.pop(0))

# check if the stack is empty
print(len(queue) == 0)

# iterate through the remainder of the queue and print its elements
while (len(queue) != 0):
  print(queue.pop(0))
