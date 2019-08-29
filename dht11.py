import grovepi
import time
dht_sensor_port=4
dht_sensor_type=0
while True:
                [ temp,hum ] = grovepi.dht(dht_sensor_port,dht_sensor_type)
        #       print("Temp =", temp, "*C Humidity =", hum,"%")
                print 'Temp: '+ str(temp) + '*C' + '\tHumidity:' + ' %'+ str(hum) 
                time.sleep(1)








