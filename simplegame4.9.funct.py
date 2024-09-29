class Enemy:
    def __init__(self, name):
        self.name = name
        self.life = 3

    def attack(self):
        self.life -= 1

    def check_life(self):

        return self.life


enemy1 = Enemy("enemy_1")
enemy2 = Enemy("enemy_2")
enemy3 = Enemy("enemy_3")


def enemy_fight(enemy):  # return the enemy's lives count

    enemy.attack()
    enemy_life = enemy.check_life()
    if enemy.life >= 1:
        print("ouch")
        print(f"{enemy_life} {enemy.name} life(s) left\n")
    if enemy.life < 1:
        print("ouch")
        print(f"{enemy_life} {enemy.name} life(s) left")
        enemy.life = 0
        print(f"The {enemy.name} is defeated\n")
    return enemy_life

while True:
    enemylist = [enemy1, enemy2, enemy3]
    for enemy in enemylist:
        enemylives = enemy_fight(enemy)
        if enemy == enemy1:
            enemy1lives = enemylives
        elif enemy == enemy2:
            enemy2lives = enemylives
        elif enemy == enemy3:
            enemy3lives = enemylives

    if (enemy1lives, enemy2lives, enemy3lives) == (0, 0, 0):
        print("All three enemies are defeated, game is over")
        break
