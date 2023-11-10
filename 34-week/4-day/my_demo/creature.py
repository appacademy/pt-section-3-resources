print("at the top of creatures")
class Creature:
    def __init__(self, name, level):
        print("here")
        self.name = name
        self.level = level
    def __repr__(self):
        return f"{self.content}"


    def speak(self):
        return f"{self.name} makes a generic sound."

    def attack(self):
        return f"{self.name} attacks with a basic move."

    # def __repr__(self):
    #     return f"{self.name}, {self.age}, {self.email}"

# def my_func():
#     return "hi"

# some_variable = my_func()

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
