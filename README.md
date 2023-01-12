# BMElab-Final-Project-ECG-classfier

## Referencce thesis:
https://link.springer.com/article/10.1007/s11760-018-1351-4

## Raspberry pi ADC pin connection (MCP3008):
https://www.hackster.io/talofer99/analog-input-on-raspberry-pi-with-mcp3008-e64e43
https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi?view=all
https://atceiling.blogspot.com/2014/04/raspberry-pi-mcp3008.html


## Dataset:
Dataset encoding:

*   0: Coherent
*   1: Daniel
*   2: Maria

## How to use this project:

*   1. Create your own google drive api
*   2. git clone https://github.com/coherent17/BMElab-Final-Project-ECG-classfier
*   3. cd BMElab-Final-Project-ECG-classfier
*   4. read ecg signal $ python3 readData.py
*   5. upload ecg.csv to google cloud
*   6. using model in Model folder to predict the result from ecg_signal.csv
*   7. The model will output the predict result and confidence in result.csv file download it and put it in this folder
*   8. run PredictResult.py to output the result (LED shine and messagebox shown)