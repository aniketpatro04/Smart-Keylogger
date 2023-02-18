from pynput.mouse import Controller
#At a single point of time, we can only control the mouse or the keyboard.


#Function to control the movement of the Mouse. 
#The top left of the screen in 0,0. So 100,200 means 100 pixels to the right and 200 pixels vertically
def controlMouse():
    mouse = Controller() 
    mouse.position = (100,200)


controlMouse()