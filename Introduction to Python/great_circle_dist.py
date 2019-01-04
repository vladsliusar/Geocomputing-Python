"""
    This program allows to calculate the spherical distance between any two locations on Earth
    by prompting a user to enter coordinates in decimal degrees for those two locations.          
"""

# import math module
import math
# Define function named locationOne that will process input of coordinates for the first location.
def locationOne():  
    global lat1 # use global statement on variable lat1 in order to make it available outside of the function.
    global lon1 # use global statement on variable lon1 in order to make it available outside of the function.
    loopCount=0 # assign a value of 0 to variable loopCount
    print "****This program calculates spherical distance between two locations on Earth using their coordinates."
    print "It is expected that northern latitude and eastern longitude are entered as positive numbers, and", 
    print "southern latitude and western longitude as negative numbers****"
    print
    # The while statement keeps looping until its condition (loopCount<25) made False. 
    while loopCount<25:
        loopCount+=1 
        # Variables lat1 and lon1 are being assigned a raw input function that gathers keyboard input from a user.
        lat1=raw_input("Please enter latitude of the first location in decimal degrees ")
        lon1=raw_input("Please enter longitude of the first location in decimal degrees ")
        try:
            # The float function attempts to convert the value of variables lat1 and lon1 into a float type.
            lat1=float(lat1)
            lon1=float(lon1)
            break
        # If the conversion failed, the except statement will give an error message and continue to a new loop.
        except:
            print "Incorrect values entered, please re-enter the coordinates of the first location."
locationOne() # call function locationOne
# Define function named locationOne that will process input of coordinates for the second location.
def locationTwo():
    global lat2 # use global statement on variable lat2 in order to make it available outside of the function.
    global lon2 # use global statement on variable lon2 in order to make it available outside of the function.
    loopCount=0
    while loopCount<25:
        loopCount+=1
        # Variables lat2 and lon2 are being assigned a raw input function that gathers keyboard input from a user.
        lat2=raw_input("Please enter latitude of the second location in decimal degrees ")
        lon2=raw_input("Please enter longitude of the second location in decimal degrees ")
        try:
            # The float function attempts to convert the value of variables lat2 and lon2 into a float type.
            lat2=float(lat2)
            lon2=float(lon2)
            break # If conversion successful, program continues further outside of the function.
        # If the conversion failed, the except statement will give an error message and continue to a new loop.
        except:
            print "Incorrect values entered, please re-enter the coordinates of the second location."
locationTwo() # call function locationTwo
# Use math.radians fucntion to convert values of lat1, lat2, lon1, and lon2 from decimal degrees to radians.
lat1=math.radians(lat1)
lat2=math.radians(lat2)
lon1=math.radians(lon1)
lon2=math.radians(lon2)
# Considering the distance formula d = acos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(lon1-lon2))
# use trigonometry functions to calculate sin and cos of latidudes and longitudes accordingly.
lat1Sin = math.sin(lat1)
lat2Sin = math.sin(lat2)
lat1Cos = math.cos(lat1)
lat2Cos = math.cos(lat2)
lon1Cos = math.cos(lon1)
lon2Cos = math.cos(lon2)
lon1_lon2_differnceCos = math.cos(lon1-lon2)
# Calculate the value of distance using the math.acos function on the trigonometry values of latitude and longitute calculated above.
distance = math.acos(lat1Sin*lat2Sin+lat1Cos*lat2Cos*lon1_lon2_differnceCos)
# Calculate spherical distance between the two locations. Print the below message along with the value of spherical distance.
sphericalDistance = distance*6300
print "The spherical distance between the two locations is ", int(round(sphericalDistance)),"km."

