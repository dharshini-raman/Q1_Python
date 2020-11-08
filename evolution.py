from digigon import DigiPoke
import random
class Evolved(DigiPoke):
    Type2 = ""
    def __init__(self, Name, Type, Health, Record, T2):
        super().__init__(Name, Type, Health, Record)
        self.Type2=T2

    def Type2Creator(self):
        number = random.randint(1, 4)
        if (number == 1 and self.Type != 'Fire'):
            self.Type2 = 'Fire'
        else:
            self.Type2 = 'Water'
        if (number == 2 and self.Type != 'Earth'):
            self.Type2 = 'Earth'
        else: self.Type2 = 'Air'
        if (number == 3 and self.Type != 'Water'):
            self.Type2 = 'Water'
        else:
            self.Type2 = 'Fire'
        if (number == 4 and self.Type != 'Air'):
            self.Type2 = 'Air'
        else: self.Type2 = 'Earth'
        print(self.Type2)
    def Status(self):
        print("Name: ", self.Name,  "Type: ", self.Type, "Type 2: ", self.Type2,"Health: ", self.Health, "Record ", self.Record)
        
evolved =0            

my_new_digi= DigiPoke('','Fire' , 100, 0)
my_new_digi.Name = input("Please enter this Name) \n")
my_new_digi.Type = input("Please enter a type: (Fire, Earth, Water, Air) \n")
choice = int(input("What would you like to do?: 1. Fight 2. Heal 3. Evolve 4. Retire 5. Status Check "))
while (my_new_digi.Health >0):
    print(choice)
    if choice == 1:
        if evolved == 0:
            my_new_digi.Fight()
        if evolved == 1:
            my_evolved_digi.Fight()
        choice = int(input("What would you like to do?: 1. Fight 2. Heal 3. Evolve 4. Retire 5. Status Check "))
    if choice ==2:
        if evolved == 0:
            my_new_digi.Heal()
        if evolved == 1:
            my_evolved_digi.Heal()
        choice = int(input("What would you like to do?: 1. Fight 2. Heal 3. Evolve 4. Retire 5. Status Check "))
    if choice ==3:
        if(my_new_digi.Record>=5):
            evolved =1
            my_evolved_digi= Evolved(my_new_digi.Name, my_new_digi.Type, 100, 0,"")
            my_evolved_digi.Type2Creator()
        print(my_new_digi.Name, my_evolved_digi.Name )
        choice = int(input("What would you like to do?: 1. Fight 2. Heal 3. Evolve 4. Retire 5. Status Check  "))
    if choice ==4:
        break
    if choice ==5:
        if evolved == 0:
            my_new_digi.Status()
            choice = int(input("What would you like to do?: 1. Fight 2. Heal 3. Evolve 4. Retire 5. Status Check  "))
        if evolved == 1:
            my_evolved_digi.Status()
            choice = int(input("What would you like to do?: 1. Fight 2. Heal 3. Evolve 4. Retire 5. Status Check  "))
