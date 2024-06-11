'''6.1 Порахувати кількість унікальних символів в строці.
Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()
'''

# creation of string 'I am working from Monday to Sunday 4 weeks per month.' via input
# the shorter one: 'It's too much'
input_string = input('Введіть рядок: ')

# getting the unique symbols:
unique_symbols = set(input_string)
print(unique_symbols)

# number of unique symbols:
unique_symbols_number = len(unique_symbols)
print(unique_symbols_number)

# condition > 10 symbols => True, else => False
if unique_symbols_number > 10:
    print(True)
else:
    print(False)