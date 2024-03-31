name=input("Type your name: ")
print("Welcome",name,"to this adveenture! ")
answer=input(
    "You are on a dirt road,it has come to an end and you can go left or right.Which way you would to go? ").lower()
if answer=="left":
    answer=input("You come to a river,you can walk around it or swim accross? Type walk to walk around and swim to swwim acrosss ")

    if answer=="swim":
          print("You swim across and were eaten by an aligator.")
    elif answer=="walk":
          print("You walked for many miles,ran out of water and you lost the game")
    else:
          print("Not a valid option.You lose")

elif answer=="right":
    answer=input("You come to a bridge ,it looks wobbly, do you want to cross it or head back (cross/headback) ")

    if answer=="back":
          print("You go back and loose")
    elif answer=="cross":
          answer=input("You cross the bridge and meet the stranger.Do you talk to them? jas")
          if answer=="yes":
               print("You talk to rstranger and they gave you gold.YOU WIN")
          elif answer=="no":
               print("you ignore the stranger and they offended and you loose")
          else:
               print("Not a valid option.You lose")
    else:
          print("Not a valid option.You lose")


else:
    print("Not a valid option .You lose")