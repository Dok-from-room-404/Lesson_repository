



import pygame


import sys




class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)
        
    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                n_n = [(x * self.cell_size) + self.left, (y * self.cell_size) + self.top]
                n_k = [self.cell_size, self.cell_size]
                
                
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), n_n + n_k, 1)
        

        
        
        



pygame.init()
pygame.display.set_caption('Движущийся круг 2')
size = width, height = 800, 450
screen = pygame.display.set_mode(size)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()        
    
    pygame.display.flip()