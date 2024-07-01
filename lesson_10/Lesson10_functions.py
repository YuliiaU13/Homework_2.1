def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# print(factorial(3))


def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)


# print(is_anagram('asd', 'fgh'))


def filter_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]


print(filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def find_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


# print(find_primes(10))


def triangle_area(a, b, c):
    # if a + b <= c or a + c <= b or b + c <= a:
    #     return 0
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


# print(round(triangle_area(6, 6, 6), 3))


def convert_to_24_hour(time_str):
    parts = time_str.split()
    if len(parts) != 2:
        raise ValueError('Time format is not a `hh:mm period`')
    time, period = parts
    hours, minutes = map(int, time.split(':'))
    if period.lower() == 'pm' and hours != 12:
        hours += 12
    elif period.lower() == 'am' and hours == 12:
        hours = 0
    return f'{hours:02}:{minutes:02}'


# print(convert_to_24_hour("12:23 PM"))


# def convert_to_24_hour(time_str):
#     parts = time_str.split()
#     if len(parts) != 2:
#         raise ValueError('Time format is not a `hh:mm period`')
#
#     time, period = parts
#
#     if period.lower() not in ['am', 'pm']:
#         raise ValueError('Time period must be AM or PM')
#
#     try:
#         hours, minutes = map(int, time.split(':'))
#     except ValueError:
#         raise ValueError('Time must be in `hh:mm` format')
#
#     if not (0 <= hours <= 12) or not (0 <= minutes < 60):
#         raise ValueError('Hour must be between 0 and 12, and minutes between 0 and 59')
#
#     if period.lower() == 'pm' and hours != 12:
#         hours += 12
#     elif period.lower() == 'am' and hours == 12:
#         hours = 0
#
#     return f'{hours:02}:{minutes:02}'


# print(convert_to_24_hour("15:03 PM"))
