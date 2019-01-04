"""
    This program collects user input as latitude and longitude of a location,
    and depending on the input, it tells the user where the entered latitude or longitude
    is located in relation to equator and meridian respectively.
"""

# Define function lat that would process the input value of a latitude.
def lat():
    # use global statement on variable latitude in order to make it available outside of the function.
    global latitude 
    loopcount=0
    while loopcount<1:
        loopcount+=1
        try:
            # float function converts the latitude value to float type.
            latitude = float(latitude)
            # if blocks are used to determine location of latitude in relation to equator.
            # Once determined, the message describing the location is printed to the screen.
            if latitude == 0:
                print "That location is on equator."
            elif 0 < latitude < 90:
                print "That location is north of the equator."
            elif -90 < latitude < 0:
                print "That location is south of the equator."
            elif latitude < -90:
                print "That location does not have a valid latitude!"
            elif latitude > 90:
                print "That location does not have a valid latitude!"
        # If the conversion to float type failed, the excep statement will give an error meassage.
        except:
            print "Incorrect value entered, the program is ending now."
            quit() # quit the program
# Define function lon that would process the input value of a longitude.
def lon():
    # use global statement on variable longitude in order to make it available outside of the function.
    global longitude
    loopcount=0
    while loopcount<1:
        loopcount+=1
        try:
            # float function converts the latitude value to float type.
            longitude = float(longitude)
            # if blocks are used to determine location of latitude in relation to equator.
            # Once determined, the message describing the location is printed to the screen.
            if longitude == 0:
                print "That location is on prime meridian."
            elif 0 < longitude < 180:
                print "That location is east of the prime meridian."
            elif -180 < longitude < 0:
                print "That location is west of the prime meridian."
            elif longitude < -180:
                print "That location does not have a valid latitude!"
            elif longitude > 180:
                print "That location does not have a valid latitude!"
        # If the conversion to float type failed, the excep statement will give an error meassage.
        except:
            print "Incorrect value entered, the program is ending now."
            quit() # quit the program
# Variable latitude is assigned a raw input function that gathers keyboard input from a user.        
latitude = raw_input("Please enter the value for latitude in decimal degrees: ")
lat() # call function lat
# Variable latitude is assigned a raw input function that gathers keyboard input from a user.
longitude = raw_input("Please enter the value for longitude in decimal degrees: ")
lon() # call function lon
