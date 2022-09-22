myList = [85, 24, 63, 45, 18, 31, 96, 50]
key = 17
location = None
for index in range(len(myList)):
    if myList[index] == key:
        location = index
if location == None:
    print("Key not found")
else:
    print("Key found at: ", location)