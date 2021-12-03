from pokemon import Pokemon, Attack
import random

pikashu = Pokemon("Pikashu", 'fire', '1000')
vancur = Pokemon("Vancur", 'water', '1000')

# attacks pikashu
attack1 = Attack('attack 1', 'water', '100')
attack2 = Attack('attack 2', 'fire', '200')
attack3 = Attack('attack 3', 'fire', '300')

# attacks vancur
attack4 = Attack('attack 4', 'water', '200')
attack5 = Attack('attack 5', 'fire', '10')
attack6 = Attack('attack 6', 'fire', '20')

pikashu.learn_attack(attack1)
pikashu.learn_attack(attack2)
pikashu.learn_attack(attack3)

vancur.learn_attack(attack4)
vancur.learn_attack(attack5)
vancur.learn_attack(attack6)

user = "r"
menu = ['1', '2', '3', 'Q', 'q']


while user.lower() != "q":
    print("POKEMON".center(50, "-"))
    print("1. Crear Pokemon")
    print("2. Aprender ataque")
    print("3. Atacar!!")
    print("Presione la letra Q para terminar de la batalla")
    option_menu = input(":")

    if option_menu in menu:
        if option_menu == "3":
            while int(vancur.hp) > 0 and int(pikashu.hp) > 0:
                print(vancur.name + " HP:" + str(vancur.hp))
                print(pikashu.name + " HP:" + str(pikashu.hp))

                print('Selecciona el ataque:')
                for k, attack in enumerate(pikashu.attacks):
                    print(str(k + 1) + "-->" + attack.name + " with damage:" + str(attack.damage))

                select_attack = input(":")

                selected_attack = pikashu.attacks[int(select_attack) - 1]
                vancur.receive_damage(selected_attack)

                # random attack from PC Pokemon
                random_attack = random.choice(vancur.attacks)

                pikashu.receive_damage(random_attack)

                print(pikashu.name + " Received " + random_attack.damage + " Remaining life " + str(pikashu.hp))
                print(vancur.name + " Received " + selected_attack.damage + " Remaining life " + str(vancur.hp))

            print("*".center(50, "-"))

            if vancur.hp > pikashu.hp:
                print(vancur.name + " has has WIN!!!")
                print(pikashu.name + " has LOST , is dead!!!")
            else:
                print(pikashu.name + " has has WIN!!!")
                print(vancur.name + " has LOST , is dead!!!")

            print("*".center(50, "-"))
    else:
        print("Ha seleccionado una Opcion no valida!")

# print(pikashu)
# print(vancur)


# test attack

# print({p1})  # call __repr__ return a list or dict

# print({p1.attacks[0].damage}) #acces to object data
