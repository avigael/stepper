import RPi.GPIO as GPIO
import time

class MOTOR():
    def __init__(self, port: int):
        if (port == 1):
            self.dir_pin = 13
            self.step_pin = 19        
            self.enable_pin = 12
            self.mode_pins = (16,17,20)
        elif (port == 2):
            self.dir_pin = 24
            self.step_pin = 18        
            self.enable_pin = 4
            self.mode_pins = (21,22,27)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.dir_pin, GPIO.OUT)
        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.setup(self.enable_pin, GPIO.OUT)
        GPIO.setup(self.mode_pins, GPIO.OUT)
        self.digital_write(self.mode_pins, [(0, 0, 0)])
        
    def digital_write(self, pin, value):
        GPIO.output(pin, value)
        
    def stop(self):
        self.digital_write(self.enable_pin, 0)

        
    def turnStep(self, dir, steps, stepdelay=0.005):
        if (dir == "L"):
            print("forward")
            self.digital_write(self.enable_pin, 1)
            self.digital_write(self.dir_pin, 0)
        elif (dir == "R"):
            print("backward")
            self.digital_write(self.enable_pin, 1)
            self.digital_write(self.dir_pin, 1)
        else:
            print("the dir must be : 'L' or 'R'")
            self.digital_write(self.enable_pin, 0)
            return

        if (steps == 0):
            return
            
        print("turn step:",steps)
        for i in range(steps):
            self.digital_write(self.step_pin, True)
            time.sleep(stepdelay)
            self.digital_write(self.step_pin, False)
            time.sleep(stepdelay)
