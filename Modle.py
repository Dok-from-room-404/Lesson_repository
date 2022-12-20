



import pygame




class Board:
    def __init__(self, width, height, cell_size=50, dic_image_from_level={}):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.board = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.dic_image_from_level = dic_image_from_level

 

 
    def render(self, screen, level):
        wcolor = pygame.Color(255, 255, 255)
        for y in range(self.height):
            for x in range(self.width):
                n_x, n_y = self.left + self.cell_size * y, self.top + self.cell_size * x
                k_x, k_y = self.cell_size, self.cell_size
                
                pygame.draw.rect(screen, wcolor, (n_x, n_y, k_x, k_y), 1)
                
                
                level_res = level[y][x]
                print(level_res)
                if level_res == "@":
                    titleRect = self.dic_image_from_level["."].get_rect()
                    titleRect.bottomleft = (n_x, n_y + 50)
                    screen.blit(self.dic_image_from_level["."], titleRect)
 
                    
                    
                    
                    
                titleRect = self.dic_image_from_level[level[y][x]].get_rect()
                titleRect.bottomleft = (n_x, n_y + 50)
                
                screen.blit(self.dic_image_from_level[level[y][x]], titleRect)
 
    
 
    def get_cell(self, mouse_pos):
        board_width = self.width * self.cell_size
        board_height = self.height * self.cell_size
        if self.left < mouse_pos[0] < self.left + board_width:
            if self.top < mouse_pos[1] < self.top + board_height:
                cell_coords = (mouse_pos[1] - self.left) // self.cell_size,\
                              (mouse_pos[0] - self.top) // self.cell_size
                return cell_coords
        return None
 
    def click(self, cell_coords):
        x = (cell_coords[0] // self.cell_size) - (self.left // self.cell_size)
        y = (cell_coords[1] // self.cell_size) - (self.top // self.cell_size)
        
        
        if x >= 0 and y >= 0 and x < self.width and y < self.height:
            return (x, y)
        
