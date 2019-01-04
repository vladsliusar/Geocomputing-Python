"""
    This program calculates the area of a triangle or trapezoid depending on the user input. Additionally,
    it allows to convert input values into a numeric type, and prompts a user to enter the correct type of value if unable to convert.
    Prompts to correct all values.
"""

# Define a function loopHeight that will process height values of a triangle or trapezoids.
def loopHeight():
    global height # use global statement on variable height in order to make it available outside of the function.
    loopCount = 0
    # The while statement keeps looping until its condition (loopCount<4) made False. 
    while loopCount<4:                      
        loopCount += 1
        # Variable height is being assigned an input function that gathers keyboard input from a user.   
        height = raw_input ("Please enter the lenght of the height: ")      
        # Try statement attempts to execute each statement below.
        # If try statement failed, it skips the remaining part and jumps to the except statement               
        try:                                                 
            # The integer function attempts to convert the value of variable "height" into a float type.
            height = float(height)     
            # If the conversion was successful, height becomes an integer, which could be used in any further calculation.
            # The while loop breaks after that.           
            break                          
        # If the conversion failed, the except statement will give an error message and continue to a new loop.
        except:         
            print '\nyou entered a string value that can NOT be converted to a float value'  
    if loopCount == 4:
        quit()
# Define a function loopBase that will process base value of a triangle.
def loopBase():
    global base # use global statement on variable base in order to make it available outside of the function.
    loopCount = 0
    # The while statement keeps looping until its condition (loopCount<4) made False. 
    while loopCount<4:                      
        loopCount += 1
        # Variable base is being assigned an input function that gathers keyboard input from a user.   
        base = raw_input ("Please enter the length of the base of the triangle: ")    
        # Try statement attempts to execute each statement below.
        # If try statement failed, it skips the remaining part and jumps to the except statement               
        try:                                                     
            # The integer function attempts to convert the value of variable base into a float type.
            base = float(base)    
            # If the conversion was successful, base becomes an integer, which could be used in any further calculation.
            # The while loop breaks after that.            
            break                          
        # If the conversion failed, the except statement will give an error message and continue to a new loop.
        except:         
            print '\nyou entered a string value that can NOT be converted to a float value'  
    if loopCount == 4:
        quit()
# Define a function loopBaseA that will process smaller base value of a trapezoid.
def loopBaseA():
    # Use global statement on variable baseA in order to make it available outside of the function.
    global baseA 
    loopCount = 0
    # The while statement keeps looping until its condition (loopCount<4) made False. 
    while loopCount<4:                      
        loopCount += 1
        # Variable baseA is being assigned an input function that gathers keyboard input from a user.   
        baseA = raw_input ("Please enter the length of the smaller base of the trapezoid: ")   
        # Try statement attempts to execute each statement below.
        # If try statement failed, it skips the remaining part and jumps to the except statement               
        try:                                                   
            # The integer function attempts to convert the value of variable baseA into a float type.
            baseA = float(baseA)     
            # If the conversion was successful, baseA becomes an integer, which could be used in any further calculation.
            # The while loop breaks after that.        
            break                          
        # If the conversion failed, the except statement will give an error message and continue to a new loop.
        except:         
            print '\nyou entered a string value that can NOT be converted to a float value'  
    if loopCount == 4:
        quit()
# Define a function loopBase that will process larger base value of a trapezoid.
def loopBaseB():
    global baseB # use global statement on variable baseB in order to make it available outside of the function.
    loopCount = 0
    # The while statement keeps looping until its condition (loopCount<4) made False. 
    while loopCount<4:                      
        loopCount += 1
        # Variable baseB is being assigned an input function that gathers keyboard input from a user.   
        baseB = raw_input ("Please enter the length of the larger base of the trapezoid: ")     
        # Try statement attempts to execute each statement below.
        # If try statement failed, it skips the remaining part and jumps to the except statement               
        try:                                               
            # The integer function attempts to convert the value of variable baseB into a float type.
            baseB = float(baseB)     
            # If the conversion was successful, baseB becomes an integer, which could be used in any further calculation.
            # The while loop breaks after that.            
            break                          
        # If the conversion failed, the except statement will give an error message and continue to a new loop.
        except:         
            print '\nyou entered a string value that can NOT be converted to a float value'  
    if loopCount == 4:
        quit()
# Assign input function (string) to variable answer.  
# The function prompts the user to choose an area to be calculated for either triangle or trapezoid.              
answer = raw_input("Would you like to calculate area of triangle or trapezoid? ")
# if answer/input is triangle(supplied condition), the below commands are executed. Otherwise, the program goes to elif.
if answer == "triangle":    
    print "This program finds the area of a triangle."  # this line prints out the specified string to the screen
    print   # this command prints out an empty space
    loopHeight() # call function loopHeight
    loopBase() # call function loopBase
    # Variable area is being assigned the expression that calculates an area of a triangle, the result is printed to the screen.
    area = 0.5 * height * base 
    print "The area of the triangle with height", height, "and base", base, "is", area, "."
    exit # exit running the script.
# if answer is trapezoid, the below commands are executed.
elif answer == "trapezoid": 
    print "This program finds the area of a trapezoid."
    print
    loopHeight() # call function loopHeight
    loopBaseA() # call function loopBaseA
    loopBaseB() # call function loopBaseB
    # Variable area is being assigned the expression that calculates an area of a trapezoid, the result is printed to the screen.
    area = (baseA + baseB) / 2 * height 
    print "The area of the trapezoid with height", height,",","smaller base", baseA,"and larger base", baseB, "is", area, "."    





