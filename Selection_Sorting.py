#finding the minimum value

list1 = [55,6,2,88,54,43,21,12,62,1,77,52,80,99,90,12,20,0]

for i in range(len(list1)):
    min_val = min(list1[i:])
    min_index = list1.index(min_val)

    temp = list1[i]
    list1[i] = list1[min_index]
    list1[min_index] = temp

#print(list1)


#Finding the maximum value
for i in range(len(list1)):
    max_val = max(list1[i:])
    max_index = list1.index(max_val)

    temp = list1[i]
    list1[i] = list1[max_index]
    list1[max_index] = temp
print(list1)