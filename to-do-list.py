list = []
item = None

while item != "exit":
    item = input("please enter an item to add to the to-do list (say exit to stop): ")
    if item != "exit":
        list.append(item)

print()
print("here's your to-do list:")

for thing in list:
    print(thing)