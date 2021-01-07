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

# create a list to store Candidate names
candidate_options = []

# create dictionary to store candidates with their vote totals
candidate_votes = {}
#Open the election results and read the file

# Winning Candidate and Vote Tracker 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:

    #To do read and analyze the data here
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    
    # loop over data and increment the total votes
    for row in file_reader:
        # add 1 to the total votes
        total_votes += 1

        #create variable to store the candidate name in the given row
        candidate_name = row[2]

        # if statment to test if the candidate in the current row is not already in the list of candidates
        if candidate_name not in candidate_options:
            # if name not in the list, add it to the list
            candidate_options.append(candidate_name)
            
            # add the candidate name to the candidate votes dict as a key with 0 votes
            candidate_votes[candidate_name] = 0
        
        # add 1 to the candidate votes in the dict
        candidate_votes[candidate_name] += 1
    # loop over the names in the candidate list
    for candidate_name in candidate_options:

        # store the vote count for the candidate being looped    
        votes = candidate_votes[candidate_name]

        #calculate candidate's percent of total votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # print each candidate and vote total in a string
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # check if current candidate's vote count and percentage is is greater than the current winning vote count/percentage
        if votes > winning_count and vote_percentage > winning_percentage:
            
            # set the winning count to the current candidate's vote count
            winning_count = votes
            # set the winning percentage to the current candidate's percentage
            winning_percentage = vote_percentage
            # set winning candidate to current candidate name
            winning_candidate = candidate_name
    # To do print winning candidate's name, vote count, and vote percentage to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Vote Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
        

