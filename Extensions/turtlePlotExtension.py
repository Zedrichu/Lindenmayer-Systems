# -*- coding: utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt
from math import sin,cos


def turtlePlot(prompt,turtleCommands):
    """
    Creates the plots according to the commands entered
    
    ---------------
    Parameters:
        prompt - string
                text displayed as legend
        turtleCommands - array
                        contains pairs of lengths and angles
    ---------------

    @author: Adrian Zvizdenco & Felix Aertebjerg & Emilie Hansen
    """
    #Vector containing directions
    d = []
    #Vector containing points to be plotted
    p = []
    #Initialised direction with paired x and y
    d.append([1,0])
    #Initialised starting point (pair of x and y )
    p.append([0,0])
    #Length of the entire graph
    lengrp = len(turtleCommands) // 2 *  turtleCommands[0]
    
    #Generating future points and directions
    for i in range(len(turtleCommands)//2):
        #Angle
        ang = turtleCommands[2*i+1]
        #Length
        lgt = turtleCommands[2*i]
        
        d.append((cos(ang)*d[i][0]-sin(ang)*d[i][1],
                  sin(ang)*d[i][0]+cos(ang)*d[i][1]))    
        
        p.append((p[i][0]+lgt*d[i][0],p[i][1]+lgt*d[i][1]))
    #Ending point
    
    # p.append([1,0])
    p = np.array(p)
    
    #X-coordinates found
    x = p[:,0]
    #Y-coordinates found
    y = p[:,1]
    
    #Plotting system graphics
    
    plt.plot(x,y,c='red',label=prompt)
    plt.title("Lindenmayer System Graphics")
    plt.xlabel("x-coordinates")
    plt.ylabel("y-coordinates")
    plt.legend(loc="best")
    plt.show()
    #Displaying curve length   
    print("The curve length of the system is {}".format(lengrp))
    print()
