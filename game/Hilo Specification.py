from random import randint

def main():
    Score = 300
    Cards = randint(0, 13)
    F = 0
    End = 'Y'
    Result =''
    while  End.upper == 'Y' or Score > 0:
        Card1 = randint(0, 13)
        print(f'The card is: {Card1}')
        Selection =input(f'Higher or Lower? H/L ')
        Card2 = randint(0, 13)
        print(f'New card was: {Card2}') 
        Result = WinOrLost(Card1, Card2)
        Score = ChangeScore(Result,Selection,Score)
        print(f'Your score is: {Score}')
        End = input('Play again? Y/N ')
        print()
    else: 
        if Score <= 0:
            print('You lost')
        else:
            print(f'Final Score: {Score}')
        print('Thanks for playing')
        
def WinOrLost(Card1, Card2):
    if Card1 > Card2:
        Result = 'L'
    elif Card2 > Card1:
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
        pass
    
class Card:
    def __init__(self):
        self.number = randint(0, 13)