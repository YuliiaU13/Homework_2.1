from lesson_14.additional_task.class_1_house_devices import HouseDevices


class ElectronicDevices(HouseDevices):  # inheritance from HouseDevices
    def __init__(self, function, subtype, label, model, year):
        super().__init__(category='Electronic', function=function, subtype=subtype, label=label, model=model, year=year)

    def say_class_name(self):
        print('This class is ElectronicDevices')

    def say_function(self):
        print(f'This device is for {self.function}')
