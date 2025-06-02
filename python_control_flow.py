# # Control flow tools
# users = {"Hans": "active", "Bogdan": "inactive"}
#
# other_users = users.copy()
#
# other_users["Simona"] = "active"
#
# # Dicts are mutable
# # To bypass this mutability you can use the copy() method
# print(other_users)
#
# print(users)
#
# print("items: ")
#
# print(users.items())
#
# items = users.items()
#
# print(type(items))

# delete inactive users:

# users = {"Hans": "active", "Bogdan": "inactive", "Simona": "active"}
#
# for user, status in users.copy().items():
#     if status == "inactive":
#         del users[user]
#
# print(users)

users = {"Hans": "active", "Bogdan": "inactive", "Simona": "active"}

# This throws an error: dictionary changed size during iteration

# for user, status in users.items():
#     if status == "inactive":
#         del users[user]
#
# print(users)

# To make it work you must use a copy of the dictionary

copy = users.copy()
print(type(copy))


for user, status in users.copy().items():
    if status == "inactive":
        del users[user]

print(users)

# Range function

# for i in range(0, 5):
#     print(i, end=",")

for i in range(10, 2, -2):
    print(i, end=",")

a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i])

for i, word in enumerate(a):
    print(i, word)

b = range(0, 5)

print(type(b))
print(b)

# Break and continue statements

for i in range(2, 10):
    if i % 2 == 0:
        print(f"Found an even number: {i}")
        continue
    print(f"Found an odd number: {i}")

# else Clauses on Loops

# In a for or while loop the break statement may be paired with an else clause. If the loop finishes without executing the break, the else clause executes.
#
# In a for loop, the else clause is executed after the loop finishes its final iteration, that is, if no break occurred.
#
# In a while loop, it’s executed after the loop’s condition becomes false.
#
# In either kind of loop, the else clause is not executed if the loop was terminated by a break. Of course, other ways of ending the loop early, such as a return or a raised exception, will also skip execution of the else clause.
print("else Clauses on Loops")

for i in range (2, 2):
    print(i)

for n in range(2, 10):
    for x in range(2, n):
        print(n, "%", x)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# Match statements

print("------------------------")
print("Match statements")

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401:
            return "Unauthorized"
        case _ :
            return "OK"

print(http_error(400))
print(http_error(401))
print(http_error(510))

def http_error(status):
    match status:
        case 400 | 401:
            return "Not allowed"
    return "OK"

print(http_error(400))
print(http_error(401))
print(http_error(510))

# Patterns can look like unpacking assignments, and can be used to bind variables:

def match_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"0, y={y}"
        case (x, 0):
            return f"x={x}, 0"
        case (x, y):
            return f"x={x}, y = {y}"
        case _:
            raise ValueError("Not a point")

# print(match_point((0, 0)))
# print(match_point((0, 3)))
# print(match_point((4, 0)))
# print(match_point((2, 3)))
# print(match_point(2))


class Point:
    def __repr__(self):
        print(self.x, self.y)
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            return "Origin"
        case Point(x=0, y=y):
            return f"0, y={y}"
        case Point(x=x, y=0):
            return f"x={x}, 0"
        case Point():
            return "Somewhere else..."
        case _:
            raise ValueError("Not a point!")

#p = Point(10, 12)

# print("here")
# print(where_is(Point(0, 0)))
# print(where_is(Point(0, 2)))
# print(where_is(Point(2, 0)))
# print(where_is(p))
# print(where_is((2, 3)))


# point = Point(y=2, x=4)
#
# print(point)


class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

#points = [Point(0, 0), Point(0, 2)]
points = [2, 3]
match points:
    case []:
        print("No points ")
    case [Point(0, 0)]:
        print("Origin")
    case [Point(0, y1), Point(0, y2)]:
        print("Two points on the Y axis")
    case _:
        print("Not a point")

# We can add an if statement to a pattern, called "guard".
# Note that value capture happens before guard is evaluated!

p: Point = Point(2 , 3)

match p:
    case Point(x, y) if x == y:
        print(f"X == Y")
    case Point(x, y):
        print("Not on diagonal")

x1 = 2
y2: int = 3
#l = [x, y, 4, 5, 6]
l = [2, x1, 4, 5, 6]

l = [1, 3, 4, 5 ,6]
match l:
    case [y2, x1, *rest]:
        print("that's true")
        print(y2, x1)
        print(*rest)
    # case [x1, y2, *_]:
    #     print("that's also true")
    case _:
        print("that's false")

# l = [1, 2, 3, 4, 5, 6]
# match l:
#     case [y2, x1, *rest]:
#         print("that's true")
#         print(y2, x1)
#         print(type(rest))
#         print(type(*rest))
#     # case [x1, y2, *_]:
#     #     print("that's also true")
#     case _:
#         print("that's false")

#dict = {"bandwith": 100, "latency": 23, "speed": 150}
dict = {"bandwith": 50, "speed": 100, "latency": 35}

match dict:
    case {"bandwith": b, "latency": l}:
        print("True")
    case _:
        print("False")

d = {"bandwidth": 100, "latency": 20, "protocol": "HTTP", "location": "USA"}

match d:
    case {"bandwidth": b, "latency": l, **rest}:
        print(f"Bandwidth: {b}, Latency: {l}, Other data: {rest}")

match d:
    case {"bandwidth": b, "latency": l, **rest}:
        print(f"Bandwidth: {b}, Latency: {l}, Other data: {rest}")

# case (Point x1, y1), Point(x2, y2) as p2

x = True
y = None
if x is True:
    print('true')
else:
    print('false')

if y is None:
    print("None")
else:
    print("Not None")

# Patterns may use named constants.
# These must be dotted names to prevent them from being interpreted as capture variable:

# from enum import Enum
# class Color(Enum):
#     RED = 'red'
#     GREEN = 'green'
#     BLUE = 'blue'
#
# color = Color(input("Enter your choice of 'red', 'blue', or 'green'"))
#
# match color:
#     case Color.RED:
#         print("I see red")
#     case Color.GREEN:
#         print("Nature is green")
#     case Color.BLUE:
#         print("The sky is blue!")
#     case _:
#         raise ValueError("Not a valid color!")

# Functions

def foo():
    a = 10 # local variable
    print(a)

foo()

x = 5

def bar():
    #x = 10
    global x
    x = 10
    print(x)

bar()
print(x)

print("------------------")
def outer():
    y = 5

    def inner():
        #y = 10
        nonlocal y
        y = 10
        print(y)

    inner()
    print(y)

outer()
print("------------------")

z = 20
def example_outer():
    w = 15

    def example_inner():
        nonlocal  w
        print(w)
        print(z)
        w = w + 1 # => UnboundLocalError: cannot access local variable 'w' where it is not associated with a value

    example_inner()
example_outer()

def foo():
    a = 10
    print(a)

f = foo
print(foo)
print(f)

print("-----------")
def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

def f2(a, L=None):
    if L is None:
        L = []

    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3))


def cheeseshop(kind, *args, **kwargs):
    print("-- Do you have any", kind, "?")
    print(f"-- We've run out of {kind}")
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(f"{kwarg}:{kwargs[kwarg]}")

cheeseshop("cheese",
           "potato",
           "pasta",
           shoekeeper="John",
           teacher="Bob")

# Positional-Only parameters: /

# This is useful for functions where you want to strictly enforce the order of arguments
# or when the parameters' names should be kept flexible, such as built-in functions and methods
# where the names might vary across implementations

# Parameters following the / may be positional-or-keyword or keyword-only.

def example_func(pos1, pos2, /):
    print(f"Positional 1: {pos1}, Positional 2: {pos2}")

example_func(2, 3) # -> this is ok!

# example_func(pos1=2, pos2=3) # -> TypeError: example_func() got some positional-only arguments passed as keyword arguments: 'pos1, pos2'

# Keyword-Only Parameters: *

# This is helpful when a function has many arguments, and you want to make the usage clearer,
# preventing potential mix-ups by requiring keywords.

def example_func2(*, kwarg1, kwarg2):
    print(f"Keyword 1: {kwarg1}, Keyword 2: {kwarg2}")

example_func2(kwarg1="mere", kwarg2="pere")

# example_func2("mere", "pere") # -> TypeError: example_func2() takes 0 positional arguments but 2 were given

# Combining Positional-Only and Keyword-Only parameters:
def combined_example(pos1, pos2, /, pos_or_kwarg, *, kwarg1, kwarg2=0):
    print(f"Positional 1: {pos1}, Positional 2: {pos2}, Mixed: {pos_or_kwarg}, Keyword 1: {kwarg1}, Keyword 2: {kwarg2}")

combined_example(1, 2, 3, kwarg1=4, kwarg2=5) # -> this works

combined_example(1, 2, pos_or_kwarg=3, kwarg1=4, kwarg2=5) # -> this works

def func1(name, **kwargs):
    return 'name' in kwargs # -> This will always be false since 'name' will be assigned to name and not to kwargs

# print(func1('Bogdan', **{"name": 'Ana'})) # -> TypeError func1() got multiple values for argument 'name'

def func2(name, /, **kwargs):
    return 'name' in kwargs

print(func2('Bogdan', **{'name': 'Ana'})) # -> Works because '/' allows name as positional argument and 'name' as key

# Use positional-only if you want the name of the parameters to not be available to the user.
# This is useful when parameter names have no real meaning, if you want to enforce the order
# of the arguments when the function is called or if you need to take some positional parameters
# and arbitrary keywords.

# Use keyword-only when names have meaning and the function definition is more understandable by being
# explicit with names or you want to prevent users relying on the position of the argument being passed.

# For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.

# Arbitrary Argument Lists

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

# Any formal parameters which occur after the *args parameter are ‘keyword-only’ arguments,
# meaning that they can only be used as keywords rather than positional arguments.

def concat(*args, sep='/'):
    return sep.join(args)

concat("earth", "mars", "venus")

concat("earth", "mars", "venus", sep=".")

# Unpacking Argument Lists
list(range(3, 6))

args = [3, 6]

list(range(*args))

def parrot(voltage, state="a stiff", action="voom"):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action" : "VOOM"}

parrot(**d)

# Lambda Expressions

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(30)
print(f(31))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

# Documentation strings

def my_func():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_func.__doc__)

# Function annotations
def func(ham: str, eggs: str = "Eggs") -> int:
    print("Annotations: ", func.__annotations__)
    print("Arguments", ham, eggs)
    return len(ham + eggs)

func("test")


