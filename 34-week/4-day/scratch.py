class Enemy:
    def __init__(self, hp, attack, level = 1):
        self.hp = hp
        self.attack = attack
        self.level = level

    def enemy_stats(self):
        return {
            "hp": self.hp,
            "attack": self.attack,
            "level": self.level
        }


new_enemy = Enemy(5, 3)

# print(new_enemy)
# print(new_enemy.enemy_stats())
