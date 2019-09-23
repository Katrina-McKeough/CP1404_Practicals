from prac_06.guitar import Guitar

guitars = []

print("My guitars!")
name = input("Name: ")
while not name == "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print("{} ({}) : ${:,.2f} added.".format(name, year, cost))
    name = input("Name: ")

# Test code:
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
