# 1) Розробіть функцію is_palindrome, яка приймає рядок і повертає True,
# якщо рядок є паліндромом (читається однаково зліва направо і справа наліво) та False
# в іншому випадку. Напишіть тести для перевірки роботу функції на різних вхідних текстах.

def is_palindrome(some_string):
    some_string = some_string.replace(' ', '').lower()
    return some_string == some_string[::-1]


print(is_palindrome('assassa'))

# Список містить словники - дані про ціну і тираж кожного з журналів.
# Скласти програму, яка визначає середню вартість журналів,
# тираж яких більше 10 000 примірників.

journal_list = [
    {"name": "National Geographic", "volume": 15000, "price": 7.99},
    {"name": "Time", "volume": 20000, "price": 5.99},
    {"name": "Vogue", "volume": 18000, "price": 6.99},
    {"name": "Forbes", "volume": 10000, "price": 6.99},
    {"name": "Scientific American", "volume": 9000, "price": 9.99},
    {"name": "Sports Illustrated", "volume": 12000, "price": 4.99},
    {"name": "The New Yorker", "volume": 11000, "price": 8.99},
    {"name": "Cosmopolitan", "volume": 17000, "price": 5.99},
    {"name": "Wired", "volume": 6000, "price": 7.99},
    {"name": "Rolling Stone", "volume": 9000, "price": 6.99}
]

volume_param = 10000


def get_avg_price(some_list):
    sum_price = 0
    total_number = 0
    for journal in some_list:
        if journal['volume'] > volume_param:
            sum_price += journal['price']
            total_number += 1
        if total_number == 0:
            return 0
    return round((sum_price / total_number), 2)


print(get_avg_price(journal_list))
