import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

a = int(input("chose rock (0), paper (1), scisors (2), let\'s rock \n"))
b = random.randint(0,2)
if a == 0:
        print(rock)
elif a==1:
        print(paper)
elif a ==2:
        print(scissors)


if b == 0:
        print(rock)
elif b==1:
        print(paper)
elif b ==2:
        print(scissors)


if a==0 and b==0:
        print ("it\'s a tie")
if a==1 and b==1:
        print ("it\'s a tie")
if a==2 and b==2:
        print ("it\'s a tie")
if a==0 and b==1:
        print ("you lose")
if a==0 and b==2:
        print ("you win")
if a==1 and b==0:
        print ("you win")
if a==1 and b==2:
        print ("you lose")
if a==2 and b==0:
        print ("you lose")
if a==2 and b==1:
        print ("you win")