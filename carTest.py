from motor import *
from servo import *

from pynput import keyboard


# -1 = left
# 0 = center
# 1 = right


try:
    print("testing")    

except:
    cleanMotor()
    cleanServo()
    
def on_press(key):
    if key.char == 'w':
        forward(100)
        
    if key.char == 's':
        reverse(100)
        
    if key.char == 'a':
        turn(-1, 100)
        
    if key.char == 'd':
        turn(1, 100)

    if key.char == 'p':
        cleanMotor()
        cleanServo()
        return False
        
def on_release(key):
    if key.char == 'w' or key.char == 's':
        stopMotor() #stops the motor
        
    if key.char == 'a' or key.char == 'd':
        turn(0, 0) #sets to center
    

    
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


