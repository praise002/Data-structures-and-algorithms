def bubble_sort(elements, key="name"):
    size = len(elements)  # get the elements size

    for i in range(size - 1):
        swapped = False
        for j in range(size - 1):
            if (elements[j][key]) > (elements[j + 1][key]):  # comparing 1st with 2nd
                tmp = elements[j]  # temporary variable
                elements[j] = elements[j + 1]  # 1st element goes to 2nd position
                elements[j + 1] = tmp  # 2nd element goes to 1st element
                swapped = True
        if not swapped:
            break  # after 1st iteration


if __name__ == "__main__":

    elements = [
        {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
        {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
        {"name": "aamir", "transaction_amount": 800, "device": "iphone-8"},
        {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"}
    ]
    bubble_sort(elements)
    print(elements)
