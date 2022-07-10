"""Ascending order"""


# def shell_sort(a_list):
#     #find d gap
#     gap = len(a_list) // 2
#     while gap > 0:   #only sort when greater than 0
#         for index in range(gap, len(a_list)):   #gap is pos & also 4
#             current_element = a_list[index]  #index will start from gap
#             pos = index  #it is called position, in ex its pos 4
#             while pos >= gap and current_element < a_list[pos - gap]:  #4-4=0
#                 a_list[pos] = a_list[pos - gap]
#                 pos = pos - gap
#
#             a_list[pos] = current_element  #when it breaks out of d loop
#
#         gap = gap // 2   #after one pass reduce d gap
#
#
# num = int(input("List length: "))
# list1 = [int(input()) for i in range(num)]
# shell_sort(list1)
# print("Sorted list:", list1)


"""descending order"""


def shell_sort(a_list):
    #find d gap
    gap = len(a_list) // 2
    while gap > 0:   #only sort when greater than 0
        for index in range(gap, len(a_list)):   #gap is pos & also 4
            current_element = a_list[index]  #index will start from gap
            pos = index  #it is called position, in ex its pos 4
            while pos >= gap and current_element > a_list[pos - gap]:  #4-4=0
                a_list[pos] = a_list[pos - gap]
                pos = pos - gap

            a_list[pos] = current_element  #when it breaks out of d loop

        gap = gap // 2   #after one pass reduce d gap


num = int(input("List length: "))
list1 = [int(input()) for i in range(num)]
shell_sort(list1)
print("Sorted list:", list1)
