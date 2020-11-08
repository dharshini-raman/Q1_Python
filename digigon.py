import random
import sys
class DigiPoke():

    def __init__(self, Name, Type, Health, Record):
        self.Name = N
        self.Type = T
        self.Health = 100
        self.Record = 0
        
    #def get_name(self):
    #   assigned_name = input("Please enter a name:\n")
    #   print(f'You entered {value}')
    #   return assigned_name
    #def get_type(self):
     #   assigned_type = input("Please enter a type: (Fire, Earth, Water, Air) \n")
      #  print(f'You entered {value}')
       # return assigned_type
    
    def Fight(self):
        result = random.randint(0, 1)
        if (result == 0):
            print('You won this round!')
            self.Record=self.Record+1
            self.Health=self.Health - 10
            
        if (result == 1):
            print('You lost this round!')
            self.Health=self.Health - 25
        print(self.Health)

    def Heal(self):
        self.Record=self.Record-0.5
        self.Health=self.Health + 10
        print(self.Health)
    def Status(self):
        print("Name: ", self.Name,  ", Type: ", self.Type,", Health: ", self.Health, ", Record: ", self.Record)
        
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
        print("Name: ", self.Name,  ", Type: ", self.Type, ", Type 2: ", self.Type2,", Health: ", self.Health, ", Record: ", self.Record)
    def Retire(self):
        sys.exit()
        
evolved =0            


N = input("Please enter a Name \n")
T = input("Please enter a type: (Fire, Earth, Water, Air) \n")
my_new_digi= DigiPoke(N,T, 100, 0)
choice = int(input("What would you like to do?: 1. Fight 2. Heal 3. Evolve 4. *option unavailable* 5. Status Check "))

if evolved == 0:
    while (my_new_digi.Health > 1):
        print(choice)
        if choice == 1:
            if evolved == 0:
                my_new_digi.Fight()
            choice = int(input("What would you like to do?: 1. Fight 2. Heal 3. Evolve 4. *option unavailable* 5. Status Check  "))
        if choice ==2:
            if evolved == 0:
                my_new_digi.Heal()
            choice = int(input("What would you like to do?: 1. Fight 2. Heal 3. Evolve 4. *option unavailable* 5. Status Check  "))
        if choice ==3:
            if(my_new_digi.Record>=5):
                evolved =1
                my_evolved_digi= Evolved(my_new_digi.Name, my_new_digi.Type, 100, 0,"")
                my_evolved_digi.Type2Creator()
            #print(my_new_digi.Name, my_evolved_digi.Name )
            choice = int(input("What would you like to do?: 1. Fight 2. Heal 3. Evolve 4. *option unavailable* 5. Status Check "))
        if choice ==5:
            my_new_digi.Status()
            choice = int(input("What would you like to do?: 1. Fight 2. Heal 3. Evolve 4. *option unavailable* 5. Status Check  "))

if evolved == 1:
    while (my_evolved_digi.Health >0):
        print(choice)
        if choice == 1:
            my_evolved_digi.Fight()
            choice = int(input("What would you like to do?: 1. Fight 2. Heal 3. Evolve 4. Retire 5. Status Check "))
        if choice ==2:
            my_evolved_digi.Heal()
            choice = int(input("What would you like to do?: 1. Fight 2. Heal 3. Evolve 4. Retire 5. Status Check "))
        if choice ==3:
            if(my_new_digi.Record>=5):
                evolved =1
                my_evolved_digi= Evolved(my_new_digi.Name, my_new_digi.Type, 100, 0,"")
                my_evolved_digi.Type2Creator()
            #print(my_new_digi.Name, my_evolved_digi.Name )
            choice = int(input("What would you like to do?: 1. Fight 2. Heal 3. Evolve 4. Retire 5. Status Check  "))
        if choice ==4:
                my_evolved_digi.Retire()
        if choice ==5:
            my_evolved_digi.Status()
            choice = int(input("What would you like to do?: 1. Fight 2. Heal 3. Evolve 4. Retire 5. Status Check  "))
