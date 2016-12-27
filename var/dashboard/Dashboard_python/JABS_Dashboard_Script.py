#!/usr/local/bin/python3

# Date Updated:   03/28/2016
# Version Number: 2.0

# Here the required Packages are referenced.
import json
import time
import os
import sys
import string
import calendar

# To create test data in development environment, uncomment
# the following line, comment out the three sys.argv values, and Tab the rest of the script once:
def test(Identifier, DateTime, Transactions):

    # Define the arguments that will be passed into the script from cron.
    # These three arguments need to be commented out in development
    # Identifier = sys.argv[1]
    # DateTime = sys.argv[2]
    # Transactions = sys.argv[3]

    # Convert the Trans_state (number of transactions) value from a string to an integer.
    # Remove the "-" in the date string between the date and time then replace with a blank space.
    Transactions = int(Transactions)
    DateTime = DateTime[0:10] + " " + DateTime[11:19]

    # Define the day/time variables from the time stamp passed to this script.
    # The date is used to name the JSON files.
    # The year and month are used to create the directory structure.
    Current_Year = DateTime[0:4]
    Current_Month = int(DateTime[5:7])
    Current_Month = calendar.month_name[Current_Month]
    Current_Date = DateTime[0:4] + DateTime[5:7] + DateTime[8:10]

    # Define the directories used throughout this script as variables:
    #
    # Turn on these variables for our Windows development:
    JSON_Data = "C:/Program Files (x86)/EasyPHP-Webserver-14.1b2/www/var/www/html/JSON_data/"
    JSON_Template = "C:/Program Files (x86)/EasyPHP-Webserver-14.1b2/www/var/dashboard/" \
                    "Dashboard_python/JABS_JSON_template.json"
    #
    # Turn on these variables for Linux instance:
    # JSON_Data = "/var/www/html/JSON_data/"
    # JSON_Template = "/var/dashboard/Dashboard_python/JABS_JSON_template.json"
    #
    # These variables should NOT be changed for the change in Linux/Windows:
    JSON_Location = (JSON_Data + Current_Year + '/' + Current_Month)
    JSON_File = (JSON_Location + '/' + Current_Date + '.json')

    # Check for a directory for the current year and month,
    # then create them if they do not exist.
    if not os.path.exists(JSON_Location):
        os.makedirs(JSON_Location)


    # with open("C:/Program Files (x86)/EasyPHP-Webserver-14.1b2/www/var/"
    #           "dashboard/Dashboard_python/test_template.json", 'w') as outfile:
    #     json.dump({}, outfile, indent=4)

    # with open("C:/Program Files (x86)/EasyPHP-Webserver-14.1b2/www/var/"
    #           "dashboard/Dashboard_python/test_template.json", 'r+') as outfile:
    #     load = json.load(outfile)
    #     load[Identifier].update({'test': 1})
    #     json.dump(load, outfile, indent=4)


    # The else block checks if the JSON file for the current day does not exist, then create it from the JSON template.
    # For all other times in the day we will append the JSON file for that current day. The JSON file
    # is opened as a string and will close after the .read() is executed. We must close the JSON template
    # in the 'else' statement.
    if os.path.isfile(JSON_File):
        Calc_val = open(JSON_File).read()
        Calc = json.loads(Calc_val)
        try:
            LastTrans = Calc[Identifier][-1]['Cumulative']
        except:
            LastTrans = 0
            if Transactions > 500:
                Transactions = 0
    else:
        LastTrans = 0
        if Transactions > 500:
                Transactions = 0
        openJSONTemp = open(JSON_Template, "r")
        loadJSONTemp = json.load(openJSONTemp)
        open_JSON = open(JSON_File, "w")
        json.dump(loadJSONTemp, open_JSON, indent=4)
        openJSONTemp.close()
        open_JSON.close()

    # We need to check for 'TR' Identifiers here because we do not want STAT graphs to get
    # the current 'Transactions' value over-written.
    if Identifier.endswith('TR') or Identifier.endswith('EMAIL'):
        if LastTrans > Transactions:
            Transactions = LastTrans

    # Using the text file to store the last number of transactions will work for number-of-transactions graphs.
    # When graphing the system up/down status these text files will break the graph, so here we check for a
    # transaction graph and then calculate the new number of transactions. For status graphs we simply pass
    # the new transaction number from cron.
    if Identifier.endswith('TR') or Identifier.endswith('EMAIL'):
        CurrentTrans = Transactions - LastTrans
    else:
        CurrentTrans = Transactions

    Open_JSON = open(JSON_File).read()
    Load_JSON = json.loads(Open_JSON)

    # Add a new data set to each array when this Python script is called.
    if Identifier.endswith('STAT'):
        Load_JSON[Identifier].append({"Date": DateTime, "Cumulative": Transactions, "group": Identifier + "_total"})

    # For transaction graphs, write the change in number of transactions value to the JSON file.
    if Identifier.endswith('TR') or Identifier.endswith('EMAIL'):
        Load_JSON[Identifier].append({"Date": DateTime, "TransIncrease": CurrentTrans, "group": Identifier + "_step"})
        Load_JSON[Identifier].append({"Date": DateTime, "Cumulative": Transactions, "group": Identifier + "_total"})

    # Access the current JSON file with writing permission. Write the appended JSON data back to the
    # original file and then close the opened file to save computer memory.
    Open_JSON = open(JSON_File, "w")
    json.dump(Load_JSON, Open_JSON, indent=4)
    Open_JSON.close()
