import random


class Pokemon(object):
    def __init__(self, name, health, high_attack_power, low_attack_power):
        self.name = name
        self.health = health
        self.high_attack_power = high_attack_power
        self.low_attack_power = low_attack_power

    def attack(self):
        return random.randint(self.low_attack_power, self.high_attack_power)

    def defend(self, enemy, attack_power):
        self.health -= attack_power

    def growl(self):
        print('Growl')


class WaterType(Pokemon):
    def growl(self):
        print('Glub Glub')

    def defend(self, enemy, attack_power):
        if isinstance(enemy, FireType):
            print('Yikes, not yet')
            attack_power /= 2
            self.health -= attack_power
        elif isinstance(enemy, GrassType):
            print('Hella Damage!!')
            attack_power *= 2
            self.health -= attack_power
        print(self.name + ' defended against ' + enemy.name + '. ' + 'The  attack power: ' + str(attack_power)
              + " health: " + str(self.health))


class FireType(Pokemon):
    def growl(self):
        print('RAWR XD')

    def defend(self, enemy, attack_power):
        if isinstance(enemy, WaterType):
            print('RAWrum!!')
            attack_power *= 2
            self.health -= attack_power
        elif isinstance(enemy, GrassType):
            print('Gotta try harder!!!')
            attack_power /= 2
            self.health -= attack_power
        print(self.name + ' defended against ' + enemy.name + '. ' + 'The  attack power: ' + str(attack_power)
              + " health: " + str(self.health))


class GrassType(Pokemon):
    def growl(self):
        print('*Bush noise*')

    def defend(self, enemy, attack_power):
        print("ap: " + str(attack_power))
        print("health: " + str(self.health))
        if isinstance(enemy, WaterType):
            print('Defense broken')
            attack_power /= 2
            self.health -= attack_power
        elif isinstance(enemy, FireType):
            print('Defended')
            attack_power *= 2
            self.health -= attack_power
        print(self.name + ' defended against ' + enemy.name + '. ' + 'The  attack power: ' + str(attack_power)
              + " health: " + str(self.health))
        # self.name print('defended') self.name print(attack power)

# 1st gen and gen 3
bulb = GrassType('Bulbasaur', 80, 40, 10)
treec = GrassType('Treecko', 80, 50, 20)
squirt = WaterType('Squirle', 30, 60, 30)
mud = WaterType('Mudkip', 40, 60, 20)
charm = FireType('Charmander', 90, 50, 20)
torch = FireType('Torchic', 90, 60, 20)

# fred.defend(willma, willma.attack())
bulb.defend(treec, squirt.attack())
bulb.defend(treec, charm.attack())
bulb.defend(treec, treec.attack())

# Mikael checked code switched up the attack and then some :D
# Tried is and changed the character and the attack