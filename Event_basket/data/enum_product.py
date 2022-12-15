import enum


class Category(enum.Enum):
    other = 0
    meat = 1
    fish = 2
    vegetables_fruits = 3
    grocery = 4
    milk_dairy_eggs = 5
    drinks = 6
    desserts = 7
    spices = 8


class TypeOfPackaging(enum.Enum):
    other = 0
    kg = 1
    piece = 2
