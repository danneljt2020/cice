from pokemon import Pokemon, Attack

attack1 = Attack('nombre_ataque1', 'water', '500')
attack2 = Attack('atak 2', 'fire', '300')

p1 = Pokemon("Pikashu", 'fire', '300')
p1.receive_damage('200')
p1.receive_damage('22')

p1.learn_attack(attack1)
p1.learn_attack(attack2)


print({p1})  # call __repr__ return a list or dict

print({p1.attacks[0].damage}) #acces to object data


# print(p1)  # call __str__
# print(p1.attacks)
