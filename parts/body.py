from random import randint as rnd

class GuesNumber:
    '''This class defines the user's name, 
    the number of games, and outputs the game listen
    '''

    def __init__(self):
        self.user_name = input('Добро пожаловать в игру напишите' 
         'пожалуйста как вас зовут')
    
    def game(self):
        self.count:int = 1
        self.count += 1
        competer_count = rnd(1,100)
        
        while True:
            try:
                hum_num = int(input('please enter your number: '))
                
                if isinstance(hum_num, int):
                    if hum_num == competer_count:
                        print ('you won')
                        break
                    elif hum_num < competer_count:
                        print ('your count smaler')
                    else:
                        print ('Your count more')
                else:
                    raise TypeError
            except:
                print('Incorrect input format, pleasy ty numeric plrase')

game = GuesNumber()
game.game()