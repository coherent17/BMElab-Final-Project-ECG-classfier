import tkinter as tk
import csv
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
LED_Coherent = 17
LED_Daniel = 18
LED_Mariia = 22
LED_stranger = 23

GPIO.output(17, False)
GPIO.output(18, False)
GPIO.output(22, False)
GPIO.output(23, False)

def shine(pin):
    count = 0
    while count < 5:
        GPIO.output(pin, True)
        time.sleep(0.5)
        GPIO.output(pin, False)
        time.sleep(0.5)
        count  = count + 1

if __name__ == "__main__":
    with open('result.csv', newline='') as csvfile:
        rows = csv.reader(csvfile)
        
        for row in rows:
            result = row[0]
            confidence_0 = row[1]
            confidence_1 = row[2]
            confidence_2 = row[3]


    window = tk.Tk()
    window.title("BMElab final Project ECG classfier predict result")
    window.geometry('500x150')
    f1 = tk.Frame(window)
    f2 = tk.Frame(window)
    f1.pack()
    f2.pack()

    TopLabel = tk.Label(f1, text= 'BMElab final Project: EKG classfier Predict Result').grid(row = 0, column = 1)

    Subj1 = tk.Label(f1, text= 'Coherent(0)').grid(row = 1, column = 0)
    Conf1 = tk.Label(f1, text= 'Confidence = ' + confidence_0).grid(row = 1, column = 1)
    Subj2 = tk.Label(f1, text= 'Daniel(1)').grid(row = 2, column = 0)
    Conf2 = tk.Label(f1, text= 'Confidence = ' + confidence_1).grid(row = 2, column = 1)
    Subj3 = tk.Label(f1, text= 'Mariia(2)').grid(row = 3, column = 0)
    Conf3 = tk.Label(f1, text= 'Confidence = ' + confidence_2).grid(row = 3, column = 1)

    
    if int(result) == 0:
        result = 'Coherent'
        shine(LED_Coherent)

    elif int(result) == 1:
        result = 'Daniel'
        shine(LED_Daniel)

    else:
        result = 'Mariia'
        shine(LED_Mariia)


    if max(float(confidence_0), float(confidence_1), float(confidence_2)) < 0.5:
        result = 'Stranger'
        shine(LED_stranger)
    
    
    Result = tk.Label(f2, text = 'Result = ' + result).grid(row = 1, column = 1)
    GPIO.cleanup()
    window.mainloop()