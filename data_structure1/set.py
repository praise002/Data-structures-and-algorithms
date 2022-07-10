"""
It is the collection of unique elements
It is unordered
It is mutable i.e can add and delete element
sets cannot be nested
It can have diff type of element
We can't access element from set using the index
"""

set1 = {1, 1, 2, 2, 3, 1}
s = set()
print(set1)
print(type(s))
s.add(3)
print(s)
s2 = {'run', 3, 4.56, 'sing'}
print(1 in s2)
for i in s2:  #to loop over the set
    print(i)