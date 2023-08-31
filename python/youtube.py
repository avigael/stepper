from time import sleep
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

GPIO.output(12, 0)
GPIO.output(4, 0)

MotorDir = ['forward', 'backward']

class DRV8825():
    def __init__(self, dir_pin, step_pin, enable_pin):
        print(dir_pin, step_pin, enable_pin)
        self.dir_pin = dir_pin
        self.step_pin = step_pin
        self.enable_pin = enable_pin

    def digital_write(self, pin, value):
        GPIO.output(pin, value)

    def stop(self):
        self.digital_write(self.enable_pin, 1)
    
    def turnStep(self, dir, steps, stepDelay=0.005):
        if (dir == MotorDir[0]):
            print('forward')
            self.digital_write(self.enable_pin, 0)
            self.digital_write(self.dir_pin, 0)
        elif (dir == MotorDir[1]):
            print('backward')
            self.digital_write(self.enable_pin, 0)
            self.digital_write(self.dir_pin, 1)
        else:
            print('error 0')
            self.digital_write(self.enable_pin, 1)
            return
        
        if (steps == 0):
            return

        print('turn step:', steps)
        for i in range(steps):
            self.digital_write(self.step_pin, 1)
            sleep(stepDelay)
            self.digital_write(self.step_pin, 0)
            sleep(stepDelay)

Motor1 = DRV8825(13, 19, 12)
Motor2 = DRV8825(24, 18, 4)

test = 12800
Motor1.turnStep('forward', test, 1/test)
sleep(0.5)
Motor1.turnStep('backward', test, 1/test)
Motor1.stop()

GPIO.output(12,0)
GPIO.output(4,0)
GPIO.cleanup()