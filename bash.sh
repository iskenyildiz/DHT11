#!/bin/bash
while true; do
    python3 bash.py

    curl -i -XPOST "http://35.198.129.164:8086/write?db=mydb" --data-binary @data.txt
done


