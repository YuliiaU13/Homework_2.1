"""
Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
"""


def even_numbers(n):
    for number in range(0, n + 1, 2):
        yield number


n = 20
for num in even_numbers(n):
    print(num)

print('--' * 5)


"""
Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
"""


def fibonacci_generator(m):
    a, b = 0, 1
    while a <= m:
        yield a
        a, b = b, a + b


m = 10
for num in fibonacci_generator(m):
    print(num)
