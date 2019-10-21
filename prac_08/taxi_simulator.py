from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """ Taxi simulator program that allows users to choose from available taxis for a trip. """

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))
        elif choice == "d":
            print("")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").lower()
    print("Total trip cost: ")


main()
