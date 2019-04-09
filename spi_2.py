import time
import board
import busio
import digitalio

import tempprueba

import os
from time import sleep

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Initialize SPI bus and sensor.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D26)  
sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=100, ref_resistor=430.0, wires=3)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 1
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

while True:
    
    value = mcp.read_adc(1)
    
    # Read temperature.
    temp = sensor.temperature
    print(temp)
    print(value)
    print()
    time.sleep(2)