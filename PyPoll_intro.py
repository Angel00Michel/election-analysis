
# Import the datetime class from the datetime modudle.
import datetime as dt
# Use now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now ", now)

import os
import csv
import random
#import numpy as np

dir(os)
dir(os.path)
dir(csv)
dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438})
dir(str)
dir(int)
dir(float)
dir(bool)
dir(list)
dir(tuple)
dir(dict)
dir(dt)
dir(random)
#dir(numpy)

# Assign a variable for the file to load and the path. 
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis.
    print(election_data)

# Close the file.
election_data.close()

file_to_load = 'Resources/election_results.csv'
with open(file_to_load) as election_data:
    print(election_data)
election_data.close()

file_to_load = os.path.join("Resources", "election_results.csv")