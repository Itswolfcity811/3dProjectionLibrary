"""
Projections

Description:
"""
#https://infogalactic.com/info/3D_projection

from math import sin, cos
import pygame
pygame.init()

def OrthographicProjection(VertexPoint, FocalLength):
    XProjected = round(FocalLength * VertexPoint[0] / FocalLength + VertexPoint[2])
    
    YProjected = round(FocalLength * VertexPoint[1] / FocalLength + VertexPoint[2])
    
    return XProjected, YProjected

def PerspectiveProjection(VertexPoint, FocalLength, CamAngle=[0, 0, 0]):
    a = VertexPoint
    cam = [0, 0, FocalLength]
    
    s = sin(0)
    c = cos(0)
    
    o = CamAngle
        
    x, y, z = a[0] - cam[0], a[1] - cam[1], a[2] - cam[2]
    
    x = abs(x)
    y = abs(y)
    z = abs(z)
    
    c = lambda i : cos(o[i])
    s = lambda i : sin(o[i])
    
    d = [0.0, 0.0, 0.0]
    
    d[0] = c(1) * (s(2) * y + c(2) * x) - s(1) * z
    d[1] = s(0) * (c(1) * z + s(1) * (s(2) * y + c(2) * x)) + c(0) * (c(2) * y - s(2) * x)
    d[2] = c(0) * (c(1) * z + s(1) * (s(2) * y + c(2) * x)) - s(0) * (c(2) * y - s(2) * x)
    
    debug = False
    if debug:
        print("VertexPoint: " + str(a))
        print("FocalLength: " + str(FocalLength))
        print("CamAngle: " + str(CamAngle))
        print("x, y, z", x, y, z)
        print("PreProjection: " + str(d))
    
    b = [0.0, 0.0]
    
    e = []
    
    b[0] = (cam[2] / d[2] * d[0] - cam[0])
    b[1] = (cam[2] / d[2] * d[1] - cam[1])
    
    if debug:
        print("Out: " + str(b))
        print()
        pygame.time.wait(100)
    """
    print("cam: " + str(cam))
    print("d: " + str(d))
    print("b: " + str(b))
    print()
    """
    
    return b[0], b[1]
    
if __name__ == "__main__":
    from Main import main
    
    main()