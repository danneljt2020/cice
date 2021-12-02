from pokemon import Pokemon, Attack

pikashu = Pokemon("Pikashu", 'fire', '1000')
vancur = Pokemon("Vancur", 'water', '1000')

# attacks pikashu
attack1 = Attack('atak 1', 'water', '300')
attack2 = Attack('atak 2', 'fire', '200')

# attacks vancur
attack3 = Attack('atak 3', 'fire', '300')
attack4 = Attack('atak 4', 'water', '300')

pikashu.learn_attack(attack1)
pikashu.learn_attack(attack2)

vancur.learn_attack(attack3)
vancur.learn_attack(attack4)

# pikasu attack a vancur
vancur.receive_damage(pikashu.attack('fire'))

# vancur attack pikasu
pikashu.receive_damage(vancur.attack('water'))

print(pikashu)
print(vancur)


# test attack

# print({p1})  # call __repr__ return a list or dict

# print({p1.attacks[0].damage}) #acces to object data
