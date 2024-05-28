# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
bananas = apples * 4
print(bananas)

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = storona_1 + storona_2 + storona_3 + storona_4
print('Периметр = ', perimeter)

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apples = 4
pears = apples + 5
plums = apples - 2
trees_total = apples + pears + plums
print(f'Яблуні = {apples}')
print(f'Груші = {apples} + 5 =', pears)
print(f'Сливи = {apples} - 2 =', plums)
print(f'Всього дерев = {apples} + {pears} + {plums} =', trees_total)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
t1 = 5
dif_t_2 = 10
dif_t_3 = 4
print(f'Температура надвечір = {t1} - {dif_t_2} + {dif_t_3} =', t1 - dif_t_2 + dif_t_3)

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys//2
today_total = boys - 1 + girls - 2
print(f'Дівчат = {boys} : 2 =', girls)
print(f'Дітей сьогодні = ({boys} - 1) + ({girls} - 2) =', today_total)

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book_1 = 8
book_2 = book_1 + 2
book_3 = (book_1 + book_2)//2
book_total = book_1 + book_2 + book_3
print(f'Друга книга = {book_1} + 2 =', book_2)
print(f'Третя книга = ({book_1} + {book_2}) : 2 =', book_3)
print(f'Всі книги = {book_1} + {book_2} + {book_3} =', book_total)