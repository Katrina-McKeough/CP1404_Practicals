from prac_08.car import Car
from random import uniform


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability=0.0):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but only if reliability permits."""
        if uniform(1, 100) >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
