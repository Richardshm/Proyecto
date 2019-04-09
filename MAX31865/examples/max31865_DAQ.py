
import time
from time import sleep
from datetime import datetime
import board
import busio
import digitalio
import os

import ada_max31865

# Initialize SPI bus and sensor.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D26)  # Chip select of the MAX31865 board.

sensor = ada_max31865.MAX31865(spi, cs, rtd_nominal=100, ref_resistor=430.0, wires=3)
i = 0
file = open("/home/pi/Proyectos/MAX31865/examples/Data Log/data_log.csv", "a")

if os.stat("/home/pi/Proyectos/MAX31865/examples/Data Log/data_log.csv").st_size == 0:
        file.write("Tiempo,Temperatura,Resistencia\n")

while True:
    temp = round(sensor.temperature, 4)
    res = round(sensor.resistance, 4)
    
    i=i+1
    tiemp = i*5
    file.write(str(tiemp)+","+str(temp)+","+str(res)+"\n")
    file.flush()
    
    print("Temperatura:",temp)
    print("Resistencia:",res)
    print()
    time.sleep(5)
    
