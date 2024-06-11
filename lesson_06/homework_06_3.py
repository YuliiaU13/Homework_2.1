'''6.3 Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який сформує новий list (наприклад lst2),
який містить лише змінні типу стрінг, які присутні в lst1. Дані в лісті можуть бути будь-якими'''

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(lst1)
lst2 = []
for string in lst1:
    if isinstance(string, str):
        if len(string) > 0:
            lst2.append(string)
print(lst2)