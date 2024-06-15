'''6.4 Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті'''

list_numbers = [12, 3, 44, 5, 0, 8, 93, 7, 4]

# sum_even = 0
# for number in list_numbers:
#     if number % 2 == 0:
#         sum_even += number
# print("Сума парних чисел у списку =", sum_even)

print("Сума парних чисел у списку =", sum([k for k in list_numbers if k % 2 == 0]))