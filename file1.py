#1
print("Goodbye, World!")

#2
# Variables and types
mystring = "hello"
myfloat = 10.0
myint = 20

# Testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

#3
# Lists 
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

#4
# Basic Operators
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

#5
# String Formatting
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f."

print(format_string % data)

#6
# Basic String Operations
s = "Hey there! Have a seat."

print("Length of s =", len(s))
print("The first occurrence of the letter a =", s.index("a"))
print("a occurs", s.count("a"), "times")
print("The first five characters are '%s'" % s[:5])
print("The next five characters are '%s'" % s[5:10])
print("The thirteenth character is '%s'" % s[12])
print("The characters with odd index are '%s'" % s[1::2])
print("The last five characters are '%s'" % s[-5:])
print("String in uppercase:", s.upper())
print("String in lowercase:", s.lower())

if s.startswith("Hey"):
    print("String starts with 'Hey'. Good!")
if s.endswith("seat."):
    print("String ends with 'seat.'. Good!")

print("Split the words of the string:", s.split())
