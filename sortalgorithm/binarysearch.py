def binary_search(list1, key):
    low = 0
    high = len(list1) - 1
    found = False
    while low <= high and not found:  #if found is true
        mid = (low + high) // 2
        if key == list1[mid]:
            found = True
        elif key > list1[mid]:
            low = mid + 1
        else:
            high = mid - 1

    if found:
        found = True
        print(key, "is found.")
    else:
        found = False
        print(key, "is not present in list.")


list1 = [23, 1, 4, 2, 3]
list1.sort()
print(list1)
key = int(input("Enter the key: "))
binary_search(list1, key)
