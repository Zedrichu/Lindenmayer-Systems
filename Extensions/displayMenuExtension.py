# -*- coding: utf-8 -*-
"""
Extension with UI Utilities for the main script

"""

#Source code found in the python modules book and used as extension

"""
INPUTNUMBER Prompts user to input a number

Usage: num = inputNumber(prompt) Displays prompt and asks user to input a
 number. Repeats until user inputs a valid number.

Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015

---------------------------------------------------------------------------

DISPLAYMENU Displays a menu of options, ask the user to choose an item
 and returns the number of the menu item chosen.

Usage: choice = displayMenu(options)

Input options Menu options (array of strings)
Output choice Chosen option (integer)

Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015

"""
#Source code **********
import numpy as np

def inputNumber(prompt):
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("Error: Please enter a number as your choice")
            print()
            pass
    return num


def displayMenu(options):
    
    print("Menu: ")
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1,options[i]))
    
    choice = 0
    
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose a menu item: ")
        print()
    return choice 
#******************
    
#Other functions created for the interface 

def inputRI(prompt,pvt):
    """
    The function acts as error handling for the number of iterations
    It must be an integer and reasonable from a resource perspective
    Parameters:
        prompt -string 
                message to be displayed
        pvt - integer 
                the limit number of iterations defined in main script
    Returns:
        num - integer
            reasonable number of iterations
            
    Changes made by Zvizdenco Adrian
    """
    while True:
        try:
            num = int(input(prompt))
            if (num<0 or num>=pvt):
                raise ValueError
            break
        except ValueError:
            print("Error: Please input a reasonable number of iterations")
            print("Consider computational time as an expensive resource")
            print()
            pass
    return num

def inputSystem(prompt):
    """
    Provides error handling for obtaining the system type
    
    Parameters:
        prompt - string
                message to be displayed
    ------------
    Returns:
        system - string
                the type of Lindenmayer system selected
    @author: Adrian Zvizdenco 
    """
    menuItems = np.array(['Koch Curve','Sierpinski Triangle',
                          'Koch Curve(User-defined)'])
    
    print(prompt)
    print("-----------------------------")
    choice = displayMenu(menuItems)
    system = menuItems[choice-1]
    return (system,choice)

def inputAngle(prompt):
    """
    Provides error handling for obtaining the angle
    
    Parameters:
        prompt - string
                message to be displayed
    ------------
    Returns:
        angle - string
                the type of Lindenmayer system selected
    @author: Adrian Zvizdenco 
    """
    
    while True:
        try:
            angle = float(input(prompt))
            if (angle<0 or angle>90):
                raise ValueError
            break
        except ValueError:
            print("Error: Please enter a valid angle between 0-90 degrees: ")
            print()
            pass
    return angle
    