# Cards Module
# Basic classes for a game with playing cards

class Card(object):
    """ A playing card. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit, value = 0, face_up = True):
        self.suit = suit
        self.rank = rank
        if (self.rank != "J" and self.rank != "Q" and self.rank != "K" and self.rank != "10" and self.rank != "A"):
            self.value= int(self.rank)
            
        elif (self.rank == "A"):
            self.value =1
        else: 
            self.value = 0
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit + " card:" + str(self.value)
        else:
            rep = "XX"
        return rep


    def flip(self):
        self.is_face_up = not self.is_face_up
       

   


class Hand(object):
    """ A hand of playing cards. """
    def __init__(self):
        self.cards = []
        

    def __str__(self):
        if self.cards:
           rep = ""
           for card in self.cards:
               rep += str(card)+ "\t"
        else:
            rep = "<empty>"
        return rep 
    
    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
    def sameSuit(self):
        suit_list=[]
        for cards in self.cards:
            suit_list.append(cards.suit)
            #print(suit_list)
        if (len(suit_list)==2):
            if(suit_list[0]==suit_list[1]):
                return True
            else:
                return False
    def Sum(self, S=0,third=False):
        if third==False:
            for cards in self.cards:
                                
                S+=cards.value
        if(S>9):
            S=S%10        
        return(S)

class Deck(Hand):
    """ A deck of playing cards. """
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS: 
                self.add(Card(rank, suit))
                

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    
    def deal(self, hands, per_hand = 2):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't continue deal. Out of cards!")
