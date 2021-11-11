# Add our dependencies.
import csv
import os


# 1. Retrieve the data
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
# Candidate Votes
candidate_votes = {}
# Winner
wining_percentage = 0
Winner = ""
wining_vote_count = 0



# Open the election results and read the file
with open(file_to_load, encoding='utf-8') as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    #print(headers)

    # Print each row in the CSV file.
    for row in file_reader:

       #  Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]


        # Print unique candidate name from each row.
        if candidate_name not in candidate_options:
            
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # 2. Get the total votes.
        candidate_votes[candidate_name] += 1


for candidate, votes in candidate_votes.items():

    # 3. Get the perentage votes
    percentage_votes = votes/total_votes * 100
    
    # Print each candidate's name and percentage of votes received
    print(f"{candidate}: {percentage_votes:.1f}%  ({votes:,})\n")

    # 4. Determine the winner and save winner's name, votes and percentage votes
    if percentage_votes > wining_percentage and votes > wining_vote_count:
        
        # Setting the winning percentage
        wining_percentage = percentage_votes

        # Setting the winner's name
        winner = candidate

        # Setting the winner's votes
        wining_vote_count = votes


message = (
    f"-----------------------------\n"
    f"Winner: {winner}\n"
    f"Winning Vote Count: {wining_vote_count:,}\n"
    f"Winning Percentage: {wining_percentage:.1f}%\n"
    f"-----------------------------")

# The name, votes and percentage votes received by the winner
print(message)

