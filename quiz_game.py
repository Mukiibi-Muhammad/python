print("Welcome to my computer quiz!")

playing = input("Do you want to play")

if playing.lower() != "yes":
    quit()


print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print('correct!')
    score += 1

else:
    print("Incorrect")

answer = input("What does GPU stand for? ")
if answer == "graphic process unit":
    print('correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print('correct!')
    score += 1

else:
    print("Incorrect")

answer = input("What does PSU stand for? ")
if answer == "power supply unit":
    print('correct!')
    score += 1

else:
    print("Incorrect")

print("You have got " + str(score) + " questions correct")
print("You have got " + str((score/4)*100) + "% questions correct")
