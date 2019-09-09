""" Quick Pick Lottery Ticket Generator """
import random

LINE_LENGTH = 6
MIN_VALUE = 1
MAX_VALUE = 45

number_of_picks = int(input("How many quick picks? "))
for i in range(number_of_picks):
    quick_pick = []
    for j in range(LINE_LENGTH):
        number = random.randint(MIN_VALUE, MAX_VALUE)
        while number in quick_pick:
            number = random.randint(MIN_VALUE, MAX_VALUE)
        quick_pick.append(number)
    quick_pick.sort()
    formatted_quick_pick = []
    for number in quick_pick:
        formatted_quick_pick.append("{:2d}".format(number))
    print(" ".join(formatted_quick_pick))
