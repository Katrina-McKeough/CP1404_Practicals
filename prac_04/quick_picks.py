""" Quick Pick Lottery Ticket Generator """
import random

LINE_LENGTH = 6
MIN_VALUE = 1
MAX_VALUE = 45

number_of_picks = int(input("How many quick picks? "))
for i in range(number_of_picks):
    numbers_in_line = []
    for j in range(LINE_LENGTH):
        numbers_in_line.append(random.randint(MIN_VALUE, MAX_VALUE))
        numbers_in_line.sort()
# TODO write code that prints quick picks
