import random
bank = ('Potter', 'Divya', 'Rachel', 'Jonathan')
name = random.choice(bank)
intitialName = name
scrambledName=""
pos =0
while name:
        pos = random.randint(0,len(name)-1)
        scrambledName = scrambledName + name[pos]
        name = name[:pos] + name[(pos + 1):]

#IK IK I could have used a loop...
print(scrambledName)  
print("Guess:")
guess=input()
if guess==intitialName:
    print("You got it!")
elif guess!=intitialName:
    print("try again!")
    guess2=input()
    if guess2==intitialName:
        print("You got it!")
    elif guess2!=intitialName:
        print("You suck at this")
        guess3=input()
        if guess3==intitialName:
            print("Finally!")
        elif guess3!=intitialName:
            print("Really?")
            guess4=input()
            if guess4==intitialName:
                print("Was it really that hard?")
            elif guess4!=intitialName:
                print("Tsk Tsk Tsk")
                guess5=input()
                if guess5==intitialName:
                    print("It took you that many tries?")
                elif guess5!=intitialName:
                    print("Just Leave")
    
