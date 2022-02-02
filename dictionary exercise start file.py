# This program uses a dictionary as a deck of cards.

def main():
    # Create a deck of cards.
    deck = create_deck()

    # Get the number of cards to deal.
    num_cards = int(input('How many cards should I deal? '))



    # Deal the cards.
    deal_cards(deck,num_cards)

    

    
    

# The create_deck function returns a dictionary
# representing a deck of cards.
def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    # Return the deck.
    return deck



# The deal_cards function deals a specified number of cards
# from the deck.

def deal_cards(deck, num_cards):
    # Initialize an accumulator for the hand value.
    hand = 0
    
    
    

    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck.
    if num_cards > 52:
        print('Too many cards. Please try again')
        num_cards = 52
    
    

    # Deal the cards and accumulate their values.
    import random
    
    for i in range(num_cards):
        name_card = random.choice(list(deck))
        hand += deck[name_card]
        print(name_card)

        del deck[name_card]
    
    
    
    '''
    #for count in range(num_card):
        card = random.choice(list(deck))
        value = deck[card]
        print(card)
        hand_value += value

        del deck[card]


    '''

    # Display the value of the hand.
    print('The value of the hand is', hand,'.')
    
    

# Call the main function.
main()