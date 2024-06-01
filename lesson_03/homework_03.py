#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = """
"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to", said the Cat.
"I don\'t much care where" —— said Alice.
"Then it doesn\'t matter which way you go", —— said the Cat.
"So long as I get somewhere", Alice added as an explanation.
"Oh, you\'re sure to do that", said the Cat, "if you only walk long enough."
"""
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_s = 436402
azov_sea_s = 37800
sum_s = black_sea_s + azov_sea_s
print(f'Площа Чорного та Азовського морів разом =\n'
      f'= Площа Чорного моря + Площа Азовського моря =\n'
      f'= {black_sea_s} + {azov_sea_s} = {sum_s} км2')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

all_stores = 375291
first_and_second = 250449
third_and_second = 222950
third_store = all_stores - first_and_second
second_store = third_and_second - third_store
first_store = first_and_second - second_store
sum_stores = third_store + second_store + first_store
print(f'Кількість товарів на третьому складі =\n'
      f'= Всі товари - Товари на першому та другому складі разом =\n'
      f'= {all_stores} - {first_and_second} = {third_store} шт.')

print(f'Кількість товарів на другому складі =\n'
      f'= Товари на третьому та другому складі разом - Товари на третьому складі =\n'
      f'= {third_and_second} - {third_store} = {second_store} шт.')

print(f'Кількість товарів на першому складі =\n'
      f'= Товари на першому та другому складах разом - Товари на другому складі =\n'
      f'= {first_and_second} - {second_store} = {first_store} шт.')

print(f'Перевірка: Кількість на першому + Кількість на другому + Кількість на третьому =\n'
      f'= {third_store} + {second_store} + {first_store} = {sum_stores} = {all_stores} шт.\n')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179
month_number = 18
cost = monthly_payment * month_number
print(f'Вартість комп\'ютера = Місячна плата * Кількість місяців =\n'
      f'= {monthly_payment} * {month_number} = {cost} грн')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019
ratio_a = a//8
reminder_a = a%8
print(f'a) {a} : 8 = {ratio_a}, остача {reminder_a}')

b = 9907
ratio_b = b//9
reminder_b = b%9
print(f'b) {b} : 9 = {ratio_b}, остача {reminder_b}')

c = 2789
ratio_c = c//5
reminder_c = c%5
print(f'c) {c} : 5 = {ratio_c}, остача {reminder_c}')

d = 7248
ratio_d = d//6
reminder_d = c%6
print(f'd) {d} : 6 = {ratio_d}, остача {reminder_d}')

e = 7128
ratio_e = e//5
reminder_e = c%5
print(f'e) {e} : 5 = {ratio_e}, остача {reminder_e}')

f = 19224
ratio_f = f//9
reminder_f = f%9
print(f'f) {f} : 9 = {ratio_f}, остача {reminder_f}')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza = 274*4
middle_pizza = 218*2
juice = 35*4
cake = 350*1
water = 21*3
money_amount = big_pizza + middle_pizza + juice + cake + water
print(f'Кількість грошей = 274*4 + 218*2 + 35*4 + 350*1 + 21*3 =\n'
      f'= {money_amount} грн')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos = 232
photo_on_page = 8
print(f'Кількість сторінок = Кількість фото : Фото на одній сторінці =\n'
      f'= {photos // photo_on_page} шт.')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
s = 1600
petrol_100_km = 9
tank_capacity = 48
petrol_total = 1600/100*9
stops = petrol_total/tank_capacity
print(f'Літрів бензину на подорож = \n'
      f'= Відстань : 100 км * Літрів бензину на 100 км =\n'
      f'= {s} / 100 * 9 = {petrol_total} л')
print(f'Кількість заправок = Літрів бензину на подорож : Місткість баку =\n'
      f'= {petrol_total} / {tank_capacity} = {stops}')