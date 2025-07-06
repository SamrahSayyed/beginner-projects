def add(number1, number2):
  return (number1 + number2)
  
def subtract(number1, number2):
  return number1 - number2
  
def divide(number1, number2):
  return number1 / number2
  
def multiply(number1, number2):
  return number1 * number2
  
while  True:
  

    print("1.Add\n2.Subtract\n3.Divide\n4.Multiply")
    option = input("Enter any option between 1 and 4: ")

    number1 = float(input("Enter your first number: "))
    number2 = float(input("Enter your second number: "))

    if (option == '1'):
        print(number1, "+", number2, "=", add(number1, number2))

    elif (option == '2'):
        print(number1, "-", number2, "=", subtract(number1, number2))

    elif (option == '3'):
        print(number1, "/", number2, "=", divide(number1, number2))

    elif (option == '4'):
        print(number1, "*", number2, "=", multiply(number1, number2))

    else:
      print("Enter a valid number between 1 and 4.")