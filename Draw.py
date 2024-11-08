"""
Draw

Description:
"""
from Projections import OrthographicProjection, PerspectiveProjection
from RotateWireFrame import rotateX, rotateY, rotateZ
import math

try:
    from DrawLineCircle import CircleLine as CL
except:
    ""

from Scale import Scale

import pygame
pygame.init()


def DrawPoint(window, point, CamDistance, color=(255, 255, 255), projection=OrthographicProjection):
    XProjected, YProjected = projection(point, CamDistance)
    
    scale = Scale(point[2])
    
    pygame.draw.circle(window, color, (XProjected, YProjected), scale)
    return

def DrawLine(window, point1, point2, CamDistance, color=(255, 255, 255), projection=OrthographicProjection):
    CL(window, point1, point2, CamDistance, color=color, projection=projection)    
    return

def DrawSquare(window, points, CamDistance, color=(255, 255, 255), projection=OrthographicProjection):
    #DrawLine(window, points[3], points[0], CamDistance)
    #return
    
    if len(points) != 4:
        raise("Incorrect input length.")
    
    #print(points[0])
    for i in range(len(points)):
        if i == 3:
            #DrawPoint(window, points[2], CamDistance, projection=projection, color=(255, 0, 0))
            DrawLine(window, points[0], points[3], CamDistance, color, projection=projection)
        else:
            #DrawPoint(window, points[i + 1], CamDistance, projection=projection)
            DrawLine(window, points[i], points[i + 1], CamDistance, color, projection=projection)
        
def DrawCube(window, FrontTopLeftPoint, length, CamDistance, degrees=0, color=(255, 255, 255), projection=OrthographicProjection):
    p = FrontTopLeftPoint
    #length = -length
    square1 = [p[:], [p[0], p[1] + length, p[2]], [p[0] + length, p[1] + length, p[2]], [p[0] + length, p[1], p[2]]]
    
    #print(p)
    
    if degrees != 0:
        rad = degrees * math.pi / 180
        square1 = rotateX(square1, rad)
    
    if False:
        
        #print(square1)
        #DrawLine(window, square1[0], square1[1], CamDistance, color, projection)
        #"""
        #DrawPoint(window, square1[0], CamDistance, color=(255, 0, 0), projection=projection)
        #DrawPoint(window, square1[1], CamDistance, color=(0, 0, 255), projection=projection)
        #DrawPoint(window, square1[2], CamDistance, color=(255, 255, 255), projection=projection)
        #DrawPoint(window, square1[3], CamDistance, color=(0, 255, 0), projection=projection)
        #print(square1[0])
        DrawSquare(window, square1, CamDistance, color, projection)
        #"""
        return
    
    """
    for i in range(3):
        p[i] += length
    """
    p[2] += length
    
    #print(p)
    
    square2 = [p[:], [p[0], p[1] + length, p[2]], [p[0] + length, p[1] + length, p[2]], [p[0] + length, p[1], p[2]]]
    
    if degrees != 0:
        rad = degrees * math.pi / 180
        square2 = rotateX(square2, rad)
    
    if False:
        #DrawLine(window, square1[0], square1[1], CamDistance, color, projection)
        
        DrawPoint(window, square2[0], CamDistance, color=(255, 0, 0), projection=projection)
        DrawPoint(window, square2[1], CamDistance, color=(0, 0, 255), projection=projection)
        DrawPoint(window, square2[2], CamDistance, color=(255, 255, 255), projection=projection)
        DrawPoint(window, square2[3], CamDistance, color=(0, 255, 0), projection=projection)
        
        return
    
    DrawSquare(window, square1, CamDistance, color, projection=projection)
    
    DrawSquare(window, square2, CamDistance, color, projection=projection)
    
    for i in range(4):
        DrawLine(window, square1[i], square2[i], CamDistance, color, projection=projection)
    
def DrawWireFrame(window, frame, CamDistance, color=(255, 255, 255), projection=OrthographicProjection):
    for i in range(len(frame)):
        if i + 1 >= len(frame):
            ""
        else:
            DrawLine(window, frame[i], frame[i + 1], CamDistance, color, projection)

if __name__ == "__main__":
    from Main import main
    
    main()