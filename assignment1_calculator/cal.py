#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
def add(a,b):
  return a+b

def substraction(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide(a,b):
  if b == 0:
    print("float division by zero")
    return
  return a/b

def power(a,b):
  return a**b

def remainder(a,b):
  if b==0:
    print("float division by zero")
    return
  return a%b


#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
def select_op(choice):
  if choice == '#':
    return -1
  elif choice == '$':
     return 0
  elif choice in ('+','-','*','/','^','%'):
    while True:
      num1 = input("Enter first number: ")
      print(num1)
      if num1.endswith('$'):
        return 0
      elif num1 == '#':
        return -1
      else:
        try:
          num1 = float(num1)
          break
        except ValueError:
          print("Invalid input")
          continue

    while True:
      num2 = input("Enter second number: ")
      print(num2)
      if num2.endswith('$'):
        return 0
      elif num2 == '#':
        return -1
      else:
        try:
          num2 = float(num2)
          break
        except ValueError:
          print("Invalid input")
          continue
  
    result = 0
    if choice == '+':
      result = add(num1,num2)
    elif choice == '-':
      result = substraction(num1,num2)
    elif choice == '*':
      result = multiply(num1,num2)
    elif choice == '/':
      result = divide(num1,num2)
    elif choice == '^':
      result = power(num1,num2)
    elif choice == '%':
      result = remainder(num1,num2)

    print(f"{num1} {choice} {num2} = {result}")   

  else:
    print("Unrecognized operation")  
    return       



#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()