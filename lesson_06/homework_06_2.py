'''6.2 Напишіть цикл, який буде вимагати від користувача ввести слово,
в якому є літера "h" (враховуються як великі так і маленькі).
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".'''

# while True:
#     input_word_h = input('Введіть одне слово, в якому є літера "h" або "H": ')
#     if ' ' not in input_word_h and ('h' in input_word_h or 'H' in input_word_h):
#         print("Супер :) Ви ввели вірне слово: ", input_word_h)
#         break
#     else:
#         print('Халепа :( Слово не містить необхідну літеру, або введено більше ніж одне слово.')

# variant with two separate checks (continue) with 2 if and without else:
while True:
    input_word_h = input('Введіть одне слово, в якому є літера "h" або "H": ')

    if ' ' in input_word_h:
        print('Халепа :( Введено більше ніж одне слово.')
        continue
    if 'h' in input_word_h.lower():
        print('Супер :) Ви ввели вірне слово: ', input_word_h)
        break

    print('Халепа :( Слово не містить необхідну літеру.')