"""
Scale

Description:
"""
#Logical Regresion
def Scale1(z):
    e = 2.718
    return round(139.5 / (1 + 0.3845 * (e ** (0.02316 * z))))

#Slope Intercept
def Scale(z, CamDistance):
    #return 15
    z += CamDistance
    r = round(-0.085 * z) + 50
    #print(r)
    return r

if __name__ == "__main__":
    from Main import main
    
    main()