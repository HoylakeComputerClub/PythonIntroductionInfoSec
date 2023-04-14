# Variables
# Box to put data in to
# numbers

# Integer (Whole Numbers)
numInt = 2345

# Float (Decimal)
numFloat = 12.6


# String (1 or more characters)
lettter = "A"
sentence = "the red fox"
word = "hello"

# Math (operations)

# + - * / ** %
a = 2 * 4
b = 3 + 4
c = 10 / 2
d = 2 ** 3 # 2 * 2 * 2
e = 10 % 3

name1 = "dave"
name2 = "joe"
name3 = name1 + " " + name2
"dave joe"

num1 = 10
num2 = "34"

l = [1, 2, 3, 4]



num3 = int(num2) * num1 # 340
string1 = str(num1) + num2 # "1034"
string2 = num1 + int(num2) # 340
string3 = str(num1 + int(num2)) # "340"


names = "bob dave joe steve"
namesList = names.split()

for name in namesList:
    for letter in name:
        print(letter, hex(ord(letter)))

[2, 4, 1, 78, 3, 45].sort()

