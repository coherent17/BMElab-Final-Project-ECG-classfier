#google drive api package
from __future__ import print_function
import httplib2
import os, io

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
import auth

#Rpi API
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time
import sys
import csv
from tqdm import tqdm, trange

SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.getCredentials()

http = credentials.authorize(httplib2.Http())
drive_service = discovery.build('drive', 'v3', http=http)

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

def uploadFile(filename,filepath,mimetype):
    file_metadata = {'name': filename}
    media = MediaFileUpload(filepath,
                            mimetype=mimetype)
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print('File ID: %s' % file.get('id'))


if __name__ == '__main__':
  readData(duration = 1000)
  uploadFile('ecg_signal.csv','ecg_signal.csv','excel/csv')