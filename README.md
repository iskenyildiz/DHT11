# DHT11

# Raspberry Pi 4 Temperature Humdity Sensor(DHT11) using Grove Pi+.

# First Download Grove Pi:

curl -kL dexterindustries.com/update_grovepi | bash

sudo reboot

cd /home/pi/Desktop

git clone https://github.com/DexterInd/GrovePi.git

sudo i2cdetect -y 1

# Inside Grove Pi folder:

cd Firmware

bash firmware_update.sh

# Docker installation/config for Ubuntu 18.04 Server 

```sudo apt-get update```
```sudo apt install docker.io```
```sudo systemctl start docker```
```sudo docker ps ```(for current working containers.)

```sudo docker ps -a``` (print all containers.)

# InfluxDB container

```sudo docker pull influxdb```

```sudo docker run -d -p 8083:8083 -p 8086:8086 -p 25826:25826/udp -v $PWD/influxdb:/var/lib/influxdb -v $PWD/influxdb.conf:/home/pi/influxdb.conf:ro influxdb:1.0 ```

'-d' option makes the container run in the background.

to stop the container:

```docker stop 'container ID' ```

``` curl -i -XPOST 'http://35.198.129.164:8086/write?db=mydb' --data-binary @data.txt ```

(sends the data through the InfluxDB API.)


# GRAFANA

```docker pull grafana/grafana```

```docker run -d --name=grafana -p 3000:3000 grafana/grafana ```

(--name is optional, can run into problems if you stop and restart the container. Suggested to not include.)

# Running the project

Start the containers using the run commands above.

Either create relationless database in influxdb manually or through the API using:

```curl -G http://35.198.129.164:8086/query --data-urlencode "q=CREATE DATABASE mydb"```

If you can connect to 35.198.129.164:8083 and 35.198.129.164:3000 you can proceed to sending the Raspberry Pi data.

Clone the bash.sh and bash.py files into the same directory.

Make sure bash.sh has execute priviledge you can check this using:

```ls -l bash.sh```

You can give execute access with chmod +x bash.py

Run the file ./bash.sh, check database for sent data and grafana graph.

# Notes for myself

Influxdb database schema consists of <measurement>,<tag-key><tag-value> <field-key><field-value> unix-timestamp

If the data is seperated with ',' instead of space it follows the measurement and tagkey format, make sure you fill them carefully. 

Field key is the data you want to send. Seperate it with a space. Timestamp is optional if left empty it will fill with system time.




