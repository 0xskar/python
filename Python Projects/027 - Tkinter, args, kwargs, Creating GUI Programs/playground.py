def add(*args):
    total = 0
    for n in args:
        total += n
    return total


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=6)



class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(model="750")

print(my_car.model, my_car.make)
