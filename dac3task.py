import RPi.GPIO as GPIO


channal = 23
Max_voltage = 3.3


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
p = GPIO.PWM(channal, 1000)
p.start(0)
try:
    
    while True:
        inputstr = input("Please, enter a valur between 0 and 100 ('q' to exit) > ")

        if inputstr.isdigit():
            value = float(inputstr)

            if value >= 101:
                print("The value is too large, please, try again")
                continue

            p.ChangeDutyCycle(value)
            print("Entered value =", value, "%")

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
    p.stop()
    GPIO.cleanup(channal)
    print("GPIO cleanup complited")