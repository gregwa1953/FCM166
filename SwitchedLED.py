# import RPi.GPIO as GPIO
import RTk.GPIO as GPIO

# It looks like the RTK library only supports
# the BCM GPIO pin numbers
# If you are using the BCM GPIO pin numbers...
LedPin = 18
BtnPin = 17
# Otherwise the physical board numbers...
# LedPin = 12
# BtnPin = 11


def setup():
    GPIO.setmode(GPIO.BCM)
    # GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def loop():
    while True:
        if GPIO.input(BtnPin) == GPIO.LOW:
            print("...LED On")
            GPIO.output(LedPin, GPIO.LOW)
        else:
            print("...LED Off")
            GPIO.output(LedPin, GPIO.HIGH)


def destroy():
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()


if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
