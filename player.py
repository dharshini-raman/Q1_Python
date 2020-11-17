class Player:
    def __init__(self, amount):
        if amount < 1:
            print('You do not have money')
        self.amount = 100
        self.hand_bet = None
        self.suit_bet = 0
        self.amount_bet = 0
        self.sinput = None
        self.binput = None
        self.badb_bet = 0

    def amount(self):
        if(amount>0):
            return self.amount
        else:
            print("You have no money")
            return self.amount
    def hand_bet(self, hand):
        self.hand_bet = hand

    def amount_bet(self):
        return self.amount_bet
    def sinput(self):
        return self.sinput
    def binput(self):
        return self.binput

    def suit_bet(self):
        return self.suit_bet
    def badb_bet(self):
        return self.badb_bet
    #if player wins suit bet:
    def bad_beats(self, t=0):
        if t==1:
            print("you won the bad beats bet!")
            self.amount += int(self.badb_bet * 40)#3rd card 9,8
            print(self.amount)
        elif t ==2:
            print("you won the bad beats bet!")
            self.amount += int(self.badb_bet * 10) #Natural 9,8
            print(self.amount)
        elif t == 3:
            print("you won the bad beats bet!")
            self.amount += int(self.badb_bet * 6)#8, 7
            print(self.amount)
        elif t == 4:
            print("you won the bad beats bet!")
            self.amount += int(self.badb_bet * 4)#7, 6
            print(self.amount)
        elif t == 5:
            print("you won the bad beats bet!")
            self.amount += int(self.badb_bet * 1)#-1
            print(self.amount)
        elif t == 6:
            print("you did not win the bad beats bet!")
            self.amount -= int(self.badb_bet)#N/A
            print(self.amount)
    def same_suit(self, u=0):
        if u==1:
            print("you won the same suit bet!")
            self.amount += int(self.suit_bet * 25)
            print(self.amount)
            
        elif u ==2:
            print("you won the double same suit bet!")
            self.amount += int(self.suit_bet * 250)
            print(self.amount)
            
        elif u ==3:
            print("you lost the same suit bet!")
            self.amount -= int(self.suit_bet)
            print(self.amount)
            
    #if player wins bet:
    def win(self):
        if self.hand_bet == 'player':
            self.amount += int(self.amount_bet * 1)
        elif self.hand_bet == 'banker':
            self.amount += int(self.amount_bet * 0.95) #Read that the commision only applies to bets placed on banker
        elif self.hand_bet == 'tie':
            self.amount += int(self.amount_bet * 8)
        self.hand_bet = None
        print(self.amount)
        
    
    def tied(self):
        print(self.amount)
        
    #if the player lost their bet
    def lose(self):

            self.amount = (self.amount)-(self.amount_bet)
            self.hand_bet = None
