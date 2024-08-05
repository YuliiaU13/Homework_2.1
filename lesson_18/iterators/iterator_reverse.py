"""
Реалізуйте ітератор для зворотного виведення елементів списку.
"""


class ReverseListIterator:
    def __init__(self, some_list):
        self.some_list = some_list
        self.index = len(some_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.some_list[self.index]


new_list = [1, 2, 3, 4, 5]
reverse_iterator = ReverseListIterator(new_list)
for item in reverse_iterator:
    print(item)
