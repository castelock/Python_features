import Person

# The del keyword
p1 = Person('Jhon', 36)
print(p1)
del p1

# Intrinsic Attributes
print('Class attributes')
print(Person.__name__)
print(Person.__module__)
print(Person.__doc__)
print(Person.__dict__)
print('Object attributes')
print(p1.__class__)
print(p1.__dict__)

# Static method
Person.static_function() 