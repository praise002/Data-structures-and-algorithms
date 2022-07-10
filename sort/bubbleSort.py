def bubble_sort(elements):
    size = len(elements)  #get the elements size

    for i in range(size - 1):  #if its range(2), it sorts twice
        swapped = False
        for j in range(size - 1 - i):  #bcus we want to compare it all the way to 34, after it no other element, -iwhen in 2nd itr go all the way to n-2 ele
            if elements[j] > elements[j + 1]:  #comparing 1st with 2nd
                tmp = elements[j]  #temporary variable
                elements[j] = elements[j + 1]  #1st element goes to 2nd position
                elements[j + 1] = tmp  #2nd element goes to 1st element
                swapped = True
        if not swapped:
            break   #after 1st iteration


if __name__ == "__main__":
    # elements = [5, 9, 2, 1, 67, 34, 88, 34]
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    bubble_sort(elements)
    print(elements)
