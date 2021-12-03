class Pokemon:
    types = ['fire', 'grass', 'water']
    counter = 0
    exp_rate = 1
    win = 0
    lose = 0
    PLUS = 1.5

    def __init__(self, name, type_p, hp):
        if type_p not in self.types:
            raise ValueError("%s is not a valid type." % type_p)
        self.type_p = type_p
        self.name = name
        self.hp = hp
        self.attacks = []
        Pokemon.counter += 1

    @classmethod
    def set_exp_rate(cls, exp_rate):
        cls.exp_rate = exp_rate

    @classmethod
    def win_lose(cls, key):
        if key == 'win':
            cls.win += 1
        if key == 'lose':
            cls.lose += 1

    def get_hp(self):
        return self.hp

    def learn_attack(self, attack):
        if attack not in self.attacks:
            self.attacks.append(attack)

    def attack(self, type_attack):
        attack = None
        for a in self.attacks:
            if a.type_a == type_attack.lower():
                attack = a
        return attack

    def receive_damage(self, attack):

        damage = float(attack.damage)
        if attack.type_a == "fire" and self.type_p == "grass":
            damage *= Pokemon.PLUS
        if attack.type_a == "grass" and self.type_p == " water":
            damage *= Pokemon.PLUS
        if attack.type_a == "water" and self.type_p == "fire":
            damage *= Pokemon.PLUS
        remains_hp = float(self.hp) - damage

        self.hp = remains_hp if float(damage) > 0 else 0

        return damage

    def __repr__(self):
        return "name:% s type_p:% s hp:% s win:%s lose:%s attacks:% s " % (
            self.name, self.type_p, self.hp, self.win, self.lose, self.attacks)

    def __str__(self):
        return "Pokemon: named %s type %s life points %s WIN : %s LOSE: %s" % (
            self.name, self.type_p, self.hp, self.win, self.lose)


class Attack:
    def __init__(self, name, type_a, damage):
        self.name = name
        self.type_a = type_a
        self.damage = damage

    def get_damage(self):
        return self.damage

    def get_type_a(self):
        return self.type_a

    def __repr__(self):
        return "name:% s type_a:% s damage:% s" % (self.name, self.type_a, self.damage)

    def __str__(self):
        return "Attack info: name %s type attack %s damage %s" % (self.name, self.type_a, self.damage)

    def __eq__(self, other):
        if not isinstance(other, Attack):
            return NotImplemented
        return self.name == other.name
