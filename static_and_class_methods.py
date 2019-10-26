import datetime


class Person:
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

    @staticmethod
    def is_teen(age):
        """This is a toolbox function - it does not affect class properties"""
        return age in range(13, 20)

    def check_teenager(self):
        return self.age in range(13, 20)

    @classmethod
    def from_birthyear(cls, name, year):
        """Method bound to the class itself. As results it will return Person class
        Used for factories - creating collection of classes"""
        age = datetime.datetime.now().year - year
        return cls(name=name, age=age)


factory_parameters = {
    'Jeff': 2001,
    'Mike': 1895,
    'James': 2013,
    'Kilo': 2016,
    'Lima': 1985,
}
# created a collection of classes from factory_parameters
factory = [Person.from_birthyear(key, value) for key, value in factory_parameters.items()]
print(factory)
