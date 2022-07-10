"""
python program to reverse the given string using recursion
steps:
input ---> string
define recursive fn
print result, reversed str
Base case:
if str1 == ""
    return ""
if str length is 1
    return str
"""


def reverse_str(str1):
    if len(str1) == 1:  #base condition, now it is 1 it returns the last string
        return str1
    else:
        return reverse_str(str1[1:]) + str1[0]  #recursive fn, it keeps executing until str1 is 1


str1 = input("Enter the string: ")
str2 = reverse_str(str1)
print("Reversed string is: ", str2)
