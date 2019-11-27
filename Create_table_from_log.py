import os
import sys

arguments = len(sys.argv) - 1
if arguments != 1:
    raise Exception('Please provide one argument to the script. This should be the path to .log file')


my_file = sys.argv[1]

try:
    with open(my_file) as infile:
        pass
except IOError:
    print('Could not find file, please check input argument is a path to the .log file')


content_list = [] # where we store the whole txt file as a list
tables_lines = [] # empty dataframe where we'll identify where the table part starts
linenum = 0 # start linenum at zero, used as a counter
substr = "Summary of Genetic Correlation Results".lower()  # Part of text where table begins

print('Reading log file')
with open (my_file,'rt') as myfile:
    for count, line in enumerate(myfile):
        linenum += 1
        content_list.append(line.rstrip('\n')) #take out the line breaks
        if line.lower().find(substr) != -1: #when you find the substring, create some text that tells us where it is
            line_start = linenum - 1
            tables_lines.append("Line " + str(line_start) + ": " + line.rstrip('\n'))
        
                              
                             
#print('Your table starts on line ' + str(tables_lines)) #print out where the text is 


table_only = content_list[line_start:] # Select only the lines where the table exists (one less that what is printed)


new_list = [data.split() for data in table_only] # This splits each line into individual components
columns = new_list[1] # The first line is the columns
#print('Printing column names: ' + str(columns))
#print('Printing first line of data: ' + str(new_list[2])) 

import pandas as pd

my_table = pd.DataFrame(new_list[2:], columns = columns) # Import data (from line 2 onwards) and columns
print('Creating table')

#print(my_table) 

# You can see that the last 3 rows are not wanted, so we should remove these

#print('Dropping unecessary last 3 rows (double check you have the correct number of rows)')
my_table.drop(my_table.tail(3).index, inplace = True)
#print(my_table)

#output_file = input("Please specify the name of your new table file: ")
output_file = my_file + '_table.csv'

my_table.to_csv(output_file, index = None) # save table as csv

print('Table saved as ' + output_file)
