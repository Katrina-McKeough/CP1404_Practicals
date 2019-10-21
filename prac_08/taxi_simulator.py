from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """ Taxi simulator program that allows users to choose from available taxis for a trip. """

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_cost = 0
    chosen_taxi = None

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            chosen_taxi = taxis[taxi_choice]
        elif choice == "d":
            if chosen_taxi is None:
                print("Choose a taxi first!")
            else:
                chosen_taxi.start_fare()
                drive_distance = float(input("Drive how far? "))
                chosen_taxi.drive(drive_distance)
                current_trip_cost = chosen_taxi.get_fare()
                total_cost += current_trip_cost
                print("Your {} trip cost you ${:2f}".format(chosen_taxi.name, current_trip_cost))
        else:
            print("Invalid option")
        print("Bill to date: ${:2f}".format(total_cost))
        print(MENU)
        choice = input(">>> ").lower()
    print("Total trip cost: ${:2f}".format(total_cost))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
