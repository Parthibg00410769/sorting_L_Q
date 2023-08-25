list1 = []

q1 = int(input("How many numbers you want to input: "))
print("Enter the values now: ")
for i in range(q1):
    list1.append(int(input()))

for j in range(len(list1)-1):
    for i in range(len(list1)-1):
        if list1[i] > list1[i+1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]

print(list1)
