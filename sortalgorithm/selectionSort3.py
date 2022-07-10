"""method2"""

list1 = [34, 5, 6, 81, 0, 5]
print("unsorted list", list1)
for i in range(len(list1) - 1):  #to ignore the sorted part
    min_val = list1[i]  #first value present is min value
    for j in range(i + 1, len(list1)):  #i+1 to compare min val with d next val
        if list1[j] < min_val: #if true
            min_val = list1[j]  #becomes the new min val

    min_index = list1.index(min_val, i)  #i is the start to resolve duplicate values
    if list1[i] != list1[min_index]:  #don't swap when elements is in correct position
        list1[i], list1[min_index] = list1[min_index], list1[i]

print(list1)


"""Descending order"""
num = int(input("How many numbers do you want to enter: "))
list1 = [int(input("enter number: ")) for x in range(num)]
print("unsorted list", list1)
for i in range(len(list1) - 1):
    max_index = i
    for j in range(i + 1, len(list1)):
        if list1[j] > list1[max_index]:
            max_index = j

    if list1[i] != list1[max_index]:
        list1[i], list1[max_index] = list1[max_index], list1[i]

print(list1)
