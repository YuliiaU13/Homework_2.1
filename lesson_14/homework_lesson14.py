"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.
"""


class Student:

    def __init__(self, first_name, second_name, age, avg_score):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.avg_score = avg_score

    def set_avg_score(self, avg_score):
        self.avg_score = avg_score

    def get_info(self):
        return (f'{self.first_name} {self.second_name}, {self.age}, '
                f'score is {self.avg_score}')


student_1 = Student('Alyona', 'Chernenko', 19, 74.5)
print(student_1.get_info())

student_1.set_avg_score('91.5')
print(student_1.get_info())
