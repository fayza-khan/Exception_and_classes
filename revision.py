class Sample:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def properties_name_age(self):
        print("Name of the person is", self.name, ".")
        print("Age of the person is", self.age, ".")

    def future_age(self):
        x = int(input("Add the additional years, to get future age here:"))
        print("Age of the person named", self.name, " after", x, "years is", self.age+x)


John = Sample("John", 20)
John.properties_name_age()
John.future_age()
