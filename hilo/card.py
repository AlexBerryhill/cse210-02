import random

class Card:
    """
    A card with a value from 1 - 13

    Attributes:
    value (int): value of 'drawn' card

    Responsibility of card is to hold the value of the card that is "drawn"
    from the deck
    """

    def __init__(self):
        """Constructs a new instance of Card.
        Args:
            self (Card): An instance of Card.
        """
        self.value = 0
        self.sub_value = 0
        self.suit = ''
        self.draw()

    def draw(self):
        """
        'Draws' a card from the deck by generating a value from
        1 - 13
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 13)
        self.suit = random.choice(['Clubs', 'Diamonds', 'Hearts', 'Spades'])
        if self.suit == 'Clubs':
            self.sub_value = 1
        if self.suit == 'Diamonds':
            self.sub_value = 2
        if self.suit == 'Hearts':
            self.sub_value = 3
        if self.suit == 'Spades':
            self.sub_value = 4

        
