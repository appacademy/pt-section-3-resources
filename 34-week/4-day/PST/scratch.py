class Enemy:
    def __init__(self, hp, attack, level = 1):
        self.hp = hp
        self.attack = attack
        self.level = level

    def creature_stats_dict(self):
        return {
            "hp": self.hp,
            "attack": self.attack,
            "level": self.level
        }

new_creature = Enemy(9, 5, 10)

# print(new_creature)
# print(new_creature.creature_stats_dict())
