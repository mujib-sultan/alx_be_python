num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation1 = input("choose the operation (+ , - , * , /)")
match operation1:
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
        result = num1/num2
        if num2 != 0 :
            print(f"The result is {result}") 
        else :
            print("cannot divide by zero ") 
    case _:
        print("Invalid operation. Please choose from +, -, *, /.")        
             
         







