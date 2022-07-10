"""Big O Notation"""


# def get_squared_numbers(numbers):
#     squared_numbers = []
#     for n in numbers:
#         squared_numbers.append(n*n)
#     return squared_numbers
#
#
# numbers = [2, 5, 8, 9]
# print(get_squared_numbers(numbers))

"""Challenge""""Array"

monthly_expenses = [2200, 2350, 2600, 2130, 2190]
extra = monthly_expenses[1] - monthly_expenses[0]
print(extra)

first_quarter_expenses = monthly_expenses[0] + monthly_expenses[1] + monthly_expenses[2]
print(first_quarter_expenses)

print(2000 in monthly_expenses)

june_expense = monthly_expenses.append(1980)
print(monthly_expenses)

monthly_expenses[3] = monthly_expenses[3] - 200
print(monthly_expenses[3])
print(monthly_expenses)


"""Challenge 2"""

heros = ['spider man', 'thur', 'hulk', 'iron man', 'captain america']
print(len(heros))
heros.append('black panther')
print(heros)
heros.remove('black panther')
print(heros)
heros.insert(3, 'black panther')
print(heros)
# del heros[1:3]
# print(heros)
# heros.insert(1, 'doctor strange')
# print(heros)
#OR
heros[1:3] = ['doctor strange']
print(heros)
heros.sort()
print(heros)

"""Challenge 3"""

max = int(input('Enter a max number: '))
odd_numbers = []
for i in range(1, max):
    if i % 2 == 1:
        odd_numbers.append(i)

print(f"Odd numbers: {odd_numbers}")

