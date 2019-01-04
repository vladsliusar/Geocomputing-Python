"""
    This program collects user input of DD or DMS, converts it to the other form,
    and reports the converted value.
"""
        
# Import math module.
import math
# Define function dms2dd that performs necessary calculations to convert DMS to DD.
def dms2dd((degrees, minutes, seconds)):
    # assign a tuple to variable dms
    dms = (degrees, minutes, seconds)
    # assign tuple item values to variables
    degrees = float(dms[0]) # index 0, first item
    minutes = float(dms[1]) # index 1, second item
    seconds = float(dms[2]) # index 2, third item
    # If block ensures that negative and positive input values of DMS are calculated appropriately.
    if degrees >0:
        DD = degrees+minutes/60+seconds/3600
    else:
        DD = degrees-minutes/60-seconds/3600
    print "Its DD form is",round(DD,4),"." # print message to the screen including the value of DD.
# Define function dms2dd that performs necessary calculations to convert DD to DMS.
def dd2dms(degrees):
    D = int(degrees) # calculate degrees value using int function
    # calculations for minutes:
    DM = degrees - D
    MS = DM * 60
    M = int(MS) # calculate final minutes value using int function
    # calculations for seconds:
    SM = MS - M
    S = int(SM*60) # calculate final seconds value using int function
    # If block ensures that negative input values of DD are calculated appropriately.
    if degrees < 0:
        M = M *(-1)
        S = S *(-1)
    print "Its DMS form is",D,M,S,"." # print message to the screen

# Assign raw_input function to variable dmsORdd, collect user input as a string value.
dmsORdd = raw_input("Please enter a latitude or longitute value in DMS or DD format. >")
# Incorrect input values could be trapped here.
# Split function creates a list from user input values.
dmsORdd.split()
# Convert each item in the list to float type, 
# assign the list to the variable number_dmsORdd.
number_dmsORdd = [float(i) for i in dmsORdd.split(',')]
# If block determines if the user input is DD or DMS
# and directs to the appropriate function for conversion.
if number_dmsORdd == number_dmsORdd[:1]: # if one item in the list
    number_dmsORdd = float (number_dmsORdd[0])
    print "The input value is in DD form." # print message to the screen
    # Call dd2dms fucntion.
    dd2dms(number_dmsORdd)
elif number_dmsORdd == number_dmsORdd[0:3]: # if 3 items in the list
    print "The input value is in DMS form." # print message to the screen
    # Call dms2dd fucntion.
    dms2dd(number_dmsORdd)



