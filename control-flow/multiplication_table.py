number = int(input("Enter a number to see its multiplication table:"))
i=1
for i in range(1,11):
    
    result = i*number

    print (f"{number} x {i} = {result}")
