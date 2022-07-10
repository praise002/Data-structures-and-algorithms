# def hash_fn(text):
#     return sum(ord(character) for character in text)  #sum is iterable


# print(hash_fn('lorem'))
# print(hash_fn('loren'))
# print(hash_fn('loner'))  #produce same value as above, leads to hash collisions

#to fix it
# def hash_fn(key):
#     return sum(ord(character) for character in str(key))  #be able to deal with any type of argument


# print(hash_fn('lorem'))
# print(hash_fn(3.14))
# print(hash_fn(True))
# print(id('Lorem') ) #objects memory address, not secure, it is predictable, it doesnt have a uniform distribution
# print(hash_fn('3.14'))
# print(hash_fn(3.14))  #same output needs to fix
# print(repr('3.14'))
# print(repr(3.14))


def hash_fn(key):
    return sum(ord(character) for character in repr(key))   #to distinguish strings from numbers


print(hash_fn('3.14'))   #strings are now distinguishable from numbers
print(hash_fn(3.14))


letters = ['a', 'b', 'c']
for letter in enumerate(letters):
    print(letter)    #it prints the index and the letter enclosed in a tuple

#to tackle the issue with anagram like loren and loner


def hash_function(key):
    return sum(index * ord(character)
               for index, character in enumerate(repr(key).lstrip(" "), start=1))  #starts from 1 so first index is not discarded as 0


#the longer the string the bigger the hash code
print(hash_function('Tiny'))
print(hash_function('This has a somewhat medium length.'))
print(hash_function('This is very long and slow! * 1_000_000'))

#to address unbounded growth take the modulo % of ur hash code against a known max size
print(hash_function('Tiny') % 100)
print(hash_function('This has a somewhat medium length.') % 100)
print(hash_function('This is very long and slow! * 1_000_000') % 100)

print(hash_function('a'), hash_function('b'), hash_function('c'))

import sys
print(sys.hash_info)
print(sys.hash_info.algorithm)


