class Robot:
    population = 0

    def __init__(self, name):
       '''Инициализация данных.'''
        self.name = name
        print('(Инициализация {0})'.format(self.name))
        Robot.population +=1
    def __del__(self):
        '''Я умираю'''
        self.name = name()
        
