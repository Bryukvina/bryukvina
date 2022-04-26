import numpy as np
import matplotlib.pyplot as plt
import time
import RPi.GPIO as GPIO

#Настройка портов вывода
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
bits = len(dac)
levels = 2 ** bits
maxVoltage = 3.3
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)


def num2dac(value):
    signal = [int(bit) for bit in bin(value)[2:].zfill(bits)]
    GPIO.output(dac, signal)
    return signal

def adc():
    left = 0
    right = 256
    while right - left > 1:
        middle = (right + left) // 2
        num2dac(middle)
        time.sleep(0.01)
        if GPIO.input(comp) == 1:
            left = middle
        else:
            right = middle
    i = int(left / levels * len(leds))
    GPIO.output(leds[i % len(leds):], 1)
    return left / levels * maxVoltage


try:
    new_measures = []
    start_time = time.time()
    GPIO.output(troyka, 1)
    voltage = adc()
    while voltage < 0.97 * 3.3:
        new_measures.append(voltage)
        voltage = adc()
    GPIO.output(troyka, 0)
    voltage = adc()
    while voltage >= 0.02 * 3.3:
        new_measures.append(voltage)
        voltage = adc()
    finish_time = time.time()
    experiment_len = finish_time - start_time
    plt.plot(new_measures)  #Вывод значений на графике
    file = open("data.txt", "w")
    file.write("\n".join(map(str, new_measures)))
    samp_freq = (experiment_len / len(new_measures))
    quan_step = (max(new_measures) - min(new_measures)) / len(new_measures)
    file1 = open("settings.txt", "w")
    file1.write(samp_freq, quan_step)
    print("Time of experiment: {:.2f}, Period of measure: {:.2f}, Sampling frequancy: {:.2f}, quantization step = {:.2f}".format(experiment_len, 1/samp_freq, samp_freq, quan_step))


    plt.show()
