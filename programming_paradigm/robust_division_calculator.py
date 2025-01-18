def safe_divide( numerator, denominator):
      
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        
        result = numerator/denominator
        print(f"The reult of the division is {result} ")
    except ZeroDivisionError:
        print("Error: cannot divide by zero!")
    except ValueError:
        print("please enter numbers only")

   


    

   
    
            
                 
              
   