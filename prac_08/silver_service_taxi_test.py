from prac_08.silver_service_taxi import SilverServiceTaxi

print("Example SilverServiceTaxi with fanciness of 4:")
really_fancy_taxi = SilverServiceTaxi("Hummer", 200, 4)
print(really_fancy_taxi)

print("Example SilverServiceTaxi with fanciness of 2:")
somewhat_fancy_taxi = SilverServiceTaxi("Bigger Kia Cerato (2017)", 100, 2)
print(somewhat_fancy_taxi)

print("After driving 18km:")
somewhat_fancy_taxi.drive(18)
print(somewhat_fancy_taxi)
print("Fare is ${} (expected $48.78)".format(somewhat_fancy_taxi.get_fare()))
