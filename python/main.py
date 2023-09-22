import RPi.GPIO as GPIO
import time
from MOTOR import MOTOR


try:
    motor1 = MOTOR(port=1)
    motor2 = MOTOR(port=2)
    motor1.turnStep(dir='L', steps=200, stepdelay = 0.005)
    time.sleep(0.5)
    motor1.turnStep(dir='R', steps=400, stepdelay = 0.005)
    motor1.stop()

    while True:
        print('Enter command:')
        command = input()
        if (command == "w"):
            motor2.turnStep(dir='L', steps=200)
        elif (command == "s"):
            motor2.turnStep(dir='R', steps=200)
        elif (command == "a"):
            motor1.turnStep(dir='L', steps=200)
        elif (command == "d"):
            motor1.turnStep(dir='R', steps=200)
        else:
            exit()
        motor1.stop()
        motor2.stop()

except:
    print("\nMotor stop")
    motor1.stop()
    motor2.stop()
    exit()