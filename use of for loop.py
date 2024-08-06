


j = 5

for i in range(j):
    for j in range(i+1):
        print("* ", end="")
    print( )


j = 5

for i in range(j):
    for j in range(i+1):
        print(j+1, end=" ")
    print()    


list = [84, 51, 67, 41, 35]
min, max = list[0], list[0]

for i in range(1, len(list)):
	if list[i] < min:
		min = list[i]
		
	if list[i] > max:
		max = list[i]
		
print( min)
print(max)
