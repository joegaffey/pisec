cat /home/pi/pir.log | grep $(date -d "yesterday" +"%Y-%m-%d") > /home/pi/logs/$(date -d "yesterday" +"%Y-%m-%d").csv
> pir.log
