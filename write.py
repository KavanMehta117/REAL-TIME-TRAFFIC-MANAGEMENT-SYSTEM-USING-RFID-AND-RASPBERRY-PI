import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import serial

ser = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

i = 0

try:
	while i < 5:
       		reader = SimpleMFRC522(0, 0)
		id, text = reader.read()
		t1 = datetime.now().time()
		time1 = (t1.hour*60 + t1.minute)*60+t1.second
		ser.write("The time from reader 3 and id %ld  is %d\n"%(id,time1))
		print ("Data from R3 is sent\n")
		time.sleep(0.1)
		reader1 = SimpleMFRC522(0, 1)
		id1,text1 = reader1.read()
		t2 = datetime.now().time()
		time2 = (t2.hour*60 + t2.minute)*60+t2.second
		ser.write("The time from reader 4 and id %ld is %d\n"%(id1,time2))
		print ("Data from R4 is sent\n")
		time.sleep(0.1)
		i += 1
finally:
	GPIO.cleanup()


