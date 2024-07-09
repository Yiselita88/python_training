# # LinkedIn Learning Python course by Joe Marini

# def main():
#    print("Hello World")
#    name = input("What's your name?")
#   print("Nice meeting you", name)

# if __name__ == "__main__":
#    main()


# def func1():
#     print("I am a function")


# def func2(arg1, arg2):
#     print(arg1, " ", arg2)


# def cube(x):
#     return x ** 3


# def power(num, x=1):
#     result = 1
#     for i in range(x):
#         result = result * num
#     return result


# func1()
# print(func1())
# print(func1)

# func2(10, 20)
# print(func2(10, 20))
# print(cube(3))

# print(power(2))
# print(power(2, 3))
# print(power(num=2, x=3))


# def multi_add(*args):
#     result = 0
#     for x in args:
#         result = result + x
#     return result


# print(multi_add(4, 5, 10, 4))

# # conditional statements


# def main():
#     x, y = 100, 100

#     # conditional flow uses if, elif, else
#     if x < y:
#         result = "x values is less than y value"
#     elif x == y:
#         result = "x and y are equals"
#     else:
#         result = "x is greater than y"

#     print(result)

#     result = "x is less than y" if x < y else "x is greater or equal to y"
#     print(result)


# if __name__ == "__main__":
#     main()

# def main():
#     x = 0

# # while loop
# while (x < 5):
#     print(x)
#     x += 1

# # for loops
# for x in range(5, 10):
#     print(x)

# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# for d in days:
#     if d == "Wed":
#         break
#     print(d)

#     for x in range(5, 10):
#         if x == 7:
#             break
#         print(x)

#     for t in range(15, 30):
#         if t % 2 == 0:
#             continue
#         print(t)

#     days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#     for i, d in enumerate(days):
#         print(i, d)


# if __name__ == "__main__":
#     main()


# CLASSES
class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed


class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed)


class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "motorcycle at", self.speed)


car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)

print(mc1.wheels)
print(car1.enginetype)
print(car2.doors)


car1.drive(30)
car2.drive(40)
mc1.drive(50)


# modules in python
import math as math
print("the square root of 16 is", math.sqrt(16))
print("Pi value is", math.pi)

x = 10 / 0
try:
    x = 10/0
except:
    print("Well that didn't work!")

try:
    answer = input("What should I divide 10 by?")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("You can't divide by zero!")
except ValueError as e:
    print("You didn't give me a valid number!")
    print(e)
finally:
    print("This code always runs")
