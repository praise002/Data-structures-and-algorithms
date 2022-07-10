def bubble_sort(elements):
    size = len(elements)  # get the elements size

    for mx in range(size - 1, -1, -1):
        swapped = False
        for j in range(mx):
            if elements[j] > elements[j + 1]:  # comparing 1st with 2nd
                tmp = elements[j]  # temporary variable
                elements[j] = elements[j + 1]  # 1st element goes to 2nd position
                elements[j + 1] = tmp  # 2nd element goes to 1st element
                swapped = True
        if not swapped:
            break  # after 1st iteration


if __name__ == "__main__":
    elements = [("m", 1), ("i", 4), ("s", 4), ("p", 2)]
    bubble_sort(elements)
    print(elements)
