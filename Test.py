



import pygame


import sys


class Game:
    def __init__(self):
        """Инициализируем класс и создаем словарь с изо"""
        self.dic_image = {
            "title": pygame.image.load('fon.jpg'),
            "actor": pygame.image.load('mar.png'),
            ""
        }
        
    def show(self): ...
    
    
    
def main(*size):
    pygame.init()
    game = Game()
    pygame.display.set_caption('Перемещение героя')
    
    screen = pygame.display.set_mode(size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()        

        pygame.display.flip()





        



if __name__ == "__main__":
    size = width, height = 800, 450
    main(size)
    
