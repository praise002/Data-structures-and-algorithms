import hashlib

a = hash(3.14)
print(a)
b = hash(3.14)
print(b)
c = hash(3.1415986754678)
print(c)
d = hash('Lorem')
print(d)
print(hash('lorem'))
print(hash(None))
print(hash(hash))
# print(hash([1, 2, 3]))  #error