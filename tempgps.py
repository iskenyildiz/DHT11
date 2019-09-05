import grovepi
import time
import smtplib
dht_sensor_port=4 #DHT11 uses digital ports connected to S
dht_sensor_type=0
import time
import requests

source_mail_address='yourmail@gmail.com'
target_mail_address='targetmail@gmail.com'
source_mail_password='passwd'

ip_request = requests.get('https://get.geojs.io/v1/ip.json')
my_ip = ip_request.json()['ip']  
#print(my_ip)


geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
geo_request = requests.get(geo_request_url)
geo_data = geo_request.json()

org=geo_data["organization"] 
neworg=org.replace(" ", "_")



data=open('data.txt','w')
[ temp,hum ] = grovepi.dht(dht_sensor_port,dht_sensor_type)
print ('Temp: '+ str(temp) + '*C' + '\tHumidity:' + ' %'+ str(hum) + ' ' + str(time.strftime("%s",time.gmtime())))
data.write('temperature,location=' + neworg + ' temp='+ str(temp))
data.write('\n')
data.write('temperature,location=' + neworg + ' hum='+ str(hum))


def mail(content):
    mail = smtplib.SMTP("smtp.gmail.com",587) 
    mail.starttls()
    mail.login(source_mail_address,source_mail_password)
    mail.sendmail(source_mail_address,target_mail_address,content)


if temp>=25.0: 
    content = 'Oda sicakligi ' + str(temp) + '*C' + ' Sicaklik yuksek!'
    mail(content)
elif temp<=15:
    content = 'Oda sicakligi ' + str(temp) + '*C' + ' Sicakligi artirmaniz onerilir.'
    mail(content)
elif hum >=35:
    content = 'Odadaki nem orani  %' +  str(hum)  + ' Nem orani cok yuksek!'
    mail(content)
elif hum <=15:
    content = 'Odadaki nem orani  %' +  str(hum)  + ' Nem orani cok dusuk!'
    mail(content)
