task = input("Enter your task :")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
match priority :
    case "high":
        if time_bound == "yes":
            print(f"Reminder : {task}is a high priority task that requires immediate attention today!")
        else :
            print(f"Reminder : {task} is a high priority task that requires delegation ")  
    case "medium " : 
        if time_bound == "yes":
           print(f"Reminder : {task} is a medium priority task which may need schedule ")
        else :
            print (f"Note : {task} is a medium prioriy task which may need your free time to accomplish it ")
    case "low":
        if time_bound == "yes":
            print(f"Note : {task} is a low priority task you can do it after your main project")
        else :
            print(f"Note : {task}  is a  priority task. Consider completing it when you have free time.")    
            


