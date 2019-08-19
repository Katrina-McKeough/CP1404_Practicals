for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(1, 21):
    print(21 - i, end=' ')
print()

star_number = int(input("Please enter a number: "))
for i in range(star_number):
    print("*", end='')
print()

for i in range(1, star_number + 1):
    print("*" * i)
print()
