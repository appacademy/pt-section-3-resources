from creature import Creature
# from creature import Creature as c
# import creature
# print(creature)
test = "hello".isLower()
print("in enemies")
class Dragon(Creature):
    def __init__(self, name, level, wing_span):
        super().__init__(name, level)
        self.wing_span = wing_span

    def speak(self):
        return f"{self.name} roars loudly!"

    def attack(self):
        return f"{self.name} breathes fire!"

    def __str__(self):
        return f"< {self.name} is a Level {self.level} Dragon with a {self.wing_span}m wingspan >"

my_drag = Dragon("will", 100, 50)
print("end of file", my_drag)
