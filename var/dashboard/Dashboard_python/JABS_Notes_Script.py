#!/usr/local/bin/python3

# Here the required Packages are referenced.
import json
import time
import os
import sys
import string
import glob
import calendar

# To create test data in development environment, uncomment
# the following line, comment out the three sys.argv values, and Tab the rest of the script once:
def test(DateTime, Notes):

    # Define the arguments that will be passed into the script from cron.
    # These two arguments need to be commented out in development
    # DateTime = sys.argv[1]
    # Notes = sys.argv[2]

    # Define the day/time variables from the time stamp passed to this script.
    # The date is used to name the JSON files.
    # The year and month are used to create the directory structure.
    Current_Year = DateTime[0:4]
    Current_Month = int(DateTime[5:7])
    Current_Month = calendar.month_name[Current_Month]
    Current_Date = DateTime[0:4] + DateTime[5:7] + DateTime[8:10]

    # Define the directories used throughout this script as variables:
    #
    # Turn on this variables for our Windows development:
    # JSON_Data = "C:/Program Files (x86)/EasyPHP-Webserver-14.1b2/www/var/www/html/JSON_data/"
    #
    # Turn on this variables for Linux instance:
    JSON_Data = "/var/www/html/JSON_data/"
    #
    # These variables should NOT be changed for the change in Linux/Windows:
    JSON_Location = (JSON_Data + Current_Year + '/' + Current_Month)
    JSON_File = (JSON_Location + '/' + Current_Date + '.json')

    if os.path.isfile(JSON_File):
        with open(JSON_File, 'r+') as data:
            Load_JSON = json.load(data)
            Load_JSON["NOTES"] = [Notes]
            data.seek(0)
            json.dump(Load_JSON, data, indent=4)
