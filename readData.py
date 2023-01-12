import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time
import sys
import csv
from tqdm import tqdm, trange

def readData(duration = 1000):
  spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
  cs = digitalio.DigitalInOut(board.D22)
  mcp = MCP.MCP3008(spi, cs)
  chan = AnalogIn(mcp, MCP.P0)

  ecg_signal = []

  for i in trange(duration):
    ecg_signal.append(float(str(chan.voltage)))
    time.sleep(0.01)

  print(ecg_signal)

  #write the ecg signal data to file
  filename = 'ecg_signal.csv'
  with open(filename, 'w') as csvfile:
      csvwriter = csv.writer(csvfile)
      csvwriter.writerow(ecg_signal)

if __name__ == '__main__':
  readData(duration = 1000)