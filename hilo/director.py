from hilo.card import Card

class Director:
    """Directs the game and controls play
    Attributes 
        card (integer): A integer representing a card value.
        playing (boolean): If the game is being played or not.
        player_score (integer): The number of points the player recieves on current round.
        total_score (integer): The total number of points the player has."""
    def __init__(self):
        """ Constructs Director
        Args: 
            self (Director): an instance of Director
        """
        self.card = Card()
        self.playing = True
        self.player_score = 0
        self.total_score = 300
        self.input = ""
    
    def start_game(self):
        """Starts the game by using the main game loop
        Args: 
            self (Director): an instance of Director
        """
        print('''
Welcome to Hilo! In this game you try to guess
if the next card drawn will be higher or lower
than the previous card. The card suits are also
taken into account. The order from lowest to
highest is Club, Diamond, Heart, Spade.
You win 100 points if correct, and loose 75
if incorrect. Good Luck!''')


        while self.playing: 
            value, sub_value = self.get_input()
            self.card.draw()
            self.calc_points(value, sub_value)
            self.give_outputs()
            self.check_points()

    def get_input(self):
        """ Gets user input
        Args:
            self (Director): An instance of Director.
        """
        value = self.card.value
        sub_value = self.card.sub_value
        while True:
            print(f'\nThe card is {round(self.card.value)} of {self.card.suit}')
            self.input = input('Higher or lower? [h/l]')
            if self.input == 'h' or self.input =='l':
                break
            else:
                print('That is not valid, please use h or l')

        return value, sub_value
        

    def calc_points(self, value, sub_value):
        """ Gets user input
        Args:
            self (Director): An instance of Director.
            value (int): The value of the card this current round
        """

        next_value = self.card.value
        next_sub_value = self.card.sub_value

        if next_sub_value == sub_value:
            if next_value > value and self.input == 'h':
                print('You won!')
                self.total_score += 100
            elif next_value < value and self.input == 'l':
                print('You won!')
                self.total_score += 100
            elif next_value == value:
                print('That was the same card!')
            else:
                print('Wrong answer :(')
                self.total_score -= 75

        elif next_sub_value > sub_value:
            if next_value > value and self.input == 'h':
                print('You won!')
                self.total_score += 100            
            else:
                print('Wrong answer :(')
                self.total_score -= 75
        else:
            if next_value < value and self.input == 'l':
                print('You won!')
                self.total_score += 100            
            else:
                print('Wrong answer :(')
                self.total_score -= 75    

    def give_outputs(self):
        """"Tells the player what their next card was and their points
        Args:
            self (Director): An instance of Director.
        """
        print(f'Next Card was {self.card.value} of {self.card.suit}')
        print(f"You have {self.total_score} points!")

    def check_points(self):
        """"Checks if the player can play again
        Args:
            self (Director): An instance of Director.
        """
        if self.total_score <= 0:
            print('You ran out of points, you lose\n')
            self.playing = False
            return
        else:
            while True:
                play_again = input("Play again? (y/n): ")
                if play_again == "y":
                    break
                elif play_again == 'n':
                    self.playing = False
                    break
                else:
                    print("Please enter 'y' or 'n'.")
