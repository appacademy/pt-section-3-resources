# Classes

# Creating a class
class Player:
    # class variables
    player_count = 0

    # class constructor
    def __init__(self, name, class_type, level = 1):
        # instance variables
        self.name = name
        self.class_type = class_type
        self.level = level
        # Player.player_count += 1
        Player.increase_player_count()

    # instance methods
    def level_up(self):
        if self.level < 100:
            self.level += 1
            return f"You have leveled up! Your new level is {self.level}"
        else:
            return f"You are at the maximum level!"

    # getters
    @property
    def my_level(self):
        return self.level

    # setters
    @my_level.setter
    def increase_level(self, level):
        if self.level < 100:
            self.level = level
        else:
            return f"You are at the maximum level!"

    # class methods
    @classmethod
    def increase_player_count(cls):
        # Player.player_count += 1
        cls.player_count += 1

    # static methods
    @staticmethod
    def player_info():
        return f"A players minimum level is 1 and the max level is 99"




# print(Player.player_count)
jesse = Player("Jesse", class_type="Wizard")
# jesse = Player("Chris", class_type="Barbarian")
# print(jesse)
jesse.increase_level = 20
# print(jesse.level)
# print(jesse.my_level)
# print(jesse.name)
# print(jesse.class_type)
# print(jesse.level)
# jesse.level_up()
# print(jesse.level)

# print(Player.player_count)
# Player.player_count += 1

# jesse.player_count += 1
# print(jesse.player_count)
# print(Player.player_count)


# decorators

from datetime import datetime

# our decorator, which takes in a callback function
def timer(func):

    # define the wrapper function that we're going to return
    def wrapper(num_1, num_2):
        # get current time before function call
        before_time = datetime.now()

        # invoke the callback
        val = func(num_1, num_2)
        # log the return value of the function
        print(val)

        # get current time after function call
        after_time = datetime.now()

        # calculate total time
        total = after_time - before_time

        # return the total time
        return total

    # decorator returns the wrapper function object
    return wrapper

# @timer
# def my_function():
#     return "Hello World"

# print(my_function())

# @timer
# def name_printer(name):
#     return name

# print(name_printer("Jesse"))

# @timer
# def num_adder(num1, num2):
#     return num1 + num2

# print(num_adder(10,15))


# imports
# from helpers import multiply_by_2

# print(multiply_by_2(5))

import random

print(random.randint(0, 10))
