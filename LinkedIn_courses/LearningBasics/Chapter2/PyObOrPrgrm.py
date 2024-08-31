# # # # Inheritance
# # # Example of repeated attributes in several classes
# # class Book:
# #     """docstring for  Book"""

# #     def __init__(self, title, author, pages, price):
# #         self.title = title
# #         self.author = author
# #         self.pages = pages
# #         self.price = price


# # class Magazine:
# #     def __init__(self, title, publisher, price, period):
# #         self.title = title
# #         self.publisher = publisher
# #         self.price = price
# #         self.period = period


# # class Newspaper:
# #     def __init__(self, title, publisher, price, period):
# #         self.title = title
# #         self.publisher = publisher
# #         self.price = price
# #         self.period = period

# # declare a new class with common attributes:


# class Publication:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price


# class Periodical(Publication):
#     def __init__(self, title, price, period, publisher):
#         super().__init__(title, price)
#         self.period = period
#         self.publisher = publisher


# # then the previous classes with repeated attributes can be written as:

# class Book(Publication):
#     def __init__(self, title, author, pages, price):
#         super().__init__(title, price)
#         self.author = author
#         self.pages = pages


# class Magazine(Periodical):
#     def __init__(self, title, publisher, price, period):
#         super().__init__(title, price, period, publisher)


# class Newspaper(Periodical):
#     def __init__(self, title, publisher, price, period):
#         super().__init__(title, price, period, publisher)


# # creating the object
# b1 = Book("Brave New World", "Aldous", 311, 29.0)
# print(b1.author)
# print(b1.price)

# # printing object
# n1 = Newspaper("NY times", "NY times Inc", 6.0, "Daily")
# print(n1.period, n1.publisher)

# m1 = Magazine("Scientific American", "nature", period="montly", price=5.99)
# print(m1.price)

# print('-------------------ABSTRACT BASE CLASSES---------------------')
# # # ABSTRACT BASE CLASSES

# from abc import ABC, abstractmethod


# class GraphicShape(ABC):
#     def __init__(self):
#         super().__init__()

#     @abstractmethod
#     def calcArea(self):
#         pass


# class Circle(GraphicShape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calcArea(self):
#         return 3.14 * (self.radius ** 2)


# class Square(GraphicShape):
#     def __init__(self, side):
#         self.side = side

#     def calcArea(self):
#         return self.side * self.side


# # g = GraphicShape()


# c = Circle(10)

# print(c.calcArea())
# s = Square(12)
# print(s.calcArea())

# print('--------Multiple Inheritance CLASSES----------------')


# class A:
#     def __init__(self):
#         super().__init__()
#         self.prop1 = "prop1"
#         self.name = "Class A"


# class B:
#     def __init__(self):
#         super().__init__()
#         self.prop2 = "prop2"
#         self.name = "Class B"


# class C(B, A):
#     """the order of the classes B & A, will define the property (attribute) "name" that is gonna be printed first"""

#     def __init__(self):
#         super().__init__()

#     def showprops(self):
#         print(self.prop1)
#         print(self.prop2)
#         print(self.name)


# c = C()
# print(C.__mro__)  # this indicates the method resolution order
# c.showprops()


# print('---------------Feature called "Interfaces"--------------------')
# from abc import ABC, abstractmethod


# class GraphicShape(ABC):
#     def __init__(self):
#         super().__init__()

#     @abstractmethod
#     def calcArea(self):
#         pass


# class JSONify(ABC):
#     @abstractmethod
#     def toJSON(self):
#         pass


# class Circle(GraphicShape, JSONify):
#     def __init__(self, radius):
#         self.radius = radius

#     def calcArea(self):
#         return 3.14 * (self.radius ** 2)

#     def toJSON(self):
#         return f"{{\'Circle\': {str(self.calcArea())}}}"


# c = Circle(10)
# print(c.calcArea())
# print(c.toJSON())

# print('-----------------Understanding composition----------------')


# class Book:
#     # def __init__(self, title, price, authorfname, authorlname):
#     def __init__(self, title, price, author=None):
#         self.title = title
#         self.price = price

#         # self.authorfname = authorfname
#         # self.authorlname = authorlname
#         self.author = author

#         self.chapters = []

#     # def addchapter(self, name, pages):
#         # self.chapters.append((name, pages))
#     def addchapter(self, chapter):
#         self.chapters.append((chapter))

#     def getbookpagecount(self):
#         result = 0
#         for ch in self.chapters:
#             result += ch.pagecount
#         return result


# class Author:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def __str__(self):
#         return f"{self.fname} {self.lname}"


# class Chapter:
#     def __init__(self, name, pagecount):
#         self.name = name
#         self.pagecount = pagecount


# auth = Author("Leo", "Tolstoy")

# # b1 = Book("War & Peace", 39.0, "Leo", "Tolstoy")

# b1 = Book("War & Peace", 39.0, auth)

# # b1.addchapter("Chapter 1", 125)
# # b1.addchapter("Chapter 2", 97)
# # b1.addchapter("Chapter 3", 143)

# b1.addchapter(Chapter("Chapter 1", 125))
# b1.addchapter(Chapter("Chapter 2", 97))
# b1.addchapter(Chapter("Chapter 3", 143))


# print(b1.title)
# print(b1.author)
# print(b1.getbookpagecount())


print("------------magic methods--------------")
# print("---------String representation---------")


# class Book:
#     def __init__(self, title, author, price):
#         super().__init__()
#         self.title = title
#         self.author = author
#         self.price = price

#     def __str__(self):
#         return f"{self.title} by {self.author}, costs {self.price}"

#     def __repr__(self):
#         return f"title={self.title}, author={self.author}, price={self.price}"


# b1 = Book("War & Peace", "Leo Tolstoy", 39.95)
# b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# print(b1)
# print(b2)
# print(str(b1))
# print(repr(b2))

# print("----------Equality & Comparison----------")


# class Book:
#     def __init__(self, title, author, price):
#         super().__init__()
#         self.title = title
#         self.author = author
#         self.price = price

#     def __eq__(self, value):
#         if not isinstance(value, Book):
#             raise ValueError("Cannot compare book to a non-book")
#         return (self.title == value.title and self.author == value.author and self.price == value.price)

#     def __ge__(self, value):
#         if not isinstance(value, Book):
#             raise ValueError("Cannot compare book to a non-book")
#         return self.price >= value.price

#     def __lt__(self, value):
#         if not isinstance(value, Book):
#             raise ValueError("Cannot compare book to a non-book")
#         return self.price < value.price


# b1 = Book("War & Peace", "Leo Tolstoy", 39.95)
# b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
# b3 = Book("to kill a mockingbird", " harper lee", 24.95)
# b4 = Book("War & Peace", "Leo Tolstoy", 39.95)

# print(b1 == b4)
# print(b1 == b2)
# # print(b1 == 42)

# print(b2 >= b1)
# print(b2 < b1)

# books = [b1, b3, b2, b4]
# books.sort()

# print([book.title for book in books])

# print("---------Attribute access-------------")


# class Book:
#     def __init__(self, title, author, price):
#         super().__init__()
#         self.title = title
#         self.author = author
#         self.price = price
#         self._discount = 0.1

#     def __str__(self):
#         return f"{self.title} by {self.author}, costs {self.price}"

#     def __getattribute__(self, name):
#         if name == "price":
#             p = super().__getattribute__("price")
#             d = super().__getattribute__("_discount")
#             return p - (p * d)
#         return super().__getattribute__(name)

#     def __setattr__(self, name, value):
#         if name == "price":
#             if type(value) is not float:
#                 raise ValueError("The 'price' attr must be a float")
#         return super().__setattr__(name, value)

#     def __getattr__(self, name):
#         return name + " is not here!"


# b1 = Book("War & Peace", "Leo Tolstoy", 39.95)
# b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# #b1.price = float(40)
# print(b1.randomprop)


# print("-------callable objects-----------")


# class Book:
#     def __init__(self, title, author, price):
#         super().__init__()
#         self.title = title
#         self.author = author
#         self.price = price
#         self._discount = 0.1

#     def __str__(self):
#         return f"{self.title} by {self.author}, costs {self.price}"

#     def __call__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price


# b1 = Book("War & Peace", "Leo Tolstoy", 39.95)
# b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# print(b1)
# b1("Anna Karenina", "Leo Tolstoy", 49.95)
# print(b1)


# DATA CLASSES
print("---------DATA CLASSES---------")
# print("---------defining a data class----------")


# from dataclasses import dataclass


# @dataclass
# class Book:
#     title: str
#     author: str
#     pages: int
#     price: float
#     # def __init__(self, title, author, price):
#     #     super().__init__()
#     #     self.title = title
#     #     self.author = author
#     #     self.price = price

#     def bookinfo(self):
#         return f"{self.title}, by {self.author}"


# b1 = Book("War & Peace", "Leo Tolstoy", 1225, 39.95)
# b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
# b3 = Book("War & Peace", "Leo Tolstoy", 1225, 39.95)


# print(b1.title)
# print(b2.author)
# print(b1)

# print(b1 == b3)
# print(b1 == b2)

# b1.title = "Anna Karenina"
# b1.pages = 864
# print(b1.bookinfo())

# print("--------post initialization---------")

# from dataclasses import dataclass


# @dataclass
# class Book:
#     title: str
#     author: str
#     pages: int
#     price: float

#     def __post_init__(self):
#         self.description = f"{self.title} by {self.author}, {self.pages} pages"


# b1 = Book("War & Peace", "Leo Tolstoy", 1225, 39.95)
# b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
# # b3 = Book("War & Peace", "Leo Tolstoy", 1225, 39.95)

# print(b1.description)
# print(b2.description)

print("----------using default values------------")

from dataclasses import dataclass, field
import random


def price_func():
    return float(random.randrange(20, 40))


@dataclass
class Book:
    title: str = "No title"
    author: str = "no author"
    pages: int = 0
    # price: float = field(default=10.0)
    price: float = field(default_factory=price_func)

    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"


b1 = Book()
print(b1)

b2 = Book("War & Peace", "Leo Tolstoy", 1225)
b3 = Book("The Catcher in the Rye", "JD Salinger", 234)
# b3 = Book("War & Peace", "Leo Tolstoy", 1225, 39.95)

print(b2)
print(b3)


# print("--------Immutable dataclass-----------")

# from dataclasses import dataclass


# @dataclass(frozen=True)
# class ImmutableClass:
#     value1: str = "Value 1"
#     value2: int = 0

#     def some_func(self, newval):
#         self.value2 = newval


# obj = ImmutableClass()

# obj = ImmutableClass("Another string", 20)

# print(obj.value1, obj.value2)


# obj.value1 = "Another SAtring"
# print(obj.value1)

# obj.some_func(20)
