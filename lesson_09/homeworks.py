"""Написати функцію, яка обчислює суму двох чисел"""


def sum_of(a, b):
    return a + b


"""Написати функцію, яка приймає рядок та повертає його у зворотному порядку."""


def vice_versa(some_string):
    return some_string[::-1]


# vice_versa('мало сала')  # алас олам

"""Написати функцію, яка приймає список слів та повертає найдовше слово у списку."""


def word_max(some_list):
    words = [word for word in some_list if isinstance(word, str)]  # беремо тільки слова

    if not words:
        return None

    return max(words, key=len)


"""Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера."""


def cost_item(number_1, number_2):  # monthly_payment and amount_of_months
    return number_1 * number_2


# print(cost_item(1179, 18))