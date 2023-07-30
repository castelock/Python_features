class Person:
    """ An example class to hold a person's name and age"""

    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count +=1

    def __init__(self, name, age):
        # Class side data
        # Person.instance_count += 1
        # Class side method
        Person.increment_instance_count()
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' is ' + str(self.age)
    
    def calculate_pay(self, hours_worked):
        rate_of_pay = 7.50
        if self.age >= 21:
            rate_of_pay += 2.50
        return hours_worked * rate_of_pay
    
    @staticmethod
    def static_function():
        print('Static method')
    
