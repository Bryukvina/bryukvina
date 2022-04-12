
import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2 ** bits
maxVoltage = 3.3
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def num2dac(value):
    signal = [int(bit) for bit in bin(value)[2:].zfill(bits)]
    GPIO.output(dac, signal)
    return signal

def adc():
    for value in range(256):
        num2dac(value)
        time.sleep(0.001)
        if GPIO.input(comp) == 0:
            return value

    return 255

try:
    while True:
        value = adc()
        voltage = value / levels * maxVoltage
        print("ADC value: {:^3}, input Voltage = {:.2f}".format(value, voltage))

finally:
    GPIO.cleanup()
    print("GPIO cleanup complited")
