import cards
import player
print('Welcome to Baccarat!')
player_num=int(input('How many people are playing?'))
quit= "No"
#1)Basic-Yes
#2)Betting-Yes
#3)Multiplayer-Yes
#4)Tipping-No
#5)Ladies/Gents-Yes
#6)BonusBet-Yes
i=0
player_list =[]
while quit != "Yes":
    deck1 = cards.Deck()
    deck3 = cards.Deck()
    print("Created a new deck.")
    deck1.populate()
    deck3.populate()
    print("\nPopulated the deck.")
    deck1.shuffle()
    deck3.shuffle()
    print("\nShuffled the deck.")
    
    player_hand3 = cards.Hand()
    banker_hand3 = cards.Hand()
    player_hand = cards.Hand()
    banker_hand = cards.Hand()
    hands = [player_hand, banker_hand]
    hands3 = [player_hand3, banker_hand3]
    deck1.deal(hands, per_hand = 2)
    while i<(player_num):
        print("Player: " + str(i+1))
        player_list.append(player.Player(100))
        player_list[i].sinput= input('Would you like to bet on Same Suite? Y/N')
        if(player_list[i].sinput=="Y"):
            while((player_list[i].suit_bet<10) and ((player_list[i].amount-player_list[i].suit_bet)>0)):
                player_list[i].suit_bet= int(input('How much would you like to bet on Same Suit(must be $10+)?: '))
                while((player_list[i].amount-player_list[i].suit_bet)<0):
                    player_list[i].suit_bet= int(input('How much would you like to bet on Same Suit(must be $10+)?: '))
        player_list[i].binput= input('Would you like to bet on Bad Beats? Y/N')
        if(player_list[i].binput=="Y"):
            while(player_list[i].badb_bet<10 and ((player_list[i].amount-player_list[i].badb_bet)>0)):
                player_list[i].badb_bet= int(input('How much would you like to bet on Bad Beats(must be $10+)?: '))
                while((player_list[i].amount-player_list[i].badb_bet)<0):
                    player_list[i].badb_bet= int(input('How much would you like to bet on Bad Beats(must be $10+)?: '))
        player_list[i].hand_bet = input('Who would you like to bet on:player, banker, tie: ')
        while(player_list[i].amount_bet<10 and ((player_list[i].amount-player_list[i].amount_bet)>0)):
            player_list[i].amount_bet = int(input('How much would you like to bet(must be $10+)?: '))
            while((player_list[i].amount-player_list[i].amount_bet)<0):
                    player_list[i].amount_bet= int(input('How much would you like to bet(must be $10+)?: '))
        i=i+1
    
    print("\nDealt 2 cards to your hand and banker hand.")
    print("Player hand:")
    print(player_hand)
    
    sp =(player_hand.Sum())
    print(sp)
    print("Banker hand:")
    print(banker_hand)
    sb =(banker_hand.Sum())
    print(sb)
    pt = False
    bt = False
    if (((player_hand.Sum()!= 8) and (player_hand.Sum()!= 9)) and ((banker_hand.Sum()!= 8) and (banker_hand.Sum()!= 9))):
        
        if (player_hand.Sum() < 6):
            deck3.deal(hands3, per_hand = 1)
            print("player third card:")
            print(player_hand3)
            s3 =player_hand3.Sum()
            print("New Player Sum")
            sp=sp+s3
            ##
            print(player_hand.Sum(S =sp, third=True))
            pt = True
        else:
            pt = False
    
        if (pt == False):
            if (banker_hand.Sum() < 6):
                bt = True
        else:
            if (banker_hand.Sum() < 3):
                bt = True
            if (banker_hand.Sum()==3 and s3 != 8):
                bt = True
            if (banker_hand.Sum()==4 and s3 > 1 and s3 < 8):
                bt = True
            if (banker_hand.Sum()==5 and s3 > 3 and s3 < 8):
                bt = True
            if (banker_hand.Sum()==6 and s3 > 5 and s3 < 8):
                bt = True
            if(bt == True):
                #deck3.deal(hands3, per_hand = 1)
                
                print("Banker Third Card:")
                print(banker_hand3)
                s3 =banker_hand3.Sum()
                print("New Banker Sum")
                sb=sb+s3
                print(sb)
                print(banker_hand.Sum(S =sb, third=True))
                #print("issues")

    for i in range(player_num): 
        print("Player: " + str(i+1))
        if(player_list[i].hand_bet =='player'):
            if(sp>sb):
                player_list[i].win()
                print("you won!")
            if(sp<sb):
                player_list[i].lose()
                print("You lost!")
            if(sp==sb):
                player_list[i].tied()
                print("You tied!")
        elif(player_list[i].hand_bet =='banker'):
            if(sp<sb):
                
                player_list[i].win()
                print("You won!")
            if(sp>sb):
                player_list[i].lose()
                print("You lost!")
            if(sp==sb):
                player_list[i].tied()
                print("You tied!")
        elif(player_list[i].hand_bet =='tie'):
            if(sp==sb):
                player_list[i].win()
                print("You won!")
            if(sp!=sb):
                player_list[i].lose()
                print("You lost!")
        print(player_list[i].amount)
        #SameSuits
        if(player_list[i].sinput=="Y"):
            suit=0
            if(player_hand.sameSuit()==True and banker_hand.sameSuit()==False):
                player_list[i].same_suit(u=1)
                suit+1
            elif(banker_hand.sameSuit()==True and player_hand.sameSuit()==False):
                player_list[i].same_suit(u=1)
                suit+1
            elif(player_hand.sameSuit()==True and banker_hand.sameSuit()==True):
                player_list[i].same_suit(u=2)
            else:
                player_list[i].same_suit(u=3)
        #BadBeats
        
        if(player_list[i].binput=="Y"):
            print("BadBeats:")
            if(bt==True and pt==True and (sp==9 and sb==8 or (sb==9 and sp==8))):
                player_list[i].bad_beats(t=1)
            if(bt==False and pt==False and ((sp==9 and sb==8) or (sb==9 and sp==8 ))):
                player_list[i].bad_beats(t=2)
            elif((sp==7 and sb==8) or (sb==7 and sp==8 )):
                player_list[i].bad_beats(t=3)
            elif((sp==7 and sb==6) or (sb==7 and sp==6 )):
                player_list[i].bad_beats(t=4)
            elif(((sp-sb)==1) or ((sb-sp)==1)):
                player_list[i].bad_beats(t=5)
            else:
                player_list[i].bad_beats(t=6)
        if(player_list[i].amount<10):
            print("you ran out of money")
            player_list.pop(i)
        else:         
            player_list[i].hand_bet = None
            player_list[i].suit_bet = 0
            player_list[i].amount_bet = 0
            player_list[i].sinput = None
            player_list[i].binput = None
            player_list[i].badb_bet = 0
    i=0
    quit=input('Quit Game? Yes or No')
    
deck1.clear()
