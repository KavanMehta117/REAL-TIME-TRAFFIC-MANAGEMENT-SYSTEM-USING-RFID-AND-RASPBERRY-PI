import os
import time
from datetime import datetime
from datetime import timedelta

class tasks:

	def __init__(self,time1,time2,id1):
		self.time1 = time1
		self.time2 = time2
		self.id1 = id1

	def speed(self):
		speed = 0
		toll = 0
		a = 0
		total = 0
		t1 = 0
		t2 = 0
		b = 0
		n = os.fork()
		if n > 0:
			os.wait()
			start_time = time.time()*1000.0
			pid3 = os.getpid()
			pri = 99
			sched = os.sched_param(pri)
			sc3 = os.sched_setscheduler(pid3, os.SCHED_RR,sched)
			if (speed > 0):
				print("The car with ID" +str(self.id) + " is overspeeding with speed" +str(speed))
				f = open ("speed.txt","w+")
				f.write("Car ID: "+ str(self.id) + " Speed: " +str(speed) +"\n")
				f.close()
			end_time = time.time()*1000.0
			tt = end_time - start_time
			print ("The total execution tine of speed defaulter task is\n" +str(tt))
			total =t1 + tt +t2
		else:
			z = os.fork()
			if z > 0:
				start_time = time.time()*1000.0
				pid1 = os.getpid()
				pri = 99
				sched = os.sched_param(pri)
				s = os.sched_setscheduler(pid1, os.SCHED_RR, sched)
				speed = 1000/(self.time2 - self.time1)
				print("The speed of the car with id " +str(self.id1) +" is " +str(speed) +"\n")
				print("Process id of Speed is " +str(pid1) +"\n")
				sc = os.sched_getscheduler(pid1)
				if sc == 1:
					print("The scheduling policy of " +str(pid1) +" FIFO " +"\n")
				elif sc == 2:
					print("The scheduling policy of " +str(pid1) +" Round Robin " +"\n")
				else:
					print("The scheduling policy of " +str(pid1) +" SJF " +"\n")
				end_time = time.time()*1000.0
				tt = end_time - start_time
				print ("The total execution time of speed task is" +str(tt) +"\n")
				t1 = t1 + tt
				exit()
			else:
				start_time = time.time()*1000.0
				pid2 = os.getpid()
				pri1 = 99
				sched = os.sched_param(pri1)
				s1 = os.sched_setscheduler(pid2, os.SCHED_RR, sched)
				toll = toll + 2.25
				print("The toll of the car with id " +str(self.id1) +" is " +str(toll) +"\n")
				print("Process id of toll is " +str(pid2) +"\n")
				sc1 = os.sched_getscheduler(pid2)
				if sc1 == 1:
					print("The scheduling policy of " +str(pid2) +" FIFO " +"\n")
				elif sc1 == 2:
					print("The scheduling policy of " +str(pid2) +" Round Robin " +"\n")
				else:
					print("The scheduling policy of " +str(pid1) +" SJF " +"\n")
				end_time = time.time()*1000.0
				tt = end_time - start_time
				t2 = t2 + tt
				print ("The execution time of Toll task is" +str(tt) +"\n")
				exit()
		return total


