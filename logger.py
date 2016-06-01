import RPi.GPIO as GPIO
import datetime
import time

logfile = open('/home/pi/pir.log','a')

def logDetails(pin):
    line = "{},{}\n".format(datetime.datetime.now(), pin)
    logfile.write(line)
    logfile.flush()
    
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)

GPIO.add_event_detect(11, GPIO.FALLING, callback=logDetails)
GPIO.add_event_detect(13, GPIO.FALLING, callback=logDetails)
GPIO.add_event_detect(15, GPIO.FALLING, callback=logDetails)

while True:
    time.sleep(5)
    
logfile.close()
