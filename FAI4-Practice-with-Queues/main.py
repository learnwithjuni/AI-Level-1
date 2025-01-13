# exercise 1: place 1-10 in stack then dequeue each element and print it out
# expected output: 1 2 3 4 5 6 7 8 9 10
stack = []
for i in range(1,11):
  stack.append(i)
while (len(stack) != 0):
  print(stack.pop(0)) 
print()

# exercise 2: buildQueueString()
# takes in a QueueString and uses a queue to build and return a regular string from the QueueString
def buildQueueString(queueStr):
  # initialize a queue and resulting string
  queue = []
  buildStr = ""

  # loop through each letter and perform the right operation for
  # each letter to build new string
  for letter in queueStr:
    if letter == '*':
      buildStr += queue.pop(0)
    else:
      queue.append(letter)

  return buildStr

# test buildQueueString
print(buildQueueString("H*ELL**O**")) # == "HELLO"
print(buildQueueString("Q*UE*UES** A**R*E CO***O**L***")) # == "QUEUES ARE COOL"
print(buildQueueString("JU**NI *L**E**ARN*I**N*G**")) # == "JUNI LEARNING"
print()

# exercise 3: getEvens()
# returns a queue of all the even numbers in a inputted queue in the same order
def getEvens(oldQueue):
  # initialize queue
  newQueue = []
  
  # loop through inputted queue and add all even numbers to new queue
  while (len(oldQueue) != 0):
    num = oldQueue.pop(0)
    if num % 2 == 0:
      newQueue.append(num)

  return newQueue

# test getEvens()
print(getEvens([1, 2, 6, 5, 4, 6])) # == [2, 6, 4, 6]
  