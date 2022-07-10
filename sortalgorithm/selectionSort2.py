"""For duplicate values"""

# list1 = [56, 0, 2, 2, 6, 0]
# print("unsorted list", list1)
# for i in range(len(list1)):
#     min_val = min(list1[i:])
#     min_index = list1.index(min_val, i)  #i is the start to resolve duplicate values
#     list1[i], list1[min_index] = list1[min_index], list1[i]
#     print(list1)  #to print values of all iteration
#
# print(list1)


"""Modified"""

list1 = [34, 5, 6, 81, 0, 5]
print("unsorted list", list1)
for i in range(len(list1) - 1):  #to ignore the sorted part
    min_val = min(list1[i:])
    min_index = list1.index(min_val, i)  #i is the start to resolve duplicate values
    if list1[i] != list1[min_index]:  #don't swap when elements is in correct position
        list1[i], list1[min_index] = list1[min_index], list1[i]
    print(list1)  #to print values of all iteration

# print(list1)
