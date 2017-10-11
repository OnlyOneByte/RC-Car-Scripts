# Written by Angelo Yang for use with RC CAR
# This code is in python to use the raspberry pi
# GPIO pins to run a motor off of a L298D board
# also includes speed control

# USES PINS 37, 38, 39, and 40
# AKA GPIO26, GPIO20, GND(39), and GPIO21
import sys
import time
import RPi.GPIO as GPIO

# CONNECTIONS FROM PI TO L298 MOTOR BOARD
#
# GPIO 21 (p40) to ENB
# GPIO 20 (p38) to IN3
# GPIO 26 (p37) to IN4
# GND (p39) to common ground.
#
# MAX FREQ is 300 HZ
# Initial speed is 50% Duty cycle.
#
# PLEASE BE KIND TO THE MOTOR
# ALWAYS STOP MOTOR BEFORE CHANGING DIRECTIONS
#

Forward=26
Backward=20
speed=21
sleeptime=0.01 # this is the time between motor changes.

debugging = True #will print debugging messages if set to true
currentSpeed = 50 #speed = %. 100 is max, 0 is nonee
direction = 0 #0 is not moving. 1 is forward, -1 is backwards.

mode=GPIO.getmode()
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)
GPIO.setup(speed, GPIO.OUT)

pwm = GPIO.PWM(speed, 300)
pwm.start(50)

#for debugging purposes
def reset():
    mode=GPIO.getmode()
    GPIO.cleanup()

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Forward, GPIO.OUT)
    GPIO.setup(Backward, GPIO.OUT)
    GPIO.setup(speed, GPIO.OUT)

    pwm = GPIO.PWM(speed, 300)
    pwm.start(50)

#moves forward at speed x.
def forward(x):
    #sets the speed
    setSpeed(x)
    
    #if the motor was going backwards before, it lets the motor rest before running the other direction
    if(direction == -1):
        stopMotor()
        time.sleep(sleeptime)
        
    #turns up the output to make the motor move forward.
    GPIO.output(Forward, GPIO.HIGH)
    
    if(debugging):
        print("Moving forward at ", currentSpeed, "% speed")


#moves backwards at speed x
def reverse(x):
    #sets the speed
    setSpeed(x)
    
    #if the motor was going forwards before, it lets the motor rest before running the other direction
    if(direction == 1):
        stopMotor()
        time.sleep(sleeptime)
    
    #turns the output HIGH for the backwards pin
    GPIO.output(Backward, GPIO.HIGH)
    
    if(debugging):
        print("Moving backward at ", currentSpeed, "% speed")

#Stops the motor.
def stopMotor():
    GPIO.output(Backward, GPIO.LOW)        
    GPIO.output(Forward, GPIO.LOW)
    
    if(debugging):
        print("Stopped the motor")

#sets the speed
def setSpeed(x):
    pwm.ChangeDutyCycle(x)
    currentSpeed = x;

#returns the speed.
def getSpeed():
    return currentSpeed;
