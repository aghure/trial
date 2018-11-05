# -*- coding: utf-8 -*-

import csv 
import argparse

"""Main module."""

class SMSScheduler(object):
	"""This class will schedule sms
	for the given csv file user
	"""
	def __init__(self, csvfile ,sms_date_time):
		super(SMSScheduler, self).__init__()
		self.csv_file = csvfile
		self.sms_date_time

	
	def read_from_csv(self):
		'''
		# this will read csv file
		# this will yield the csv record 
		# here we will convert 
		'''
		


 	def run(self):
 		'''
	    this method will get executed
	    '''
	    self.read_from_csv()
	    

	   


if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='THis will take csv file and timezone')
	args = sys.argv[1:]   
    parser.add_argument('-f', '--file', 
                                dest = 'filename',
                                help='input csv file.'
                        )
    parser.add_argument('-d', '--date', 
                                dest = 'date',
	                                help='this is the date to send sms'
	                        )

    # check the given csv file path exists or not
    # create sms scheduler instance 
	sms_scheduler = SMSScheduler()
	sms_scheduler.run()