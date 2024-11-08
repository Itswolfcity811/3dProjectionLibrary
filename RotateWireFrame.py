"""
RotateWireFrame

Description:
"""
import math

def FindCenter(inputs):        
    """ Find the centre of the wireframe. """
    num_nodes = len(inputs)
    meanX = sum([node[0] for node in inputs]) / num_nodes
    meanY = sum([node[1] for node in inputs]) / num_nodes
    meanZ = sum([node[2] for node in inputs]) / num_nodes
    
    return (meanX, meanY, meanZ)

def rotateZ(box1, radians):    
    (cx1, cy1, cz1) = FindCenter(box1)
    
    for node in box1:
        x      = node[0] - cx1
        y      = node[1] - cy1
        d      = math.hypot(y, x)
        theta  = math.atan2(y, x) + radians
        node[0] = cx1 + d * math.cos(theta)
        node[1] = cy1 + d * math.sin(theta)
    
    return box1

def rotateX(box1, radians):
    (cx1, cy1, cz1) = FindCenter(box1)
    
    for node in box1:
        y      = node[1] - cy1
        z      = node[2] - cz1
        d      = math.hypot(y, z)
        theta  = math.atan2(y, z) + radians
        node[2] = cz1 + d * math.cos(theta)
        node[1] = cy1 + d * math.sin(theta)
    
    return box1

def rotateY(box1, (cx1, cy1, cz1), radians):
    (cx1, cy1, cz1) = FindCenter(box1)
    
    for node in box1:
        x      = node[0] - cx1
        z      = node[2] - cz1
        d      = math.hypot(x, z)
        theta  = math.atan2(x, z) + radians
        node[2] = round(cz1 + d * math.cos(theta))
        node[0] = round(cx1 + d * math.sin(theta))
             
    return box1

if __name__ == "__main__":
    from Main import main
    
    main()