import numpy as np
import matplotlib.pyplot as plt
import time
import RPi.GPIO as GPIO



measured_data = [1, 2, 3, 4, 5, 6, 7, 8]
plt.plot(measured_data)  #Вывод значений на графике
plt.show()


measured_data_str = "\n".join(map(str, measured_data))
with open("something.txt", "w") as file:
    f.write(measure_data_str)

