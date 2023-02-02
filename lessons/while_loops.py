# Comment 
"""Demonstrates while loops by finding low value in string"""

cards: str = "5235"

card_idx: int = 0
#look at each number in string 
"""while card_idx < 4:
    print(cards[card_idx])
    card_idx = card_idx + 1"""

low_card: int = int(cards[0])
#look at each number in in string
while card_idx < 4:
    #check if current card is less than the low card 
    current_card: int = int(cards[card_idx])
    if (current_card < low_card):
        #update low card value to be current card value 
        low_card = current_card
    card_idx = card_idx + 1
print(low_card)
