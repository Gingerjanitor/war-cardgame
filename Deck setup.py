

        
        
class card():
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value
        
    def reveal(self):
        print(f"The card is a {self.value} of {self.suit}")
        return "test"
        
class deck(card): 
    def __init__(self):
        self.deck=self.gen_deck()
        
    def gen_cardvals(self):
        cards=["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
        rawnumbers=[2,3,4,5,6,7,8,9,10,11,12,13,14]
        card_vals=dict(zip(cards,rawnumbers))
        print(card_vals)
        return card_vals
    
    def gen_deck(self):
        suits=["Spades","Diamonds","Hearts","Clubs"]
        card_vals=self.gen_cardvals()
        finaldeck=[]
        for suit in suits:
            for face,val in card_vals.items():
                cardname=[face+"_"+str(val)]
                cardname[0]=card(suit,{face:val})
                finaldeck.append(cardname[0])
        return finaldeck        
        
    


class player():
    def __init__():
        pass

master=deck()
print(master.deck[11].reveal())