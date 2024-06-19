print("Hello world!")

print('Hello world!')

print(42)

# create variables
# The user's score
score = 750
print(score)

# my favorite snack
favorite_snack = 'Cookies and Ice cream'
print(favorite_snack)

# booleans

if 7 < 6:
    print("Yes, 5 is less than 6")
else:
    print("No, we have a value greater than 6")

having_fun = "yes"

if (having_fun == "yes"):
    print("Glad you'r having fun")

# functions


def say_hello(name):
    print(f"Hello, {name}!")


say_hello('Yisel')
say_hello('Maya')

# classes


class Puppy():
    def __init__(self, name, favorite_toy):
        self.name = name
        self.favorite_toy = favorite_toy

    def play(self):
        print(self.name + "is playing with " + self.favorite_toy)


marble = Puppy('Marble', 'teddy bear')
marble.play()

onix = Puppy('Onyx', 'lizard')
onix.play()


# modules
import random

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)
print(numbers)

number = random.choice(numbers)
print(number)
