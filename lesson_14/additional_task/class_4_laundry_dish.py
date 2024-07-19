from lesson_14.additional_task.class_1_house_devices import HouseDevices
from lesson_14.additional_task.class_2_electronic import ElectronicDevices
from lesson_14.additional_task.class_3_cleaning_washing import WashingDevices, CleaningDevices


class WashingMachine(WashingDevices):  # inheritance from WashingDevices
    def __init__(self, label, model, max_load, rpm, drying, year):
        super().__init__(subtype='washing_machine', label=label, model=model, year=year)
        self.max_load = max_load
        self.rpm = rpm
        self.drying = drying
        self.payment_type = 'in_installments'
        self.__price = 55439

    def get_price(self):  # encapsulation
        print(f'The price of washing_machine is {self.__price} UAH')

    def get_remaining_balance(self, paid_parts, parts=10):  # encapsulation
        if paid_parts > parts:
            raise ValueError("Number of paid parts cannot exceed the number of parts.")
        part_amount = self.__price / parts
        remaining_balance = self.__price - (part_amount * paid_parts)
        print(f'The remaining balance to pay is {remaining_balance} UAH')


class DishWasher(WashingDevices):  # inheritance from WashingDevices
    def __init__(self, label, model, water_cons, energy_class, noise_class, year):
        super().__init__(subtype='dish_washer', label=label, model=model, year=year)
        self.water_cons = water_cons
        self.energy_class = energy_class
        self.noise_class = noise_class


air_conditioning = HouseDevices('electronic', 'cooling', 'air_cooling',
                                'Cooper&Hunter', 'CH-S24XN8', '2022')

fridge = ElectronicDevices('cooling', 'fridge', 'Samsung',
                           'RS67A', '2023')

robot_cleaner = CleaningDevices('robot_vacuum', 'Xiaomi', 'S10+', '2024')

washing_machine = WashingMachine('Bosh', 'WGB24400', 9, 1400, 'no', 2023)

dish_washer = DishWasher('Bosh', 'SMS4HMI07E', 9, 'D', 'B', 2022)

air_conditioning.say_class_name()  # Polymorphism
print('The year of air_conditioning:', air_conditioning.year)
air_conditioning.set_year('2023')
print('The changed year of air_conditioning:', air_conditioning.year)

fridge.say_class_name()  # Polymorphism
fridge.say_function()  # Polymorphism

robot_cleaner.say_class_name()  # Polymorphism
robot_cleaner.say_function()  # Polymorphism
print(f'Payment type for robot_cleaner is: {robot_cleaner.payment_type}')

washing_machine.say_class_name()  # Polymorphism
washing_machine.say_function()  # Polymorphism
print(f'Payment type for washing_machine is: {washing_machine.payment_type}')
washing_machine.get_price()
washing_machine.get_remaining_balance(5)