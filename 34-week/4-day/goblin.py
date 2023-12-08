from scratch import Enemy


class Goblin(Enemy):
    def __init__(self, hp, attack, class_type, level = 1):
        super().__init__(hp, attack, level)
        self.type = "Goblin"
        self.class_type = class_type

    def goblin_stats(self):
        return {
            "hp": self.hp,
            "attack": self.attack,
            "level": self.level,
            "type": self.type,
            "class_type": self.class_type
        }

goblin = Goblin(5,3, "Rogue",99)
goblin_2 = Goblin(5,3, "Warrior")

# print(goblin.goblin_stats())
# print(goblin_2.goblin_stats())
print(goblin.goblin_stats())
print(goblin_2.goblin_stats())
