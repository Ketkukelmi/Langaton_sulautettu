#!/usr/bin/python

import serial
import MySQLdb
import time
import datetime

while(1==1):
	
	db = MySQLdb.connect(host="localhost", user="root", passwd="meisseli", db="TOIMISTO")

	cur = db.cursor()

	port = serial.Serial("/dev/ttyUSB0", baudrate = 9600, timeout = None, parity=serial.PARITY_EVEN, rtscts=1)
	
	while(1):
		time.sleep(10)
		port.write("*")

                vals = [0, 0, 0];

                print "vals alustettu"
                
		try:
                        print "eka try"
                        vals = (port.readline()).strip().split('|')
		
                        print vals[0]
                        print vals[1]
                        print vals[2]
                        print datetime.datetime.utcnow()

                        print "Saatiin luettua arvot"
                        
                        try:
                                print "toka try"
				if vals[2] > 0:
					cur.execute("INSERT INTO ToimistoData VALUES (null, %s, 1, NOW())") % (vals[0])
                                        db.commit()
                                        print "Meni lapi"
				else:
                                        print "Meni elseen"
                                db.close()
                                
                        except MySQLdb.ProgrammingError, e:
                                print "There was mysql programming error"

                except IndexError:
                        print "Oops, something went wrong"
