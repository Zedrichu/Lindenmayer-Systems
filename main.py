# -*- coding: utf-8 -*-

"""
    Lindenmayer Systems Project.

    The main script of the project.
    The user interface is created here.
    Functionalities are located in the Extensions folder and imported in 
        the main script.
    
    
    HAVE FUN!
    
    @author: Adrian Zvizdenco & Felix Aertebjerg & Emilie Hansen 
"""
#Initialization of path and imports
import sys
sys.path.append('.')
sys.path.append('./Extensions')

import displayMenuExtension as displayUI
import LindenmayerIterationExtension as liter
from turtleGraphExtension import *
from turtlePlotExtension import * 

print("Welcome to Lindenmayer Systems! ")

menuItems = np.array([
    'Choose the type of Lindenmayer system and the number of iterations',
                      'Generate Plots','Quit'])
while True:
    choice = displayUI.displayMenu(menuItems)
    if choice == 1:
        print('Initialisation procedure...')
        print('------------------------------')
        
          #Asking user for system type and number of iterations
        System,sysnum = displayUI.inputSystem(
            "Please choose a Lindenmayer system! ")
        if (sysnum == 1):
            xy = 10
        elif (sysnum == 2):
            xy = 10
        elif (sysnum == 3):
            xy = 7
            
        N = displayUI.inputRI(
            "Please choose number of iterations (below {}):".format(xy),xy)
        
        #Obtaining the string after N iterations
        LindenString = liter.LindIter(System,N)        
        
        print ("Data loaded successfully. \n")
        print (
        "Lindenmayer system:{} for {} iterations is ready!".format(System,N))
        print ('________________________________________')
                
        while True:
            choice = displayUI.displayMenu(menuItems)
            if choice == 1:
                print ("Reinitialisation procedure...")
                print ("----------------------------")
                
                #Asking user for system type and number of iterations
                System,sysnum = displayUI.inputSystem(
                    "Please choose a Lindenmayer system! ")
                if (sysnum == 1):
                    xy = 10
                elif (sysnum == 2):
                    xy = 10
                elif (sysnum == 3):
                    xy = 7
            
                N = displayUI.inputRI(
                    "Please choose number of iterations (below {}):"
                                  .format(xy),xy)
                #Obtaining the string after N iterations
                LindenString = liter.LindIter(System,N)        
                
                print ("Data reloaded successfully. \n")
                print (
        "Lindenmayer system:{} for {} iterations is ready!".format(System,N))
                print ('________________________________________')
                
            elif choice == 2:
                print ("Generating the plots....")
                print ("-----------------------")
                
                #Generating Plots
                turtleCommands = turtleGraph(LindenString,N,System)
                turtlePlot(
                    "{} for {} iterations"
                    .format(System,N),turtleCommands)
                
                print ("Plots generated successfully ")
                print ("_______________________________________")
            
            elif  choice == 3:
                print("Quitting the program.")
                print('_______________________________________')
                print("Thanks for using the program!")
                break
        break
        
    elif choice == 3:
        print("Quitting the program.")
        print('__________________________________')
        print("Thanks for using the program!")
        break
    
    else:
        print(
    "Error : No Lindenmayer Initialisation. Please choose option 1 or quit! ")
        print()