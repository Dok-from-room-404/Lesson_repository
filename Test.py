



import pygame
from pygame.locals import *
import sys
from Modle import *


class Game:
    def __init__(self):
        """Инициализируем класс и создаем словарь с изо"""
        self.dic_image = {
            "title": pygame.image.load('fon.png'),
            "actor": pygame.image.load('mar.png'),
            "box": pygame.image.load('box.png'),
            "grass": pygame.image.load('grass.png')
        }
        self.dic_image_from_level = {
            "#":  self.dic_image["box"],
            "@":  self.dic_image["actor"],
            ".": self.dic_image["grass"]
        }
        
        
        
        
    def show(self, screen, clock_fps) -> None:
        self.show_menu(screen, clock_fps) # показывать титульный экран, пока пользователь не нажмет клавишу
        print("menu")
        
        self.show_test_level(screen)
        
        
        
        
    
    def show_menu(self, screen, clock_fps) -> None:
        """Отображает титульный экран, пока пользователь не нажмет клавишу"""
        titleRect = self.dic_image['title'].get_rect()
        screen.fill((17, 189, 234))
        screen.blit(self.dic_image['title'], titleRect)

        font = pygame.font.Font('freesansbold.ttf', 18)
        instSurf = font.render("Для начала игры нужно нажать Enter", 1, (0, 0, 0))
        
        instRect = instSurf.get_rect()
        instRect.top = 50
        instRect.centerx = 175
        
        screen.blit(instSurf, instRect)
        pygame.display.flip()
        
        while True: # Основной цикл для стартового экрана.
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                    if event.key == K_RETURN:
                        return # пользователь нажал клавишу, поэтому вернитесь.
            pygame.display.update()
            clock_fps.tick()
            
            
    
    def show_test_level(self, screen):
        level = [['.', '.', '.', '#', '#', '#', '.', '.', '.', '.', '.'], 
                 ['.', '.', '#', '#', '.', '#', '.', '#', '#', '#', '#'], 
                 ['.', '#', '#', '.', '.', '#', '#', '#', '.', '.', '#'], 
                 ['#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
                 ['#', '.', '.', '.', '@', '.', '.', '#', '.', '.', '#'], 
                 ['#', '#', '#', '.', '.', '#', '#', '#', '.', '.', '#'], 
                 ['.', '.', '#', '.', '.', '#', '.', '.', '.', '.', '#'], 
                 ['.', '#', '#', '.', '#', '#', '.', '#', '.', '#', '#'], 
                 ['.', '#', '.', '.', '.', '.', '.', '.', '#', '#', '.'], 
                 ['.', '#', '.', '.', '.', '.', '.', '#', '#', '.', '.'], 
                 ['.', '#', '#', '#', '#', '#', '#', '#', '.', '.', '.']]
        screen.fill((17, 189, 234))
        print(len(level[0]), len(level))
        self.board = Board(len(level[0]), len(level), 50, self.dic_image_from_level)
        self.board.render(screen, level)
        
        

    
    
    
def main(*size):
    
    pygame.init()
    game = Game()
    clock_fps = pygame.time.Clock()
    pygame.display.set_caption('Перемещение героя')
    
    screen = pygame.display.set_mode(size)
    game.show(screen, clock_fps)
    print("show")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()        

        pygame.display.flip()





        



if __name__ == "__main__":
    size = width, height = 550, 550
    main(size)
    
