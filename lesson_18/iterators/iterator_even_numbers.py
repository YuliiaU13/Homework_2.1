"""
Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
"""


class EvenNumbersIterator:
    def __init__(self, current, n):
        self.current = current
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        while self.current <= self.n and self.current % 2 != 0:
            self.current += 1
        if self.current > self.n:
            raise StopIteration
        result = self.current
        self.current += 2
        return result


even_iterator = EvenNumbersIterator(1, 10)
for num in even_iterator:
    print(num)
