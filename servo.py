import time
import pigpio 

#
# Middle = 1400
# range = 500 - 2500
# actual range: 1100 - 1700
# 1000 = hard right
# 1800 = hard left
# COOL

SERVO = 18
mid = 1400

currentPulsewidth = mid

pi = pigpio.pi()

def setPulsewidth(x):
    currentPulsewidth=x
    pi.set_servo_pulsewidth(SERVO, currentPulsewidth)



