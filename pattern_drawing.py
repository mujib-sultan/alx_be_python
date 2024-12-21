
rows = 1
pattern = int(input("Enter the size of the pattern:"))

while rows < pattern+1:
    for i in range(pattern):
        print("*", end="")
        
    print()
    rows+=1    