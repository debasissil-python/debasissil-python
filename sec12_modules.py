# Builtin MODULES - Comes in-built with Python

# METHODS - You can search with dir(str)
    # dir(str) - Gives you a list of all 
    # directories of str

# BUILTIN FUNCTIONS - 
    # You can search with dir(__builtins__)

# What if we want to print out from a txt file
# after every 5 seconds ?

# BUILTIN MODULES

#import sys - import system
#sys.builtin_module_names (shows all builtin_module_names)

import time    # Builtin libraries
import os      # Standard libraries

# This os.path.exists('filepath') will help the code to run always - irrespective of the file
#while True:
#    with open('files\elephant.txt', 'r') as e:
#        if os.path.exists ('files\elephant.txt'):
#            print (e.read())
#        else:
#            print("File does not exist")
#        time.sleep(10)


# THIRD PARTY MODULES     
# There are lot of modules that does not come with python, but we can install it. Eg., pandas
# To install pandas ---> pip install pandas
# Pandas is a very powerful data structure library

# We have extract the data of temperatures from the csv file and print the mean of the temperature --->


import time    # Builtin libraries
import os      # Standard libraries
import pandas  # Third party libraries
  
# This os.path.exists('filepath') will help the code to run always - irrespective of the file
while True:
    with open('files\temps_today.csv', 'r') as e:
        if os.path.exists ('files\temps_today.csv'):
            data = pandas.read_csv('files\temps_today.csv')
            print (data())
        else:
            print("File does not exist")

        time.sleep(10)



