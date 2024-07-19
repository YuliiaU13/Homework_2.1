from lesson_14.additional_task.class_2_electronic import ElectronicDevices


class CleaningDevices(ElectronicDevices):  # inheritance from ElectronicDevices
    def __init__(self, subtype, label, model, year):
        super().__init__(function='cleaning', subtype=subtype, label=label, model=model, year=year)

    def say_class_name(self):
        print('This class is CleaningDevices')


class WashingDevices(ElectronicDevices):  # inheritance from ElectronicDevices
    def __init__(self, subtype, label, model, year):
        super().__init__(function='washing', subtype=subtype, label=label, model=model, year=year)

    def say_class_name(self):
        print('This class is WashingDevices')