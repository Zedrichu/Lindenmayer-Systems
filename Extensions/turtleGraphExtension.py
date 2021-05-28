# -*- coding: utf-8 -*-


import numpy as np
import math 
import displayMenuExtension as displayUI
def turtleGraph(LindenmayerString,N,System):
    """
    Provides commands for creating the graph for a Lindenmayer system
    
    ---------------
    Parameters:
        LindenmayerString - string
                contains the series of characters 
        N - integer
            number of iterations
    ---------------
    Returns:
        turtleCommands - string
            contains the series of lengths and angles 
    

    @author: Adrian Zvizdenco & Felix Aertebjerg & Emilie Hansen
    """
    #Vector of lengths and angles
    turtleCommands = np.array([])
    
    if (System == 'Koch Curve'):
        lg = (1/3)**N
        #Linking the string to plotting commands
        for char in LindenmayerString:
            #Move forward
            if (char == 'S'):
                turtleCommands = np.append(turtleCommands,lg)
            #Turn right
            elif (char == 'R'):
                turtleCommands = np.append(turtleCommands,-2*math.pi/3)
            #Turn left
            elif (char == 'L'):
                turtleCommands = np.append(turtleCommands,math.pi/3)
        if len(turtleCommands)==1:
            turtleCommands = np.append(turtleCommands,0)
    
    elif (System == 'Sierpinski Triangle'):
        lg = (1/2)**N
        #Linking the string to plotting commands
        for char in LindenmayerString:
            #Move forward
            if (char == 'A' or char == 'B'):
                turtleCommands = np.append(turtleCommands,lg)
            #Turn left
            elif (char == 'L'):
                turtleCommands = np.append(turtleCommands,math.pi/3)
            #Turn right
            elif (char == 'R'):
                turtleCommands = np.append(turtleCommands,-math.pi/3)
        if len(turtleCommands)==1:
            turtleCommands = np.append(turtleCommands,0)
                
    elif (System == 'Koch Curve(User-defined)'):
        lg = (1/3)**N
        #Ask user for a specific angle
        ang = displayUI.inputAngle("Please enter an angle between 0-90 degrees: ")
        ang = math.pi*ang/180
        
        #Linking the string to plotting commands
        for char in LindenmayerString:
            #Move forward
            if (char == 'F'):
                turtleCommands = np.append(turtleCommands,lg)
            #Turn right
            elif (char == 'R'):
                turtleCommands = np.append(turtleCommands,-ang)
            #Turn left
            elif (char == 'L'):
                turtleCommands = np.append(turtleCommands,ang)
        if len(turtleCommands)==1:
            turtleCommands = np.append(turtleCommands,0)
                
                
    return turtleCommands

