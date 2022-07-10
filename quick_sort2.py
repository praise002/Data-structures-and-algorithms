def pivot_place(arr, first, last):  #first&last will tell d length of list, ar index
    pivot = arr[last]  #last index is pivot
    left = first
    right = last - 1
    while True:  # bcus we are doing it again and again
        while left <= right and arr[left] <= pivot:  # if true increment left
            left = left + 1
            # if any of the condition becomes false come out of d loop
        while left <= right and arr[right] >= pivot:
            right = right - 1
        if right < left:  # the first condition becomes false, we got correct position of pivot, swap
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[last], arr[left] = arr[left], arr[last]  # swap pivot with left element
    return left  # the index where the pivot element is present


def quicksort(arr, first, last):  # recursive call
    # when it contains a single element, first=last don't do anything
    if first < last:  # then execute this code
        p = pivot_place(arr, first, last)  # call pivot element so that we can divide it to left and right
        # divide the list
        quicksort(arr, first, p - 1)  # left sublist
        quicksort(arr, p + 1, last)  # right sublist


arr = [56, 26, 93, 17, 31, 44]
n = len(arr)
quicksort(arr, 0, n - 1)
print(arr)
