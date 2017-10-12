from motor import *
from servo import *

from pynput import keyboard


# -1 = left
# 0 = center
# 1 = right


try:
    print("testing")    

except:
    stopMotor()
    stopServo()
    
def on_press(key):
    if key.char == 'w':
        forward(75)
        
    if key.char == 's':
        reverse(75)
        
    if key.char == 'a':
        turn(-1, 90)
        
    if key.char == 'd':
        turn(1, 90)

def on_release(key):
    if key.char == 'w' or key.char == 's':
        stopMotor() #stops the motor
        
    if key.char == 'a' or key.char == 'd':
        turn(0, 0) #sets to center
    

    
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


