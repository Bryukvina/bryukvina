import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2 ** bits
maxVoltage = 3.3
comp = 
troyka = 17


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def num2dac(value):
    signal = decimal2binary(value)
    GRIO.output(dac, signal)
    return signal

def adc():
    fv = 256    
    for value in range(256):
        signal = num2dac(value)
        compValue = GPIO.input(comp)
        if comp == 1:
            fv = min(fv, value)
        time.sleep(0.01)
    return fv

try:
    while True:
        value = adc()
        voltage = value / levels * maxVoltage
        print("ADC value: {:^3}, input Voltage = {:.2f}".format(value, voltage))
except KeyboardInterrupt:
    print("The program was stopped by the keyboard")
else:
    pass
finally:
    p.stop()
    GPIO.cleanup(channal)
    print("GPIO cleanup complited")
