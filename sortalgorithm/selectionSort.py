"""Using min()"""

list1 = [56, 3, 2, 78, 6, 0]
for i in range(len(list1)):
    min_val = min(list1[i:])  #it takes a min val for each iteration
    # print(min_val)
    min_index = list1.index(min_val)  # to find index of min val
    # print(min_index)
    list1[i], list1[min_index] = list1[min_index], list1[i]  # swap
print(list1)


"""Max()"""
list1 = [56, 3, 2, 78, 6, 0]
for i in range(len(list1)):
    max_val = max(list1[i:])  #it takes a max val for each iteration
    max_index = list1.index(max_val)  # to find index of max val
    list1[i], list1[max_index] = list1[max_index], list1[i]  # swap
print(list1)

