def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]
    #method 2
    # if a != b:
    #     tmp = arr[a]
    #     arr[a] = arr[b]
    #     arr[b] = arr[a]


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    # start = pivot_index + 1
    # end = len(elements) - 1

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start = start + 1

        while elements[end] > pivot:
            end = end - 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)  #left partition
        quick_sort(elements, pi + 1, end)  #right partition


if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)

    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements) - 1)
        print(f"Sorted array: {elements}")