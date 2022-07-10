list1 = [10, 15, 4, 23, 0]
print("unsorted list:", list1)
for j in range(len(list1) - 1):  #so its 1 iteration less than the length of list
    for i in range(len(list1) - 1 - j):  # bcus we are comparing 4 times, j to reduce itr in each step
        if list1[i] > list1[i + 1]:  # if true, swap
            list1[i], list1[i + 1] = list1[i + 1], list1[i]
            print(list1)
        else:
            print(list1)
    print()


print("sorted list:", list1)


"""Descending order"""
# list1 = [10, 15, 4, 23, 0]
# print("unsorted list:", list1)
# for j in range(len(list1) - 1):  #so its 1 iteration less than the length of list
#     for i in range(len(list1) - 1):  # bcus we are comparing 4 times
#         if list1[i] < list1[i + 1]:  # if true, swap
#             list1[i], list1[i + 1] = list1[i + 1], list1[i]
#
# print("sorted list:", list1)


"""Method3"""
num = int(input("How many number do you want to enter: "))
list1 = []
print("Enter the values: ")
for k in range(num):
    list1.append(int(input("")))
print("unsorted list:", list1)
for j in range(len(list1) - 1, 0, -1):
    for i in range(j):
        if list1[i] > list1[i + 1]:  # if true, swap
            list1[i], list1[i + 1] = list1[i + 1], list1[i]
            # print(list1)
        # else:
        #     print(list1)
    # print()


print("sorted list:", list1)