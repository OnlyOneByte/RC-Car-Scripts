# Written by Angelo Yang for use with RC CAR
# This code is in python to use the raspberry pi

import time
import pigpio 

#
# Middle = 1400
# range = 500 - 2500
# actual range: 1100 - 1700
# 1100 = hard right
# 1700 = hard left
#
# USES PIN 18 (goes to signal wire on servo)

SERVO = 18

#These are the PWM values for each of these things
mid=1400

#How long the PWM signal has to be kept up for until it is done

delta=300

currentPulsewidth = mid

pi = pigpio.pi()

debugging = True

def setPulsewidth(x):
    currentPulsewidth=x
    pi.set_servo_pulsewidth(SERVO, currentPulsewidth)
    if(debugging):
        print("set PWM to: ", x)

#Dir is direction. -1 = left, 1 = right.
# if 0 is given, the percent value is ignored (center)
# percent is value from 1-100.
def turn(dir, percent):
    if(dir == 0): #middle
        setPulsewidth(mid)
        return
    if(percent > 100) or (percent < 1):
        raise ValueError("Expecting % Value between 1 and 100, not ", percent)
    if(dir == 1): #right
        setPulsewidth(mid - delta * (percent/100.0))
        return
    if(dir == -1): #left
        setPulsewidth(mid + delta * (percent/100.0))
        return
    
    raise ValueError('Expecting dir to be -1, 0, or 1, not ', dir)
    
def cleanServo():
    pi.stop()
    