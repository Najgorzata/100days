print('''
   ._________________.
   |.---------------.|
   ||               ||
   ||   -._ .-.     ||
   ||   -._| | |    ||
   ||   -._|"|"|    ||
   ||   -._|.-.|    ||
   ||_______________||
   /.-.-.-.-.-.-.-.-.\
  /.-.-.-.-.-.-.-.-.-.\
 /.-.-.-.-.-.-.-.-.-.-.\
/______/__________\___o_\ DrS
\_______________________/
''')
print("Welcome to WSB.")
print("Your mission is to not to die.") 

a = input("You are in WSB, do you choose to stay or leave?")
if a.lower() == "leave":
        b = input("You may learn python by yourself. You chose Y or N?")
        if b.upper() == "Y":
                c = input("It's you last call, leave this shit. Are you sure you want to study python? Y or N?")
                if c.upper() == "N":
                        print("YOU WON!!!!")
                else:
                        print("you are dead")
        else:
               print("lucky bastard") 
        

else:
        print("you are dead")
