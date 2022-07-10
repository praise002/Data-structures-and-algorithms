"""Using median element as pivot"""
import statistics

#find correct position of pivot element


def pivot_place(list1, first, last):
    low = list1[first]  #value present in 1st index
    high = list1[last]  #last
    mid = (first + last) // 2  #index position of the mid
    pivot_val = statistics.median([low, list1[mid], high])
    if pivot_val == low:
        p_index = first
    elif pivot_val == high:
        p_index = last
    else:
        p_index = mid

    list1[last], list1[p_index] = list1[p_index], list1[last]
    pivot = list1[last]
    left = first
    right = last - 1
    while True:
        while left <= right and list1[left] >= pivot:  # if true we increment d value by 1
            left = left + 1
        while left <= right and list1[right] <= pivot:  # when it becomes false
            right = right - 1
        if right < left:
            break
        else:
            list1[left], list1[right] = list1[right], list1[left]

    list1[last], list1[left] = list1[left], list1[last]  # list1[first] is pivot
    return left

#to divide the list for recursive call


def quicksort(list1, first, last):
    if first < last:  #stopping condition
        p = pivot_place(list1, first, last)
        quicksort(list1, first, p - 1)  #left sublist
        quicksort(list1, p + 1, last)  #right sublist


#main
list1 = [56, 26, 93, 17, 31, 44]
n = len(list1)
quicksort(list1, 0, n - 1)
print(list1)