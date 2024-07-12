"""Завдання 1:

Візміть два файли з теки ideas_for_test/work_with_csv
порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv"""

import csv

unique_rows = set()

# with open('random.csv', newline='') as file1:
#     reader_1 = csv.reader(file1)
#     for row in reader_1:
#         unique_rows.add(tuple(row))
#
# with open('random-michaels.csv', newline='') as file2:
#     reader_2 = csv.reader(file2)
#     for row in reader_2:
#         unique_rows.add(tuple(row))
#
# with open('result_random.csv', 'w', newline='') as result_file:
#     writer = csv.writer(result_file)
#     for row in unique_rows:
#         writer.writerow(row)


with open('Book1.csv', newline='') as file1:
    reader_1 = csv.reader(file1)
    for row in reader_1:
        unique_rows.add(tuple(row))

with open('Book2.csv', newline='') as file2:
    reader_2 = csv.reader(file2)
    for row in reader_2:
        unique_rows.add(tuple(row))

with open('result_books.csv', 'w', newline='') as result_file:
    writer = csv.writer(result_file)
    for row in unique_rows:
        writer.writerow(row)
