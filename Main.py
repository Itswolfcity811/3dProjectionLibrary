
from Projections import OrthographicProjection, PerspectiveProjection
from Draw import DrawPoint, DrawLine, DrawSquare, DrawCube, DrawWireFrame
from RotateWireFrame import rotateX, rotateY, rotateZ, FindCenter


import pygame.freetype

import pygame
pygame.init()

import math

def main(save=False):
    window = pygame.display.set_mode([2500, 2500])
    
    c = pygame.time.Clock()
    
    font = pygame.freetype.Font("Acme-Regular.ttf", size=200)
    font.fgcolor = (255, 255, 255)
    
    load = False
    if load:
        with open("Frame.json", "r") as file:
            frame = file.read()
    else:
        z = 50
        z2 = 65
        frame = [[400, 400, z], [400, 800, z], [800, 800, z], [800, 400, z], [400, 400, z]]
        box2  = [[540, 540, z2], [540, 840, z2], [840, 840, z2], [840, 540, z2], [540, 540, z2]]
    
    CamDistance = 150
    
    window.fill((0, 0, 0))
    
    rotation = 0
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            """    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    point[2] += 1
                elif event.key == pygame.K_s:
                    point[2] -= 1
            """
        
        window.fill((0, 0, 0))
        
        font.render_to(window, (0, 2300), "Last Frame Draw Time: " + str((c.get_time() - 250) / 1000))
        
        DrawCube(window, [250, 250, 15], 100, CamDistance, degrees=rotation,  projection=PerspectiveProjection) #, projection=PerspectiveProjection
        
        #This is in radions.
        #frame = rotateY(frame, FindCenter(frame), 0.25)    
         
        pygame.display.flip()
        c.tick(20)
        
        if save == True:
            print(pygame.image.tostring(window, "RGBX"))
        
        pygame.time.wait(250)
        
        rotation += 1
        
        if rotation >= 360:
            rotation = 0

if __name__ == "__main__":
    main(False)
