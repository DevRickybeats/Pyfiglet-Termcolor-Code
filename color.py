import pyfiglet
from termcolor import colored




def color_style(msg,color):
    valid_colors= ("grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white")
    
    if color not in valid_colors:
        color = 'cyan'
    otp = pyfiglet.figlet_format(msg)
    coloredotp = colored(otp, color , attrs=['blink'])
    print(coloredotp) 


msg =input("What would you like to print? ")
color = input('Pick a color\t: ')

color_style(msg,color)