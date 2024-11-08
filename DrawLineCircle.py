"""
DrawLineCircle

Description: Draws a line out of circles
"""
import pygame
pygame.init()
import math

from Scale import Scale
from Projections import OrthographicProjection, PerspectiveProjection

def dist(myList):
    end = 0
    for a in myList:
        for b in myList:
            dist = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)
          
            end += dist
            
    return end
    
def CircleLine(window, point1_2, point2_2, CamDistance, color=(255, 255, 255), projection=OrthographicProjection):
    point1 = point1_2[:]
    point2 = point2_2[:]
    
    XProjected, YProjected = projection(point1, CamDistance)
    
    scale = Scale(point1[2], CamDistance)
    
    pygame.draw.circle(window, color, (XProjected, YProjected), scale)
    
    change = 5
    
    change = lambda i : i / 18
    
    #print( dist([[point1[0] + change, point1[1], point1[2]], point2]) )
    """
    for i in range(len(point1)):
        b = -(Scale(point1[2]) * 2)

        point1[i] = round(point1[i], b)
    
    for i in range(len(point2)):
        point2[i] = round(point2[i], -(Scale(point2[2]) * 2))
    """
    
    while point1 != point2:
        #change = Scale(point1[2]) * 2
        
        #print(change)
        
        changed = False
        if dist([[point1[0] + change(scale), point1[1], point1[2]], point2]) < dist([point1, point2]):
            point1[0] += change(scale)
            changed = True
        elif dist([[point1[0] - change(scale), point1[1], point1[2]], point2]) < dist([point1, point2]):
            point1[0] -= change(scale)
            changed = True
            
        if dist([[point1[0], point1[1] + change(scale), point1[2]], point2]) < dist([point1, point2]):
            point1[1] += change(scale)
            changed = True
        elif dist([[point1[0], point1[1] - change(scale), point1[2]], point2]) < dist([point1, point2]):
            point1[1] -= change(scale)
            changed = True
        
        if dist([[point1[0], point1[1], point1[2] + change(scale)], point2]) < dist([point1, point2]):
            point1[2] += change(scale)
            changed = True
        elif dist([[point1[0], point1[1], point1[2] - change(scale)], point2]) < dist([point1, point2]):
            point1[2] -= change(scale)
            changed = True
            
        scale = Scale(point1[2], CamDistance)
        
        #print(scale)
                
        XProjected, YProjected = projection(point1, CamDistance)
    
        scale = Scale(point1[2], CamDistance)
        
        pygame.draw.circle(window, color, (XProjected, YProjected), scale)
        
        pygame.display.flip()
                
        if not changed:
            break
            
        
        """
        print(point1)
        print(point2)
        print()
        """
        
    #pygame.display.flip()
    
if __name__ == "__main__":
    from Main import main
    
    main()