# -*- coding: utf-8 -*-

import csv
import argparse
import datetime
import os

#from .utils.validators import valid_file_path,valid_datetime_type

"""Main module."""


class SMSScheduler(object):
    """
    This class will schedule sms
    for the given csv file user
    """

    def __init__(self, csv_file, sms_date_time):
        super(SMSScheduler, self).__init__()
        self.csv_file = csv_file
        self.sms_date_time = sms_date_time

    def read_from_csv(self):
        '''
         this will read csv file
         this will yield the csv record
         here we will convert
        '''

    def run(self):
        self.read_from_csv()



def valid_datetime_type(arg_datetime_str):
    """custom argparse type for user datetime values given from the command line"""
    try:
        return datetime.datetime.strptime(arg_datetime_str, "%Y-%m-%d %H:%M")
    except ValueError:
        msg = "Given Datetime ({0}) not valid! Expected format, 'YYYY-MM-DD HH:mm'!".format(arg_datetime_str)
        raise argparse.ArgumentTypeError(msg)


def valid_file_path(arg_file_path):
    """custom argparse type for validating csv file path"""
    try:
        return os.stat(arg_file_path)
    except os.error:
        msg = "Given file path is not exits! ({0})".format(arg_file_path)
        raise argparse.ArgumentTypeError(msg)
    except Exception as e:
        msg = "there is some problem with file"
        raise argparse.ArgumentTypeError(msg)


if __name__ == "__main__":
    '''
        this method will get executed
    '''
    # Create opt parser object
    parser = argparse.ArgumentParser(description='Add csv file path and date time to send sms')
    # Add a required argument
    parser.add_argument("-f", "--file", dest="filename",
                        help="csv file absolute path", type=valid_file_path,
                        default=None, required=True)

    parser.add_argument('-d', '--start-datetime',
                        dest='start_datetime',
                        type=valid_datetime_type,
                        default=None,
                        required=True,
                        help='start datetime in format -d="YYYY-MM-DD H:M" ')

    args = parser.parse_args()
    # create sms scheduler instance
    sms_scheduler = SMSScheduler(args.filename,args.start_datetime)
    sms_scheduler.run()
