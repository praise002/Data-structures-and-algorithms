def insertion_sort(my_list):
    for i in range(1, len(my_list)):  #we are comparing index 1 with index 0 range(1, 5)
        current_element = my_list[i]  #it points to index 1, then index 2 will be next
        pos = i
        while current_element < my_list[pos - 1] and pos > 0:  #the pos-1 is 0 index
            my_list[pos] = my_list[pos - 1]  #we swap
            pos = pos - 1  #check its comparism with other values

        #if d condition becomes false
        my_list[pos] = current_element


list1 = [2, 4, 3, 5, 1]
insertion_sort(list1)
print(list1)


"""descending order"""


def insertion_sort(my_list):
    for i in range(1, len(my_list)):  #we are comparing index 1 with index 0 range(1, 5)
        current_element = my_list[i]  #it points to index 1, then index 2 will be next
        pos = i
        while current_element > my_list[pos - 1] and pos > 0:  #the pos-1 is 0 index
            my_list[pos] = my_list[pos - 1]  #we swap
            pos = pos - 1  #check its comparism with other values

        #if d condition becomes false
        my_list[pos] = current_element


list1 = [2, 4, 3, 5, 1]
insertion_sort(list1)
print(list1)