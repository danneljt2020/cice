from pokemon import Pokemon, Attack
import random
from os import system

pikashu = Pokemon("Pikashu", 'fire', '1000')
vancur = Pokemon("Vancur", 'water', '1000')

# attacks pikashu
attack1 = Attack('Brave Bird', 'water', '100')
attack2 = Attack('Techno Blast', 'grass', '200')
attack3 = Attack('Iron Tail', 'fire', '300')

# attacks vancur
attack4 = Attack('Waterfall', 'water', '10')
attack5 = Attack('Smack Down', 'fire', '10')
attack6 = Attack('Razor Leaf', 'water', '100')

pikashu.learn_attack(attack1)
pikashu.learn_attack(attack2)
pikashu.learn_attack(attack3)

vancur.learn_attack(attack4)
vancur.learn_attack(attack5)
vancur.learn_attack(attack6)


def battle(poke, pc):
    POKE_1 = poke.hp
    POKE_2 = pc.hp

    while int(pc.hp) > 0 and int(poke.hp) > 0:
        print(pc.name + " HP:" + str(pc.hp) + "/" + str(POKE_2))
        print(poke.name + " HP:" + str(poke.hp) + "/" + str(POKE_1))

        print('Selecciona el ataque:')
        for k, attack in enumerate(poke.attacks):
            print(str(k + 1) + "-->" + attack.name + " with damage:" + str(attack.damage))

        select_attack = input(":")

        selected_attack = poke.attacks[int(select_attack) - 1]

        # random attack from PC Pokemon
        random_attack = random.choice(pc.attacks)

        v_damage = pc.receive_damage(selected_attack)
        p_damage = poke.receive_damage(random_attack)

        print(poke.name + " Received " + str(p_damage) + " Remaining life " + str(poke.hp))
        print(pc.name + " Received " + str(v_damage) + " Remaining life " + str(pc.hp))

    if poke.hp > pc.hp:
        win = poke
        poke.win_lose('win')
        pc.win_lose('lose')
    else:
        win = pc
        pc.win_lose('win')
        poke.win_lose('lose')

    return win


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
            POKE_1 = pikashu.hp
            POKE_2 = vancur.hp
            win = battle(pikashu, vancur)

            print("*".center(50, "-"))

            print(win.name + " has WIN!!!")

            print(win)

            print("*".center(50, "-"))
    else:
        print("Ha seleccionado una Opcion no valida!")


# print({p1})  # call __repr__ return a list or dict

