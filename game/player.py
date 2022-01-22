class Player:
  
    def __init__(self):
        '''A special method, called a constructor, that initializes two
        attributes. It is invoked using the class name followed by parentheses.
        '''
        self.score = "300"
        self.continue_game = True
        self.guess = ""

    def guess_card(self):
        self.guess = input(f'Higher or Lower? H/L ')
    
    def change_score(self, card1, card2):
        pass

    def end_game(self):
        if self.score <= 0:
            print('You lost')
        else:
            print(f'Final Score: {self.score}')
        print('Thanks for playing')
    