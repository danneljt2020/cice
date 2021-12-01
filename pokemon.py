class Pokemon:
    types = ['fire', 'grass', 'water']

    def __init__(self, name, type_p, hp):
        if type_p not in self.types:
            raise ValueError("%s is not a valid type." % type_p)
        self.type_p = type_p
        self.name = name
        self.hp = hp
        self.attacks = []

    def learn_attack(self, attack):
        self.attacks.append(attack)

    def attack(self, type_attack):
        return self.attacks[type_attack]

    def receive_damage(self, damage):
        self.hp = float(self.hp)-float(damage)
        return self.hp

    def add_attacks(self, attack):
        self.attacks.append(attack)

    def __repr__(self):
        return "name:% s type_p:% s hp:% s attacks:% s" % (self.name, self.type_p,  self.hp, self.attacks)

    def __str__(self):
        return "Hi i am pokemon: named %s type %s life points %s" % (self.name, self.type_p, self.hp)


class Attack:
    def __init__(self, name, type_a, damage):
        self.name = name
        self.type_a = type_a
        self.damage = damage

    def __repr__(self):
        return "name:% s type_a:% s damage:% s" % (self.name, self.type_a,  self.damage)

    def __str__(self):
        return "Attack info: name %s type attack %s damage %s" % (self.name, self.type_a, self.damage)

