class House:
    def __init__(self, number, name):
        self.street_Number = number
        self.locality_name = name

    def address(self):
        if self.locality_name == "Friends Colony":
            print(self.street_Number, "is located in ", self.locality_name)
        elif self.locality_name == "Lime Garden":
            print(self.street_Number, "is located in ", self.locality_name)
        else:
            print(self.street_Number, "not found in locality", self.locality_name)


home = House(33, "Friends Colony")
print(home.locality_name)
print(home.street_Number)
home.address()

home = House(23, "Lime Garden")
print(home.locality_name)
print(home.street_Number)
home.address()

home = House(11, "Amsterdam")
print(home.locality_name)
print(home.street_Number)
home.address()