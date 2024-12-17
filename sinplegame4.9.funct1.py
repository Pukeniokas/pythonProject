class Enemy:
    def __init__(self, name):
        self.name = name
        self.life = 3

    def attack(self):
        self.life -= 1

    def check_life(self):
        return self.life


class Strongenemy(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.life = 5

    def superattack(self):
        self.life -= 2

    def attackback(self):

        self.life += 2


enemy1 = Enemy("enemy_1")
enemy2 = Enemy("enemy_2")
enemy3 = Enemy("enemy_3")

strongenemy1 = Strongenemy("strongenemy_1")
strongenemy2 = Strongenemy("strongenemy_2")

enemy1lives = None
enemy2lives = None
enemy3lives = None
strongenemy1lives = None
strongenemy2lives = None


def enemy_fight(enemy):  # return the enemy's lives count or "no attack"
    if enemy.life == 0:
        return enemy.life

    playerschois = input(f"\nif you want attack {enemy.name} type A"
                         " if no attack type N or anything else > ")
    if playerschois == "A":
        print(f"{enemy.name} was attacked")
        enemy.attack()

    else:
        print(f"The same {enemy.life} {enemy.name} life(s) left\n")
        return "no_attack"

    if enemy.life >= 1:
        print("ouch")
        print(f"{enemy.life} {enemy.name} life(s) left\n")
    if enemy.life < 1:
        print("ouch")
        enemy.life = 0
        print(f"{enemy.life} {enemy.name} life(s) left")

    return enemy.life


def strongenemy_fight(enemy):  # return the strongenemy's lives count or " no_attack"
    if enemy.life == 0:
        return enemy.life

    playerschois = input(f"if you want attack {enemy.name} type A"
                         " if double attack type DA, if no attack "
                         "type N or anything else > ")
    print()
    if playerschois == "A":
        enemy.attack()
        print(f"{enemy.name} was attacked")
    elif playerschois == "DA":
        enemy.superattack()
        print(f"{enemy.name} was double  attacked")
    else:
        print(f"The same {enemy.life} {enemy.name} life(s) left\n")
        return "no_attack"

    if enemy.life > 1:
        print("ouch")
        print(f"{enemy.life} {enemy.name} life(s) left\n")
    if enemy.life == 1:
        print(" ch, ch, ch")
        enemy.attackback()
        if playerschois == "A":
            takenlives = 1
            print(f"You take from me {takenlives} life,but afterwards I got 2 new lives")
        elif playerschois == "DA":
            takenlives = 2
            print(f"You take from my {takenlives} life,but afterwards I got 2 new lives")
        print(f"{enemy.life} {enemy.name} life(s) left\n")

    if enemy.life < 1:
        print("ouch")
        enemy.life = 0

        print(f"{enemy.life} {enemy.name} life(s) left")

    return enemy.life


while True:

    if (enemy1lives, enemy2lives, enemy3lives, strongenemy1lives, strongenemy2lives) == (0, 0, 0, 0, 0):
        print("All five enemies are defeated, game is over")
        break
    enemylist = [enemy1, enemy2, enemy3,  strongenemy1, strongenemy2]
    for enemy in enemylist[0:3]:
        enemylives = enemy_fight(enemy)
        if enemylives == 0:
            print(f"The {enemy.name} is defeated\n")
            if enemy == enemy1:
                enemy1lives = enemylives
            elif enemy == enemy2:
                enemy2lives = enemylives
            elif enemy == enemy3:
                enemy3lives = enemylives
            continue

        if enemylives == "no_attack":
            continue

    for enemy in enemylist[3:]:

        enemylives = strongenemy_fight(enemy)
        if enemylives == 0:
            print(f"The {enemy.name} is defeated\n")
            if enemy == strongenemy1:
                strongenemy1lives = enemylives
            elif enemy == strongenemy2:
                strongenemy2lives = enemylives
            continue
        if enemylives == "no_attack":
            continue
