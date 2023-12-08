from scratch import Enemy

class Goblin(Enemy):
    def __init__(self, hp, attack, class_type, level = 1):
        super().__init__(hp, attack, level)
        self.type = "Goblin"
        self.class_type = class_type

    def goblin_info_dict(self):
        return {
            "hp": self.hp,
            "attack": self.attack,
            "level": self.level,
            "type": self.type,
            "class_type": self.class_type
        }
goblin = Goblin(20, 10, "Rogue", 10)
goblin_2 = Goblin(20, 10, "Rogue")

# print(goblin.creature_stats_dict())
print(goblin.goblin_info_dict())
# print(goblin.creature_stats_dict())
print(goblin_2.goblin_info_dict())
# print(isinstance(goblin, Enemy))
# print(isinstance(goblin, Goblin))
