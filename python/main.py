from MOTOR import MOTOR
import keyboard


try:
    motor1 = MOTOR(port=1)
    motor2 = MOTOR(port=2)
    STEP = 200
    DELAY = 0.00005

    while True:
        if (keyboard.read_key() == "w"):
            motor2.turnStep(dir='L', steps=STEP, stepdelay=DELAY)
        elif (keyboard.read_key() == "s"):
            motor2.turnStep(dir='R', steps=STEP, stepdelay=DELAY)
        elif (keyboard.read_key() == "a"):
            motor1.turnStep(dir='L', steps=STEP, stepdelay=DELAY)
        elif (keyboard.read_key() == "d"):
            motor1.turnStep(dir='R', steps=STEP, stepdelay=DELAY)
        elif (keyboard.read_key() == "q"):
            exit()
        motor1.stop()
        motor2.stop()

except:
    print("\nMotor stop")
    motor1.stop()
    motor2.stop()
    exit()