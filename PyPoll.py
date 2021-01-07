# The data we need to retrieve.


# 1 The total number of votes cast
# 2 A complete list of candidates who received votes
# 3 The percentage of votes each candidate won.
# 4 The total number of votes each candidate won.
# 5 The winner of the election based on popular vote.

import csv
import os

# Assign a variable for the path to the file to load
file_to_load = os.path.join('Resources', 'election_results.csv')
# Assigna variable for the path to the file to save
file_to_save = os.path.join('analysis', 'election_analysis.txt')

 # Initialize the total vote counter as a variable at 0
total_votes = 0

#Open the election results and read the file
with open(file_to_load) as election_data:

    #To do read and analyze the data here
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file