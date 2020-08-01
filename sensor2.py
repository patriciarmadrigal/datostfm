#Libraries
import Adafruit_DHT as dht
import time
from time import sleep
import os.path

lastOpennedFile = ""
path = "/home/pi/git/TFMPatri/o2.txt"

if os.path.isfile(path):
  lastOpennedFile = open(path, "a")
else:
  lastOpennedFile = open(path, "w+")
  lastOpennedFile.close()
  lastOpennedFile = open(path, "a")

def now():
    return time.strftime('%d-%m;%H:%M:%S')

def append2File(s): 
        lastOpennedFile.write(s+"\n")
        lastOpennedFile.flush()

#Set DATA pin
DHT_1 = 17
while True:
    try: 
        h,t = dht.read_retry(dht.DHT22, DHT_1)
    except:
        print("Error in sensor 1")
    
    append2File("{0};S2;{1:0.01f};{2:0.01f}".format(now(), t, h).replace('.', ','))
    sleep(300)
