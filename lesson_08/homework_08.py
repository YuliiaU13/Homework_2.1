# Створіть масив зі строками, які будуть складатися з чисел,
# які розділені комою. Наприклад:
# [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# Для кожного елементу списку виведіть
# суму всіх чисел (створіть нову функцію для цього).
# Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі),
# вам потрібно зловити вийняток і вивести “Не можу це зробити!”
# Використовуйте блок try\except, щоб уникнути інших символів,
# окрім чисел у списку.
# Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”


def sum_of_numbers_in_strings(strings):
    for string in strings:
        try:
            parts = string.split(',') # split the string to parts the "," is separator
            total = sum(int(part) for part in parts) # turn parts to numbers and count their sum
            print(total)
        except ValueError:
            print('Не можу це зробити!') # if there is ValueError, process it and display the text


set_of_strings = ['None,12,23,34,56', 'text1,2,3,4', ' ,,123,1,3', '12,10,1,2,3']

sum_of_numbers_in_strings(set_of_strings)