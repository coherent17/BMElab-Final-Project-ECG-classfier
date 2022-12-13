import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time
import sys
import csv

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D22)
 
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
 
# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

ecg_signal = []

while len(ecg_signal) < 500:
  #print('Raw ADC Value: ', chan.value)
  #print('ADC Voltage: ' + str(chan.voltage) + 'V')
  ecg_signal.append(float(str(chan.voltage)))
  time.sleep(0.01)

print(ecg_signal)

#write the ecg signal data to file
filename = 'ecg_signal.csv'
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(ecg_signal)