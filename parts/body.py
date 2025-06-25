from parts.Protection import protection
from parts import *
class GuesNumber:
    '''This class defines the user's name, 
    the number of games, and outputs the game listen
    '''
    count = 1
    competer_count = rnd(1,100)
    def __init__(self):
        self.user_name = input('Добро пожаловать в игру напишите' 
         'пожалуйста как вас зовут: ')
    
    def add_info(self,user_name):
        print (f"count game's {self.count}")
        
    def add_num(self, user_name):
        print (self.competer_count)
        
        
    def game(self):
        self.count += 1
        while True:
            try:
                
                hum_num = input('please enter your number:')
                if hum_num == 'stop':
                    GuesNumber.menu(self)
                else:
                    hum_num = int(hum_num)
                    if type(hum_num) == int:
                        if hum_num == self.competer_count:
                            print ('you won')
                            self.competer_count = rnd(1,100)
                            break
                        elif hum_num < self.competer_count:
                            print ('your count smaler')
                        else:
                            print ('Your count more')
                    else:
                        raise ValueError
            except ValueError:
                print('Incorrect input format, pleasy ty numeric plrase')


    def menu(self):
        while True:
            input_hum = input('Welcom to the game please input comand start/info or answer: ')
            match input_hum:
                case 'start':
                    GuesNumber.game(self)
                case 'answer':
                   protection(GuesNumber.add_num)(self, user_name=self.user_name)
                case 'info':
                    protection(GuesNumber.add_info)(self, user_name=self.user_name)
                case 'stop':
                    break

