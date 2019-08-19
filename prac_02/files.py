user_name = str(input("Please enter your name: "))
name_file = open('name.txt', 'w')
print(user_name, file=name_file)
name_file.close()

name_file = open('name.txt', 'r')
print("Your name is {}".format(name_file.read()))
name_file.close()

numbers_file = open('numbers.txt', 'w')
print("17\n42", file=numbers_file)
numbers_file.close()
numbers_file = open('numbers.txt', 'r')
result = int(numbers_file.readline()) + int(numbers_file.readline())
print(result)
numbers_file.close()

numbers_file = open('numbers.txt', 'r')
result = 0
for line in numbers_file:
    result += int(line)
print(result)
numbers_file.close()
