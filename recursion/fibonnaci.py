def fibonacci_of(n):
    if n in {0, 1}:  #base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n -2)  #recursive case


print(fibonacci_of(15))
# result = [fibonacci_of(n) in range(15)]
# print(result)