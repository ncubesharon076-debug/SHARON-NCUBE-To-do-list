task = ["Study", "go to school", "come back home"]

print("1. add task")
print("2. confirm task")


task = input("select: ")
if task=="1":
    task=input("enter your task:")
    task.append(task)

elif task=="2":
    print("task:")
    for task in tasks:
        print("-", task)

    

else:
    print("invalid selection")

