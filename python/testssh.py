from sshkeyboard import listen_keyboard
from MOTOR import MOTOR

motor1 = MOTOR(port=1)
motor2 = MOTOR(port=2)
STEP = 200
DELAY = 0.0005

def press(command):
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
def release(command):
        if (command == "w"):
            motor2.stop()
        elif (command == "s"):
            motor2.stop()
        elif (command == "a"):
            motor1.stop()
        elif (command == "d"):
            motor1.stop();
listen_keyboard(on_press=press,on_release=release)