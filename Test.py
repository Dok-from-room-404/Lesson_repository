



import pygame
from pygame.locals import *

import sys


class Game:
    def __init__(self):
        """Инициализируем класс и создаем словарь с изо"""
        self.dic_image = {
            "title": pygame.image.load('fon.png'),
            "actor": pygame.image.load('mar.png'),
            "box": pygame.image.load('box.png'),
            "grass": pygame.image.load('grass.png')
        }
        
        
    def show(self, screen, clock_fps) -> None:
        self.show_menu(screen, clock_fps) # показывать титульный экран, пока пользователь не нажмет клавишу
        print("menu")
        
        
        
        
    
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
            
    def show_test_level(self):

        #levelObj = levels[levelNum]
        mapObj = decorateMap(levelObj['mapObj'], levelObj['startState']['player'])
        gameStateObj = copy.deepcopy(levelObj['startState'])
        mapNeedsRedraw = True # set to True to call drawMap()
        levelSurf = BASICFONT.render('Level %s of %s' % (levelNum + 1, len(levels)), 1, TEXTCOLOR)
        levelRect = levelSurf.get_rect()
        levelRect.bottomleft = (20, WINHEIGHT - 35)
        mapWidth = len(mapObj) * TILEWIDTH
        mapHeight = (len(mapObj[0]) - 1) * TILEFLOORHEIGHT + TILEHEIGHT
        MAX_CAM_X_PAN = abs(HALF_WINHEIGHT - int(mapHeight / 2)) + TILEWIDTH
        MAX_CAM_Y_PAN = abs(HALF_WINWIDTH - int(mapWidth / 2)) + TILEHEIGHT

        levelIsComplete = False
        # Track how much the camera has moved:
        cameraOffsetX = 0
        cameraOffsetY = 0
        # Track if the keys to move the camera are being held down:
        cameraUp = False
        cameraDown = False
        cameraLeft = False
        cameraRight = False

        while True: # main game loop
            # Reset these variables:
            playerMoveTo = None
            keyPressed = False

            for event in pygame.event.get(): # event handling loop
                if event.type == QUIT:
                    # Player clicked the "X" at the corner of the window.
                    terminate()

                elif event.type == KEYDOWN:
                    # Handle key presses
                    keyPressed = True
                    if event.key == K_LEFT:
                        playerMoveTo = LEFT
                    elif event.key == K_RIGHT:
                        playerMoveTo = RIGHT
                    elif event.key == K_UP:
                        playerMoveTo = UP
                    elif event.key == K_DOWN:
                        playerMoveTo = DOWN

                    # Set the camera move mode.
                    elif event.key == K_a:
                        cameraLeft = True
                    elif event.key == K_d:
                        cameraRight = True
                    elif event.key == K_w:
                        cameraUp = True
                    elif event.key == K_s:
                        cameraDown = True

                    elif event.key == K_n:
                        return 'next'
                    elif event.key == K_b:
                        return 'back'

                    elif event.key == K_ESCAPE:
                        terminate() # Esc key quits.
                    elif event.key == K_BACKSPACE:
                        return 'reset' # Reset the level.
                    elif event.key == K_p:
                        # Change the player image to the next one.
                        currentImage += 1
                        if currentImage >= len(PLAYERIMAGES):
                            # After the last player image, use the first one.
                            currentImage = 0
                        mapNeedsRedraw = True

                elif event.type == KEYUP:
                    # Unset the camera move mode.
                    if event.key == K_a:
                        cameraLeft = False
                    elif event.key == K_d:
                        cameraRight = False
                    elif event.key == K_w:
                        cameraUp = False
                    elif event.key == K_s:
                        cameraDown = False

            if playerMoveTo != None and not levelIsComplete:
                # If the player pushed a key to move, make the move
                # (if possible) and push any stars that are pushable.
                moved = makeMove(mapObj, gameStateObj, playerMoveTo)

                if moved:
                    # increment the step counter.
                    gameStateObj['stepCounter'] += 1
                    mapNeedsRedraw = True

                if isLevelFinished(levelObj, gameStateObj):
                    # level is solved, we should show the "Solved!" image.
                    levelIsComplete = True
                    keyPressed = False

            DISPLAYSURF.fill(BGCOLOR)

            if mapNeedsRedraw:
                mapSurf = drawMap(mapObj, gameStateObj, levelObj['goals'])
                mapNeedsRedraw = False

            if cameraUp and cameraOffsetY < MAX_CAM_X_PAN:
                cameraOffsetY += CAM_MOVE_SPEED
            elif cameraDown and cameraOffsetY > -MAX_CAM_X_PAN:
                cameraOffsetY -= CAM_MOVE_SPEED
            if cameraLeft and cameraOffsetX < MAX_CAM_Y_PAN:
                cameraOffsetX += CAM_MOVE_SPEED
            elif cameraRight and cameraOffsetX > -MAX_CAM_Y_PAN:
                cameraOffsetX -= CAM_MOVE_SPEED

            # Adjust mapSurf's Rect object based on the camera offset.
            mapSurfRect = mapSurf.get_rect()
            mapSurfRect.center = (HALF_WINWIDTH + cameraOffsetX, HALF_WINHEIGHT + cameraOffsetY)

            # Draw mapSurf to the DISPLAYSURF Surface object.
            DISPLAYSURF.blit(mapSurf, mapSurfRect)

            DISPLAYSURF.blit(levelSurf, levelRect)
            stepSurf = BASICFONT.render('Steps: %s' % (gameStateObj['stepCounter']), 1, TEXTCOLOR)
            stepRect = stepSurf.get_rect()
            stepRect.bottomleft = (20, WINHEIGHT - 10)
            DISPLAYSURF.blit(stepSurf, stepRect)

            if levelIsComplete:
                # is solved, show the "Solved!" image until the player
                # has pressed a key.
                solvedRect = IMAGESDICT['solved'].get_rect()
                solvedRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)
                DISPLAYSURF.blit(IMAGESDICT['solved'], solvedRect)

                if keyPressed:
                    return 'solved'

            pygame.display.update() # draw DISPLAYSURF to the screen.
            FPSCLOCK.tick()
    
    
    
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
    size = width, height = 800, 450
    main(size)
    
