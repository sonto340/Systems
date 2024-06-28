from char import stats
from enemies import current_enemy
#
#
#
hit = False
print(f'''
      You encounter {current_enemy["name"]})!)
      What will you do?''')
while current_enemy["hp"] > 0:
        command = input('''
                >(F)ight
                >(I)tem
                >(R)un
                >'''
                )
        if command is "F" or "f":
            if current_enemy["acc"] < stats["acc"]:
                hit = True
                if hit == True:
                    damage = (current_enemy["hp"] - (stats["atk"]-current_enemy["def"]))
                    print(f"A hit! You did {damage} damage!")
                    current_enemy["hp"] -= damage
                    if current_enemy["hp"] == 0:
                         print("YOU WIN")
                else:
                    print("Oh no! You missed!")
        elif command is "I" or "i":
             print("I have no idea how to program that yet!")
             break
        elif command is "R" or "r":
             print("You ran away!")
else:
    print("battle won!")


