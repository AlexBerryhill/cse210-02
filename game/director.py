from game.card import Card

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
        while self.playing: 
            value = self.get_input()
            self.card.draw()
            self.calc_points(value)
            self.give_outputs()
            self.check_points()

    def get_input(self):
        """ Gets user input
        Args:
            self (Director): An instance of Director.
        """
        value = self.card.value
        while True:
            print(f'\nThe card is {self.card.value}')
            self.input = input('Higher or lower? [h/l]')
            if self.input == 'h' or self.input =='l':
                break
            else:
                print('That is not valid, please use h or l')

        return value
        

    def calc_points(self, value):
        """ Gets user input
        Args:
            self (Director): An instance of Director.
            value (int): The value of the card this current round
        """
        next_value = self.card.value
        if ((next_value > value) and self.input=='h'):
            print('You won!')
            self.total_score += 100
        elif ((next_value < value) and self.input=='l'):
            print('You Won!')
            self.total_score += 100
        elif (next_value == value):
            print('That was the same card!')
            pass
        else:
            print('Wrong answer :(')
            self.total_score -= 75       

    def give_outputs(self):
        """"Tells the player what their next card was and their points
        Args:
            self (Director): An instance of Director.
        """
        print(f'Next Card was {self.card.value}')
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
