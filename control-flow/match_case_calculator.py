num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("choose the operation (+ , - , * , /)")
match operation:
    case "+":
        result = num1 + num2 
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2 
        print(f"The result is {result}.")
    case "*" :
        result = num1 * num2 
        print(f"The result is {result}.")
    case "/":
        if num2 != 0 :
         print(f"The result is {result}") 
         result = num1/num2
        else :
         print("cannot divide by zero ") 
    case _:
        print("Invalid operation. Please choose from +, -, *, /.")        
             
         







