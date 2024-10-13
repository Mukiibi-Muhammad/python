name = input("Type your name: ")

print("Welcome", name, "to this adventure")

answer = input(
    "You are on a dirt road, it has coem to an endand you can go left or right: ").lower()

if answer == "left":
    answer = input(
        "You come to a river, you camn walk arounf it or swim around? Type walk/swim: ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for long and ran out of water and lost the game")
    else:
        print('Not a valid option. You lose')

elif answer == "right":
    answer = input("You came across a bridge, do you wanna cross it: ")

    if answer == "back":
        print("You go back you lose")
    elif answer == "cross":
        answer = input(
            "You cross you meet a stranger, you wanna talk to them (yes/no): ")

        if answer == "yes":
            print("Congulation", name,
                  "You talk to stranger they give you gold, YOU WIN!!!!")
        elif answer == "no":
            print("You ingore stranger and they are ofended you lose")
        else:
            print('Not valid option you lose')
    else:
        print('Not valid option you lose')
else:
    print('Not a valid option. You lose')
