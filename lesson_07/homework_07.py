# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    # Initialize the appropriate variable:
    multiplier = 1

    # Complete the while loop condition:
    while True:
        result = number * multiplier
        if result > 25:
            # Enter the action to take if the result is greater than 25:
            break
        print(f'{number}x{multiplier}={result}')

        # Increment the appropriate variable:
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# ...


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


# 1 variant
def sum_of(a, b):
    return a + b


print(sum_of(3, 15))


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def calculate_average(numbers):
    # перевірка, чи список не пустий та вивід повідомлення:
    if len(numbers) == 0:
        print('Неможливо зробити обчислення, список порожній')
        return None
    # перевірка, чи є у списку елементи "не числа":
    for element in numbers:
        if not isinstance(element, (int, float)):
            print(f'Неможливо зробити обчислення. Цей елемент не число: "{element}"')
            return None
    # формула для знаходження шуканого:
    average = sum(numbers) / len(numbers)

    print(average)


list_numbers_1 = ['', 12, 3, 'abc', 5, 0, 8, 93, 7, 4, 'xyz']
list_numbers_2 = []
list_numbers_3 = [12, 3, 5, 0, 8, 93, 7, 4]
calculate_average(list_numbers_1)
calculate_average(list_numbers_2)
calculate_average(list_numbers_3)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def vice_versa(some_string):
    print(f'Рядок у зворотному порядку: {some_string[::-1]}')


vice_versa('мало сала')


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def word_max(some_list):
    words = [word for word in some_list if isinstance(word, str)] # беремо тільки слова

    if not words:
        return None

    return max(words, key=len)


some_list = ['vacation', 123456, ('hello', 'hi', 'good bye'), 45.6, {'car': 'ford'}, True]
longest_word = word_max(some_list)
print('Найдовше слово у списку:', longest_word)


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Welcome to Ukraine!"
str2 = "Ukraine"
print(find_substring(str1, str2)) # поверне 11

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""


# task 7
"""
Знайди остачу від ділення чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

# old variant:
a = 8019
ratio_a = a//8
reminder_a = a%8
print(f'a) {a} : 8 = {ratio_a}, остача {reminder_a}')


# new variant:
def reminder_devision(a, b):
    print(f'{a} : {b} = {a//b}, остача {a%8}')

reminder_devision(8019, 8)


# task 8
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
# old variant:
# monthly_payment = 1179
# month_number = 18
# cost = monthly_payment * month_number
# print(f'Вартість комп\'ютера = Місячна плата * Кількість місяців =\n'
#       f'= {monthly_payment} * {month_number} = {cost} грн')


# new variant with input:
# def cost_item():
#     input_monthly_payment = float(input('Введіть суму місячної плати у цифрах: '))
#     input_month_number = float(input('Введіть кількість місяців оплати частинами у цифрах: '))
#     cost = input_monthly_payment * input_month_number
#     print(f'Вартість комп\'ютера = {cost:.2f} грн')
#
#
# cost_item()


# new variant without input:
def cost_item_2(number_1, number_2): # monthly_payment and amount_of_months
    cost = number_1 * number_2
    print(f'Вартість комп\'ютера = {cost:.2f} грн')


cost_item_2(1179, 18)

# task 9
'''6.3 Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який сформує новий list (наприклад lst2),
який містить лише змінні типу стрінг, які присутні в lst1. Дані в лісті можуть бути будь-якими'''

# old variant:
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(lst1)
lst2 = []
for string in lst1:
    if isinstance(string, str):
        lst2.append(string)
print(lst2)


# new variant:
def list_creation_str(some_list):
    new_list = []
    for element in some_list:
        if isinstance(element, str):
            new_list.append(element)
    print(new_list)


list_creation_str(lst1)

# task 10

'''6.1 Порахувати кількість унікальних символів в строці.
Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()
'''

# old variant:
# unique_symbols_number = len(set(input('Введіть рядок: ')))
# print(True) if unique_symbols_number >10 else print(False)


# new variant
def unique_symbols_10():
    unique_symbols_number = len(set(input('Введіть рядок: ')))
    print(True) if unique_symbols_number > 10 else print(False)

unique_symbols_10() # I am working from Monday to Sunday 4 weeks per month. -> True
unique_symbols_10() # It's too much -> False