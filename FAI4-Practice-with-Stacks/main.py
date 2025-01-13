# exercise 1: place 1-10 in stack then pop out each element and print it out
# expected output: 10 9 8 7 6 5 4 3 2 1
stack = []
for i in range(1,11):
  stack.append(i)
while (len(stack) != 0):
  print(stack.pop()) 
print()

# exercise 2: isPalindrome()
# takes in a string and returns whether or not the string is a palindrome
def isPalindrome(word):
  # create stack
  stack = []

  # add each letter to stack
  for letter in word:
    stack.append(letter)

  # check if each letter popped from stack equals
  # letter in the word (stack reverses the word)
  for letter in word:
    if letter != stack.pop():
      return False
  return True

# test isPalindrome()
print(isPalindrome("racecar"))
print(isPalindrome("mom"))
print(isPalindrome("hello world"))
print()

# exercise 3: evaluateExpression()
# take in an expression in Reverse Polish Notation and return its evaluation
def evaluateExpression(expr):
  # initialize stack and possible operators
  stack = []
  operators = {'+', '-', '/', '*'}
  # split expression into tokens (numbers and operators)
  tokens = expr.split()
  for i in range(len(tokens)):
    token = tokens[i]
    # if token is a operator, pop top two elements off the stack and perform the given operation
    if token in operators:
      num1 = stack.pop()
      num2 = stack.pop()
      if token == '+':
        stack.append(num1+num2)
      elif token == '-':
        # put num2 first to preserve order of subtraction
        stack.append(num2 - num1) 
      elif token == '*':
        stack.append(num1*num2)
      else:
        # put num2 first to preserve order of division
        stack.append(num2/num1)
    else:
      # put it on the stack if it is a number
      stack.append(int(token))
  
  # return answer
  return stack.pop()

# test evaluateExpression()
print(evaluateExpression("2 3 +")) # == 5
print(evaluateExpression("1 3 -")) # == -2
print(evaluateExpression("3 5 + 4 *")) # == 32
print(evaluateExpression("6 2 / 3 + 4 *")) # == 24.0
print()