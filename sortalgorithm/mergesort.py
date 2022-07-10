def merge_sort(list1):
    if len(list1) > 1:  #bse call, stopping condition
        mid = len(list1) // 2  # tof ind d mid element
        left_sublist = list1[:mid]  # from 0 to mid, excluding d mid
        right_sublist = list1[mid:]  # from mid to end
        merge_sort(left_sublist)  # recursive call
        merge_sort(right_sublist)
        i = 0
        j = 0
        k = 0

        #condition for merging
        while i < len(left_sublist) and j < len(right_sublist):  #i is index of left list
            if left_sublist[i] < right_sublist[j]:
                list1[k] = left_sublist[i]
                i = i + 1
                k = k + 1
            else:
                list1[k] = right_sublist[j]
                j = j + 1
                k = k + 1

        #to check values that are left out
        while i < len(left_sublist):
            list1[k] = left_sublist[i]
            i = i + 1
            k = k + 1

        while j < len(right_sublist):
            list1[k] = right_sublist[j]
            j = j + 1
            k = k + 1


#get input from user
num = int(input("How many elements do you want in the list:"))
list1 = [int(input()) for x in range(num)]
merge_sort(list1)
print("Sorted list is:", list1)