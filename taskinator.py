tasks = [] 

quitt = 0 

  

print("Welcome to Taskinator") 

print("") 

print("⊂(◉‿◉)つ") 

print("") 

print("1. Add new task") 

print("") 

print("2. View your tasks") 

print("") 

print("Enter command(1 or 2):") 

print("") 

menu = input("Enter:") 

if menu == "1" : 

    while quitt < 1: 

        print("") 

        new_task = input("Enter task name:") 

        tasks.append(new_task) 

        if new_task == "0": 
            menu = input("Enter:")
            break 
            

if menu == "2" : 

    for x in tasks: 

        print("") 

        print(x) 

        with open(r'\\tasks.txt', 'w') as f: 

           for x in tasks: 

                f.write("%s\n" % "**********************************Task*****************************************") 

                f.write("%s\n" % x) 

                 
