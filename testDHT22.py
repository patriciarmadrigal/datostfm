#Libraries
import Adafruit_DHT as dht
import time
from time import sleep
import os.path


lastOpennedFile = ""
path = "home/pi/git/TFMPatri/output.txt"

if os.path.isfile(path):
  lastOpennedFile = open("home/pi/git/TFMPatri/output.txt", "a")
else:
  lastOpennedFile = open("/home/pi/git/TFMPatri/output.txt", "w+")
  lastOpennedFile.close()
  lastOpennedFile = open("/home/pi/git/TFMPatri/output.txt", "a")

def now():
    return time.strftime('[%d-%m-%Y %H:%M:%S]')

def append2File(s): 
        lastOpennedFile.write(s+"\n")
        lastOpennedFile.flush()

#Set DATA pin
DHT_1 = 4
DHT_2 = 17
while True:
    #Read Temp and Hum from DHT22
    h,t = dht.read_retry(dht.DHT22, DHT_1)
    h2,t2 = dht.read_retry(dht.DHT22, DHT_2)
    #print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(t,h))
    # append2File("{0} [S1], {1:0.01f}, {2:0.01f}, [S2], {3:0.01f}, {4:0.01f}".format(now(), t, h, t2, h2))
    append2File("{0} [S1], {1:0.01f}, {2:0.01f}, [S2], {3:0.01f}, {4:0.01f}".format(now(), t, h, t2, h2))
    sleep(10) #Wait 5 seconds and read again
