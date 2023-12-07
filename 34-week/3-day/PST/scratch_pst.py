print("hello from scratch_pst")
from helpers import num_printer
class Player:
    player_count = 0

    def __init__(self, name, class_type, level = 1):
        self.name = name
        self.class_type = class_type
        self.level = level
        # Player.player_count += 1
        Player.increase_player_count()

    def level_up(self):
        self.level += 1

    @classmethod
    def increase_player_count(cls):
        cls.player_count += 1

    @staticmethod
    def player_info():
        return "A players minimum level is 1 and the max is 99"

    @property
    def get_level(self):
        return self.level

    @get_level.setter
    def set_level(self, level):
        if level < 100:
            self.level = level
        else:
            return "You are at the max level"

# print(Player.player_count)
# jesse = Player("Jesse", "Wizard")
# jesse.player_count += 1
# print(jesse.player_count)
# print("jesse instance player count:", jesse.player_count)
# print("Player class player count:", Player.player_count)
# print(jesse)
# print(jesse.name)
# print(jesse.level)
# jesse.level_up(99)
# print(jesse.level)
# Player.increase_player_count()
# print(Player.player_count)

# print(jesse.get_level)
# jesse.set_level = 99
# print(jesse.get_level)

# decorators

from datetime import datetime

# our decorator, which takes in a callback function
def timer(func):

    # define the wrapper function that we're going to return
    def wrapper(*args, **kwargs):
        # get current time before function call
        before_time = datetime.now()

        # invoke the callback
        val = func(*args, **kwargs)
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
# def say_hello():
#     return "hello"

# print(say_hello())

# @timer
# def sum_printer(num_1, num_2):
#     return num_1 + num_2

# print(sum_printer(4,8))

# @timer
# def name_printer(name):
#     return f"Hello {name}!"

# print(name_printer("Jacob"))
