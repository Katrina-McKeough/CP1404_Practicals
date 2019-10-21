from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """ Taxi simulator program that allows users to choose from available taxis for a trip. """

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_cost = 0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            chosen_taxi = input("Choose taxi: ")
        elif choice == "d":
            print("")
        else:
            print("Invalid option")
        print("Bill to date: ${:2f}".format(total_cost))
        print(MENU)
        choice = input(">>> ").lower()
    print("Total trip cost: ${:2f}".format(total_cost))
    print("Taxis are now:")


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
