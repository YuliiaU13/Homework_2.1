"""
Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

сторона_а (довжина сторони a)
сторона_б (довжина сторони b)
кут_а (кут між сторонами a і b)
кут_б (кут між сторонами b і a)
Необхідно реалізувати наступні вимоги:

Значення сторін повинні бути більше 0.
Сума кутів повинна дорівнювати 360 градусів.
Для встановлення значень атрибутів використовуйте метод setattr.
"""


class Rhombus:
    def __init__(self, side_a, side_b, angle_ab, angle_ba):
        self.side_a = side_a
        self.side_b = side_b
        self.angle_ab = angle_ab
        self.angle_ba = angle_ba
        if not self.check_angles():
            raise ValueError("The sum of angles must be 180 degrees")

    def __setattr__(self, key, value):
        if key in ('side_a', 'side_b'):
            if isinstance(value, (int, float)) and value > 0:
                super().__setattr__(key, value)
            else:
                raise ValueError(f"{key} must be > 0")
        elif key in ('angle_ab', 'angle_ba'):
            if isinstance(value, (int, float)) and 0 < value < 180:
                super().__setattr__(key, value)
            else:
                raise ValueError(f"{key} must be a number between 0 and 180")
        else:
            super().__setattr__(key, value)
        if key in ('angle_ab', 'angle_ba'):
            if not self.check_angles():
                raise ValueError("The sum of angles must be 180 degrees")

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]
        else:
            raise AttributeError(f"'Rhombus' object has no attribute '{item}'")

    def check_angles(self):
        if hasattr(self, 'angle_ab') and hasattr(self, 'angle_ba'):
            if self.angle_ab + self.angle_ba != 180:
                print(f"The sum of angles must be 180 degrees.")
                return False
        return True


if __name__ == '__main__':
    r1 = Rhombus(3, 7, 30, 150)
    print(r1.__dict__)
    # r1.angle_ab = 27
    # print(r1.__dict__)
    # print(r1.__setattr__('angle_ba', 30))
    # print(r1.__setattr__('side_a', -5))
    # print(r1.__dict__)
    print(r1.check_angles())
