from random import randint

class Player:
    """
    A class describing everything pertaining to the Player object. This class will handle 
    most of the game's logic and keep track of the score.
    """
  
    def __init__(self):
        '''A special method, called a constructor, that initializes three
        attributes. It is invoked using the class name followed by parentheses.
        '''
        self.score = 300
        self.continue_game = True
        self.guess = ""

    def guess_card(self):
        """Method to get the player's guess"""
        self.guess = input('Higher or Lower? [H/L]')

    def end_game(self):
        """Handles the logic to check if game over conditions have been achieved 
        (either the player's score reaches 0 or the player doesn't wish to continue)."""

        if self.score > 0:
            again = input("Play again? [y/n]: ")
            if again == "n":
                print(f'Final Score: {self.score}')
                print("Game Over! Thanks for Playing")
                self.continue_game = False
        else:
            print("Game Over! Thanks for Playing")
            self.continue_game = False
            
    
"""     def change_score(self, card1, card2):
        pass """

class Card:
    """Class that handles the card object and it's related attributes."""
    def __init__(self, number=None):
        if number is None:
            number = randint(1,13)
        self.number = number

def main():
    player1 = Player()
    Result =''
    while player1.continue_game == True:
        Card1 = Card()
        print(f'The card is: {Card1.number}')
        player1.guess_card()
        Card2 = Card()
        print(f'New card was: {Card2.number}') 
        Result = WinOrLost(Card1, Card2)
        player1.score = ChangeScore(Result, player1.guess, player1.score)
        print(f'Your score is: {player1.score}')
        player1.end_game()
        print()
        
def WinOrLost(Card1, Card2):
    if Card1.number > Card2.number:
        Result = 'L'
    elif Card2.number > Card1.number:
        Result = 'H'
    else: 
        Result = ''
    return Result

def ChangeScore(Result, Selection,Score):
    if Result  == Selection.upper():
        Score = Score + 100
    else:
        Score = Score - 75
    return Score

main()



    


    

