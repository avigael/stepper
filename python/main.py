from MOTOR import MOTOR
import keyboard


try:
    motor1 = MOTOR(port=1)
    motor2 = MOTOR(port=2)
    STEP = 200
    DELAY = 0.0005

    keyboard.add_hotkey('w', lambda: motor2.turnStep(dir='L', steps=STEP, stepdelay=DELAY))
    keyboard.add_hotkey('s', lambda: motor2.turnStep(dir='R', steps=STEP, stepdelay=DELAY))
    keyboard.add_hotkey('a', lambda: motor1.turnStep(dir='L', steps=STEP, stepdelay=DELAY))
    keyboard.add_hotkey('d', lambda: motor1.turnStep(dir='R', steps=STEP, stepdelay=DELAY))

    keyboard.wait('esc')

except:
    print("\nMotor stop")
    motor1.stop()
    motor2.stop()
    exit()