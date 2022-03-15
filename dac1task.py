import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2 ** bits
Max_voltage = 3.3

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def bin2dac(value):
    signal =decimal2binary(value)
    GPIO.output(dac, signal)
    return signal



GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

try:
    while True:
        inputstr = input("Please, enter a valur between 0 and 255 ('q' to exit) > ")

        if inputstr.isdigit():
            value = int(inputstr)

            if value >= levels:
                print("The value is too large, please, try again")
                continue
        
            signal = bin2dac(value)
            voltage = value / levels * Max_voltage
            print("Entered value = {:^3} -> {}, output voltage = {:.2f}".format(value, signal, voltage))

        elif inputstr == "q":
            break

        else:
            print("Enter a positive integer")
            continue
except KeyboardInterrupt:
    print("The program was stopped by the keyboard")
else:
    pass
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup complited")