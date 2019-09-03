
import grovepi
import time
dht_sensor_port=4
dht_sensor_type=0
import sys
import os
import time
from datetime import datetime
import requests
#now=datetime.now()
data=open('data.txt','w')
[ temp,hum ] = grovepi.dht(dht_sensor_port,dht_sensor_type)
print ('Temp: '+ str(temp) + '*C' + '\tHumidity:' + ' %'+ str(hum) + ' ' + str(time.strftime("%s",time.gmtime())))
time.sleep(1)
print(type(hum))
data.write('temperature ' + 'temp='+ str(temp))
data.write('\n')
data.write('temperature ' + 'hum='+ str(hum))

