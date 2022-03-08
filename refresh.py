# hello world
print('Hello Python')

# declare variable
x = 10
y = 5
z = x + y
print('x + y is ' + str(z))

# declare function
def say_hello(name):
    print('Hello ' + name)

def toUpper(name):
    return name.upper()


say_hello(toUpper('jeff'))

# check type
if type("hello") is str:
    print("hello is a string")

# if-else block
my_name = 'Jeff'

if my_name == 'Jameson':
    print('Hi Jameson')
elif my_name == "Nathan":
    print("Hi Nathan")
else:
    print("Hi Jeff")

# while block
i = 0
while i < 5:
    print('i is now ' + str(i))
    i += 1

# for loop
animals = ["cat", "dog", "fish"]

for animal in animals:
    print(animal)

# classes
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

rover = Dog("rover", 6)
print(rover.name + " is " + str(rover.age) + " years old")

# currying
def addNums(num1):
    def curry(num2):
        return num1 + num2
    return curry

add5 = addNums(5)

print(add5(10))

# type annotations - not enforced, but can be used
# with a linter
# in vsCode, you can use MyPy
# which also needs to be downloaded like so:
# python3 -m pip install -U mypy

def printString(name: str):
    print(name)

# printString(5) # mypy catches the error before it runs
# try-catch
try:
    print(10 / 0)
except:
    print("You can't divide by 0!")
    