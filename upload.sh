cat /home/pi/pir.log | grep $(date -d "yesterday" +"%Y-%m-%d") > /home/pi/logs/$(date -d "yesterday" +"%Y-%m-%d").log.1
/home/pi/dropbox_uploader.sh upload /hom/pi/logs/$(date -d "yesterday" +"%Y-%m-%d").log.1 $(date -d "yesterday" +"%Y-%m-%d").log.1
