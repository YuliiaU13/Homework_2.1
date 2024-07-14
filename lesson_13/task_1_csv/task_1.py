"""Завдання 1:

Візміть два файли з теки ideas_for_test/work_with_csv
порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv"""

import csv


def result_books_csv(files):
    unique_rows = set()

    for file in files:
        try:
            with open(file, newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    unique_rows.add(tuple(row))
        except FileNotFoundError:
            print(f"File {file} not found.")
            continue

    result_file = 'result_books.csv'

    with open(result_file, 'w', newline='') as result_f:
        writer = csv.writer(result_f)
        for row in unique_rows:
            writer.writerow(row)


files = ['book1.csv', 'book2.csv']
result_books_csv(files)

#old code
# unique_rows = set()

# with open('Book1.csv', newline='') as file1:
#     reader_1 = csv.reader(file1)
#     for row in reader_1:
#         unique_rows.add(tuple(row))
#
# with open('Book2.csv', newline='') as file2:
#     reader_2 = csv.reader(file2)
#     for row in reader_2:
#         unique_rows.add(tuple(row))

# with open('result_books.csv', 'w', newline='') as result_file:
#     writer = csv.writer(result_file)
#     for row in unique_rows:
#         writer.writerow(row)