# Program will check to see if a date is in the correct date format: (DD/MM/YYYY)
# For the purpose of this Assignment, the dates will span from 01/01/1000 to 31/12/2999
# Module 3.1.1: does not have the correction for dates that are valid, but not on a calendar
# Will update in 3.1.2

import re

def validateDate(date_string):
    
    # Define the regex pattern
    datePattern = re.compile(r'''(
        (0[1-9]|[1-2][0-9]|3[0-1])          # First set of numbers (DATE)
        [/]                                 # Separator
        (0[1-9]|1[0-2])                     # Second set of numbers (MONTH)
        [/]                                 # Separator
        (1000|1[0-9]{3}|2[0-9]{3})          # Third set of numbers (YEAR)
            )''', re.VERBOSE)

    # Match the date pattern and make a variable for it
    match = datePattern.search(date_string)

    
    # Check if the date is valid. If valid, separate the Date, Month, and Year into variables
    # Printed the D/M/Y to check the group number.
    if match:
        
        date = match.group(2)
        print("date is: " + date)

        month = match.group(3)
        print("month is: " + month)

        year = match.group(4)
        print("year is: " + year)
        return True
    else:
        return False

# These are dates to test the date validation program with.
datesToTest = ["01/01/1000", "31/12/2999", "2000/10/10", "01/01/3000", "31/12/0999", " 20/05/2020", "30/02/2024 ", "05/13/2022", "02/05/22", "21-03-2020", "21302020"]

# The following will test to see if the test dates are valid or not.
# Currently the dates that are valid will print the separated values first,
# then say if they are valid or not.
for date in datesToTest:
    if validateDate(date):
        print(f"{date} is a valid date.")
    else:
        print(f"{date} is not a valid date.")          

# TODO: Make sure that for the right months, the right dates are followed         