import grovepi
import time
import smtplib
dht_sensor_port=4
dht_sensor_type=0
import time
data=open('data.txt','w')
[ temp,hum ] = grovepi.dht(dht_sensor_port,dht_sensor_type)
print ('Temp: '+ str(temp) + '*C' + '\tHumidity:' + ' %'+ str(hum) + ' ' + str(time.strftime("%s",time.gmtime())))
data.write('temperature ' + 'temp='+ str(temp))
data.write('\n')
data.write('temperature ' + 'hum='+ str(hum))
if temp>=25.0: 
    content = 'Oda sicakligi ' + str(temp) + '*C'
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.starttls()
    mail.login('gozenintern@gmail.com','password')
    mail.sendmail("gozenintern@gmail.com","muhammetkrn19@gmail.com",content)





