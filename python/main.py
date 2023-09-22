import RPi.GPIO as GPIO
import time
from MOTOR import MOTOR


try:
    motor1 = MOTOR(port=1)
    motor2 = MOTOR(port=2)
    STEP = 200
    DELAY = 0.0005

    while True:
        print('Enter command:')
        command = input()
        if (command == "w"):
            motor2.turnStep(dir='L', steps=STEP, stepdelay=DELAY)
        elif (command == "s"):
            motor2.turnStep(dir='R', steps=STEP, stepdelay=DELAY)
        elif (command == "a"):
            motor1.turnStep(dir='L', steps=STEP, stepdelay=DELAY)
        elif (command == "d"):
            motor1.turnStep(dir='R', steps=STEP, stepdelay=DELAY)
        elif (command == "q"):
            exit()

except:
    print("\nMotor stop")
    motor1.stop()
    motor2.stop()
    exit()