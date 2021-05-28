# -*- coding: utf-8 -*-

def LindIter(System,N):
    """
    Provides a number of iterations through a selected Lindenmayer system
    
    ---------------
    Parameters:
        System - string
                selected Lindenmayer system
        N - integer
            number of iterations
    ---------------
    Returns:
        LindenmayerString - string
            contains the series of characters for generating further commands 
    

    @author: Adrian Zvizdenco & Felix Aertebjerg & Emilie Hansen
    """

    if (System == 'Koch Curve'):
        #Axiom string
        LStr = 'S'
        #Dislocation rule
        disS = 'SLSRSLS'
        #Iterating through N orders
        for i in range(N):
            k=0
            #Expanding string according to rules
            for j in range(len(LStr)):
                
                if (j+k >= len(LStr)):
                    break
                if (LStr[j+k] == 'S'):
                    LStr = LStr[:j+k] + disS + LStr[j+k+1:]
                    k+=len(disS)-1

    elif (System == 'Sierpinski Triangle'):
        #Axiom string
        LStr = 'A'
        #Dislocation rules 
        disA = 'BRARB'
        disB = 'ALBLA'
        #Iterating through N orders
        for i in range(N):
            k=0
            #Expanding string according to rules
            for j in range(len(LStr)):
                if (j+k >= len(LStr)):
                    break
                if (LStr[j+k] == 'A'):
                    LStr = LStr[:j+k] + disA + LStr[j+k+1:]
                    k+=len(disA)-1
                elif (LStr[j+k]=='B'):
                    LStr = LStr[:j+k] + disB + LStr[j+k+1:]
                    k+=len(disB)-1
    
    elif (System == 'Koch Curve(User-defined)'):
        #Axiom string
        LStr = 'F'
        #Dislocation rule
        disF = 'FLFRFRFLF'
        #Iterating through N orders
        for i in range(N):
            k=0
            #Expanding string according to rules
            for j in range(len(LStr)):
                
                if (j+k >= len(LStr)):
                    break
                if (LStr[j+k] == 'F'):
                    LStr = LStr[:j+k] + disF + LStr[j+k+1:]
                    k+=len(disF)-1
                    
    LindenmayerString = LStr
    return LindenmayerString
