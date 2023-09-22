from MOTOR import MOTOR
import keyboard


try:
    motor1 = MOTOR(port=1)
    motor2 = MOTOR(port=2)
    STEP = 200
    DELAY = 0.00005

    while True:
        if (keyboard.is_pressed() == "w"):
            motor2.turnStep(dir='L', steps=STEP, stepdelay=DELAY)
        elif (keyboard.is_pressed() == "s"):
            motor2.turnStep(dir='R', steps=STEP, stepdelay=DELAY)
        elif (keyboard.is_pressed() == "a"):
            motor1.turnStep(dir='L', steps=STEP, stepdelay=DELAY)
        elif (keyboard.is_pressed() == "d"):
            motor1.turnStep(dir='R', steps=STEP, stepdelay=DELAY)
        elif (keyboard.is_pressed() == "q"):
            exit()

except:
    print("\nMotor stop")
    motor1.stop()
    motor2.stop()
    exit()