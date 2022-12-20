



import pygame




class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
 
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
 
    def render(self, surface):
        wcolor = pygame.Color(255, 255, 255)
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(surface, wcolor, (self.left + self.cell_size * j, self.top + self.cell_size * i,
                                                   self.cell_size, self.cell_size), 1 if self.board[i][j] == 0 else 0)
 
    
 
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