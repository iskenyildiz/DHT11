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
while True:
     #   try:
                [ temp,hum ] = grovepi.dht(dht_sensor_port,dht_sensor_type)
        #       print("Temp =", temp, "*C Humidity =", hum,"%")
                print ('Temp: '+ str(temp) + '*C' + '\tHumidity:' + ' %'+ str(hum) + ' ' + str(time.strftime("%s",time.gmtime())))
                #print(f"Temp:{temp}*C Humidity:{hum} {datetime.now().strftime('%s')}")
                time.sleep(1)
                data.write('temperature,' + 'temp='+ str(temp) + ' ' + 'hum=' +str(hum) + ' ' + str(time.strftime("%s",time.gmtime())))
                #data.write(' ')
                #data.write('hum=' +str(hum))
                response = requests.post('http://35.198.129.164:8086/write?db=yeni4', data='temperature,temp={temp} hum={hum}')
                #response = requests.post('http://35.198.129.164:8086/write?db=yeni4', data=f'temperature,temp={int(temp)} hum={hum}')
                #print(response.status_code)
                data.write('\n')
      #  except KeyboardInterrupt as k:
       #         print("Shutting down.")
        #        break






