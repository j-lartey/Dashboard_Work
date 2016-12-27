import JABS_Dashboard_Script
import JABS_Notes_Script
import datetime
import random
import os
import sys
import string
import time

# This script generates sample data for the JABS dashboard. 
# This script is a simple first version and has been 
# replaced by "callPythonAdvanced.py"

hourVar = 00
minVar = 00
rangeLimit = 288 # 288 iterations times 5 minute interval equals 24 hours

now1 = datetime.datetime.now().replace(hour=hourVar, minute=minVar, second=00)
now2 = datetime.datetime.now().replace(hour=hourVar, minute=minVar, second=00)
now3 = datetime.datetime.now().replace(hour=hourVar, minute=minVar, second=00)
now4 = datetime.datetime.now().replace(hour=hourVar, minute=minVar, second=00)
now5 = datetime.datetime.now().replace(hour=hourVar, minute=minVar, second=00)
now6 = datetime.datetime.now().replace(hour=hourVar, minute=minVar, second=00)
now7 = datetime.datetime.now().replace(hour=hourVar, minute=minVar, second=00)
now8 = datetime.datetime.now().replace()

timechange = datetime.timedelta(minutes=5) # 5 minute increments

timestring1 = now1.strftime("%Y-%m-%d-%H:%M:%S")
timestring2 = now2.strftime("%Y-%m-%d-%H:%M:%S")
timestring3 = now3.strftime("%Y-%m-%d-%H:%M:%S")
timestring4 = now4.strftime("%Y-%m-%d-%H:%M:%S")
timestring5 = now5.strftime("%Y-%m-%d-%H:%M:%S")
timestring6 = now6.strftime("%Y-%m-%d-%H:%M:%S")
timestring7 = now7.strftime("%Y-%m-%d-%H:%M:%S")
timestring8 = now8.strftime("%Y-%m-%d")
value1 = 0
value2 = 0
value3 = 0
value4 = 1
value5 = 0
value6 = 0
value7 = 0

for num in range(0, rangeLimit):
    JABS_Dashboard_Script.test("TPRS_TR", timestring1, value1)
    now1 = now1 + timechange
    timestring1 = now1.strftime("%Y-%m-%d-%H:%M:%S")
    value1 = value1 + random.randint(0, 30)

for num in range(0, rangeLimit):
    JABS_Dashboard_Script.test("NTPRS_TR", timestring2, value2)
    now2 = now2 + timechange
    timestring2 = now2.strftime("%Y-%m-%d-%H:%M:%S")
    value2 = value2 + random.randint(0, 30)

for num in range(0, rangeLimit):
    JABS_Dashboard_Script.test("NGI_TR", timestring3, value3)
    now3 = now3 + timechange
    timestring3 = now3.strftime("%Y-%m-%d-%H:%M:%S")
    value3 = value3 + random.randint(0, 60)

for num in range(0, rangeLimit):
    JABS_Dashboard_Script.test("HOST_STAT", timestring4, value4)
    JABS_Dashboard_Script.test("CLUSTER_STAT", timestring4, value4)
    JABS_Dashboard_Script.test("TIER_STAT", timestring4, value4)
    JABS_Dashboard_Script.test("TB_STAT", timestring4, value4)
    JABS_Dashboard_Script.test("USMS_STAT", timestring4, value4)
    JABS_Dashboard_Script.test("SOA_STAT", timestring4, value4)
    value4 = 1
    now4 = now4 + timechange
    timestring4 = now4.strftime("%Y-%m-%d-%H:%M:%S")

for num in range(0, rangeLimit):
    JABS_Dashboard_Script.test("TPRS_EMAIL", timestring5, value5)
    now5 = now5 + timechange
    timestring5 = now5.strftime("%Y-%m-%d-%H:%M:%S")
    value5 = value5 + random.randint(0, 30)

for num in range(0, rangeLimit):
    JABS_Dashboard_Script.test("EFTS_EMAIL", timestring6, value6)
    now6 = now6 + timechange
    timestring6 = now6.strftime("%Y-%m-%d-%H:%M:%S")
    value6 = value6 + random.randint(0, 30)

for num in range(0, rangeLimit):
    JABS_Dashboard_Script.test("BOOKING_EMAIL", timestring7, value7)
    now7 = now7 + timechange
    timestring7 = now7.strftime("%Y-%m-%d-%H:%M:%S")
    value7 = value7 + random.randint(0, 30)

JABS_Notes_Script.test(timestring8,
                       "On this day we had an issue. See the problem? We had to call DHS and then reboot.")
