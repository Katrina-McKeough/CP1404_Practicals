from prac_08.unreliable_car import UnreliableCar

UPPER_ATTEMPT_LIMIT = 21
bad_car = UnreliableCar("Toyota Hilux (2007)", 100, 12.34)
decent_car = UnreliableCar("Kia Cerato (2017)", 100, 88.88)
print("{}, reliability of {}".format(bad_car, bad_car.reliability))
print("{}, reliability of {}".format(decent_car, decent_car.reliability))

for i in range(1, UPPER_ATTEMPT_LIMIT):
    print("Attempt {} of driving 5km".format(i))
    print("{} drove {}km".format(bad_car.name, bad_car.drive(5)))
    print("{} drove {}km".format(decent_car.name, decent_car.drive(5)))

print("After drive attempts:")
print(bad_car)
print(decent_car)
