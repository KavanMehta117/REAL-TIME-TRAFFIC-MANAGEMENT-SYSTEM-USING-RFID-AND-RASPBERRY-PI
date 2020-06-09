import RPi.GPIO as GPIO 
from mfrc522 import SimpleMFRC522
from datetime import datetime
from datetime import timedelta
import tasks
import threading 
import time 
import serial

ser = serial.Serial(
	port = '/dev/ttyS0',
	baudrate = 9600,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 10
)

arr = []

a, b = (0,0)

time_total = 0

for j in range(5):
    column = []
    for i in range(5):
        column.append(0)
    arr.append(column)


try:
	#GPIO.cleanup()
	def get_id():
		print ("Storing the ID's of the tags\n")
		i = 0
		while i < 5:
			rr = SimpleMFRC522(0, 0)
			id, text = rr.read()
			arr[i][0] = id
			print ("ID recorded")
			time.sleep(1)
			i += 1
	def id_print():
		print ("Printing the data\n")
		i = 0
		j = 0
		for i in range(len(arr)):
			for j in range(len(arr[i])):
				print (arr[i][j], end = ' ')
			print ()
	def get_time():
		print ("Time from the readers R1 and R2")
		k = 0
		while k < 5: 
			i = 0
			j = 0
			counter1 = 0
			counter2 = 0
			reader1 = SimpleMFRC522(0, 0)
			id1, text1 = reader1.read()
			t1 = datetime.now().time()
			time1 = (t1.hour*60 + t1.minute)*60+t1.second
			while i < 5:
				if arr[i][0] == id1:
					arr[i][1] = time1
					print ("Time from R1 is recorded")
				i += 1
			counter1 += 1
			time.sleep(0.1)
			reader2 = SimpleMFRC522(0, 1)
			id2, text2 = reader2.read()
			t2 = datetime.now().time()
			time2 = (t2.hour*60 + t2.minute)*60+t2.second
			while j < 5:
				if arr[j][0] == id2:
					arr[j][2] = time2
					print ("Time from the R2 is recorded")
					c = tasks.tasks(arr[j][1],arr[j][2],id2)
					t3 = c.speed()
					#time_total = time_total + t3
					print ("The total time take to execute the tasks is :"+str(t3))
				j += 1
			counter2 += 1
			k += 1
	def get_time2():
		print ("Getting time of R4 and R5\n")
		i = 0
		k = 0
		j = 0
		while k < 10:
				x = ser.readline()
				if len(x) != 0:
					res = [int(i) for i in x.split() if i.isdigit()]
					i = 0
					j = 0
					if (res[0] == 3):
						while i < 5:
							if arr[i][0] == res[1]:
								arr[i][3] = res[2]
								print ("Time from R3 recorded")
								if(arr[i][2] != 0):
									c1 = tasks.tasks(arr[i][2],arr[i][3],res[1])
									t2 = c1.speed()
									print ("The total execution time of tasks is" +str(t2))
							i += 1
					else:
						while j < 5:
							if arr[j][0] == res[1]:
								arr[j][4] = res[2]
								print ("Time from R4 recorded")
								if(arr[j][3] != 0):
									c2 = tasks.tasks(arr[j][3],arr[j][4],res[1])
									t1 = c2.speed()
									print ("The total execution time of the tasks is" +str(t1))
							j += 1
					k += 1
	def avgtt():
		avg = time_total/9
		print("The average turn around time is " +str(avg))

	
	get_id()
	id_print()
	t1 = threading.Thread(target = get_time)
	print ("Starting thread1 to get time from R1 and R2\n")
	t2 = threading.Thread(target = get_time2)
	print ("Starting thread2 to get time from R3 and R4\n")
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	id_print()
#	avgtt()
finally:
	GPIO.cleanup()



























