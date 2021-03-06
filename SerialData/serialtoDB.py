#!/usr/bin/python

import serial
import MySQLdb
import time
import datetime
import RPi.GPIO as GPIO

while(1):

	port = serial.Serial("/dev/ttyACM0", baudrate = 9600, timeout = None, parity=serial.PARITY_EVEN, rtscts=1)

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	while(1):
                db = MySQLdb.connect(host="localhost", user="root", passwd="meisseli", db="TOIMISTO")

                cur = db.cursor()
	

                coffee = True

                
		try:
                        coffee = port.readline()
		
                        print coffee
                        print datetime.datetime.utcnow()

                        door = GPIO.input(14)

                        print "Saatiin luettua arvot"
                        
                        try:
                                if coffee:
                                        cur.execute("INSERT INTO ToimistoData VALUES (null, null, %d, null)" % (door))
                                else:
                                        cur.execute("INSERT INTO ToimistoData VALUES (null, null, %d, NOW())" % (door))
                                db.commit()
                                print "Meni lapi"
                                db.close()
                                
                        except MySQLdb.ProgrammingError, e:
                                print "There was mysql programming error"
                        time.sleep(5)

                except IndexError:
                        print "Oops, something went wrong"
