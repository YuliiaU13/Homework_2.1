class HouseDevices:
    def __init__(self, category, function, subtype, label, model, year):
        self.category = category
        self.function = function
        self.subtype = subtype
        self.label = label
        self.model = model
        self.year = year
        self.payment_type = 'paid'

    def say_class_name(self):
        print('This class is HouseDevices')

    def set_year(self, year):
        self.year = year
