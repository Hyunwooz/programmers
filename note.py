commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
array = [1, 5, 2, 6, 3, 7, 4]	
for command in commands:
    x,y,z = command
    new_array = array[x-1:y]
    new_array.sort()
    print(new_array)
    print(new_array[z-1])