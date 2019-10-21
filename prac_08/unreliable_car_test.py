from prac_08.unreliable_car import UnreliableCar

new_unreliable_car = UnreliableCar("Toyota Hilux (2007)", 100, 24.7)
print(new_unreliable_car)
print("Reliability is: {}".format(new_unreliable_car.reliability))
new_unreliable_car.drive(40)
print("After attempting to drive 40km:")
print(new_unreliable_car)
