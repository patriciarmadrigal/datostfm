import glob
import time
import os.path

s3Path = ('S3', '/sys/bus/w1/devices/28-3c01b55660d2/w1_slave')
s4Path = ('S4', '/sys/bus/w1/devices/28-3c01b55668ca/w1_slave')
s5Path = ('S5', '/sys/bus/w1/devices/28-3c01b556f942/w1_slave')

pathes = []
def fillPathes():
    del pathes[:]
    if os.path.isfile(s3Path[1]):
     pathes.append(s3Path)

    if os.path.isfile(s4Path[1]):
     pathes.append(s4Path)

    if os.path.isfile(s5Path[1]):
     pathes.append(s5Path)

fillPathes()

lastOpennedFile = ""
path = "/home/pi/git/TFMPatri/o345.txt"

if os.path.isfile(path):
  lastOpennedFile = open(path, "a")
else:
  lastOpennedFile = open(path, "w+")
  lastOpennedFile.close()
  lastOpennedFile = open(path, "a")

def append2File(s): 
    lastOpennedFile.write(s+"\n")
    lastOpennedFile.flush()
       
def now():
    return time.strftime('[%d-%m-%Y %H:%M:%S]')

def read_temp_raw(p):
    f = open(p, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    res = ""
    for path in pathes:
        lines = read_temp_raw(path[1])    

        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
        res += "[{}] {}, ".format(path[0], temp_c)
    return now() + " " + res

while True:
    append2File(read_temp())
    fillPathes()
    time.sleep(10)


