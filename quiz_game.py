print("Welcome 😊 to my quiz!")

playing=input("Do you want to play?😊 ")

if playing.lower() != "yes":
     quit()
print("Ok ! Lets Play 😊")
score=0

answer=input("What does cpu stand for ?🤔 ").lower()
if answer=="central processing unit":
     print("Correct 😍")
     score=score+1
else:
     print("Incorrect 😔")


answer=input("What does gpu stand for ?🤔 ").lower()
if answer=="graphic processing unit":
     print("Correct 😍")
     score=score+1
else:
     print("Incorrect 😔")

answer=input("What does ram stand for ?🤔 ").lower()
if answer=="random access memory":
     print("Correct 😍")
     score=score+1
else:
     print("Incorrect 😔")


answer=input("What does rom stand for ?🤔 ").lower()
if answer=="read only memory":
     print("Correct 😍")
     score=score+1
else:
     print("Incorrect 😔")


answer=input("What does psu stand for ?🤔 ").lower()
if answer=="power supply":
     print("Correct 😍")
     score=score+1
else:
     print("Incorrect 😔")


print("You Got {} questions correct".format(score))
print("You Got " + str((score/5*100)) +"%.")


