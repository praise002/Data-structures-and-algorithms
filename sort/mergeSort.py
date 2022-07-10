"""
Used by the python langauage
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(a, b, arr):
    # sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:  #we want to stop at end of list
        if a[i] <= b[j]:  #compare d 2 elements
            arr[k] = a[i]
            i = i + 1  #increment i
        else:  #if b is lesser
            arr[k] = b[j]
            j = j + 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == "__main__":
    # a = [5, 8, 12, 56]
    # b = [7, 9, 45, 51]

    arr = [10, 3, 15, 7, 8, 23, 98, 29]

    # print(merge_two_sorted_lists(a, b))
    print(merge_sort(arr))
