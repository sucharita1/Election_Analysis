# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add variables to load multiple files from a path.
local_file_to_load = os.path.join("Resources", "local_election_results.csv")
senate_file_to_load = os.path.join("Resources", "senate_election_results.csv")
congress_file_to_load = os.path.join("Resources", "congress_election_results.csv")

# Add variables to save multiple files to a path.
local_file_to_save = os.path.join("analysis", "local_election_analysis.txt")
senate_file_to_save = os.path.join("analysis", "senate_election_analysis.txt")
congress_file_to_save = os.path.join("analysis", "congress_election_analysis.txt")



def get_results(loading_file):
    # Initialize a total vote counter.
    total_votes = 0

    # Track the winning candidate, vote count and percentage
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0

    # Track the largest county and county voter turnout.
    largest_county = ""
    largest_votes = 0

    # Candidate Options and candidate votes.
    candidate_options = []
    candidate_votes = {}

    # Create a county options and county votes.
    county_options = []
    county_votes = {}
 
    # Read the csv and convert it into a list of dictionaries
    with open(loading_file) as election_data:
        reader = csv.reader(election_data)

        # Read the header
        header = next(reader)

        # For each row in the CSV file.
        for row in reader:

            # Add to the total vote count
            total_votes += 1

            # Get the candidate name from each row.
            candidate_name = row[2]

            # Extract the county name from each row.
            county_name = row[1]

            # If the candidate does not match any existing candidate add it to
            # the candidate list
            if candidate_name not in candidate_options:

                # Add the candidate name to the candidate list.
                candidate_options.append(candidate_name)

                # And begin tracking that candidate's voter count.
                candidate_votes[candidate_name] = 0

            # Add a vote to that candidate's count
            candidate_votes[candidate_name] += 1

            # Write an if statement that checks that the
            # county does not match any existing county in the county list.
            if county_name not in county_options:

                # Add the existing county to the list of counties.
                county_options.append(county_name)

                # Begin tracking the county's vote count.
                county_votes[county_name] = 0

            # Add a vote to that county's vote count.
            county_votes[county_name] += 1

    return [total_votes, winning_candidate, winning_count, winning_percentage, largest_county, largest_votes, candidate_options,candidate_votes, county_options, county_votes]

    
def save_results(saving_file, result):
    total_votes = result[0]
    winning_candidate = result[1]
    winning_count = result[2]
    winning_percentage = result[3]
    largest_county = result[4]
    largest_votes = result[5]
    candidate_options = result[6]
    candidate_votes = result[7]
    county_options = result[8]
    county_votes = result[9]
        
    # Save the results to our text file.
    with open(saving_file, "w") as txt_file:

        # Print the final vote count (to terminal)
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n\n"
            f"County Votes:\n")
        print(election_results, end="")

        txt_file.write(election_results)

        # Write a for loop to get the county from the county dictionary.
        for county_name in county_votes:
            # Retrieve the county vote count.
            votes = county_votes.get(county_name)
            # Calculate the percentage of votes for the county.
            vote_percentage = float(votes) / float(total_votes) * 100

            # Print the county results to the terminal.
            county_results = (
                f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
            
            print(county_results)

            # Save the county votes to a text file.
            txt_file.write(county_results)

            # Write an if statement to determine the winning county and get its vote count.
            if votes > largest_votes:
                largest_county = county_name
                largest_votes = votes

        # Print the county with the largest turnout to the terminal.
        largest_county_summary = (
            f"-------------------------\n"
            f"Largest County Turnout: {largest_county}\n"
            f"-------------------------\n"
        )
        print(largest_county_summary)


        # Save the county with the largest turnout to a text file.
        txt_file.write(largest_county_summary)

        # Save the final candidate vote count to the text file.
        for candidate_name in candidate_votes:

            # Retrieve vote count and percentage
            votes = candidate_votes.get(candidate_name)
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate's voter count and percentage to the
            # terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

            # Determine winning vote count, winning percentage, and candidate.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate_name
                winning_percentage = vote_percentage

        # Print the winning candidate (to terminal)
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)

        # Save the winning candidate's name to the text file
        txt_file.write(winning_candidate_summary)

# Setting a variable so that election results can be calculated multiple times using a while loop
election_result = 'Y'
while election_result.upper() == 'Y':
    # Menu to choose which election data you want to print on screen and save to file loacal/congressional/senatorial
    type_of_election = input("Enter the type of election results you need. (l)ocal, (c)ongress, (s)enatorial: ")

    # If you want to print and save the local elections results
    if type_of_election.lower() == 'l':
        result = get_results(local_file_to_load)
        save_results(local_file_to_save, result)
        
    # If you want to print and save the congressional elections results  
    elif type_of_election.lower() == 'c':
        result = get_results(congress_file_to_load)
        save_results(congress_file_to_save, result)
        
    # If you want to print and save the senatorial elections results
    elif type_of_election.lower() == 's':
        result = get_results(senate_file_to_load)
        save_results(senate_file_to_save, result)
        
    # If you enter an invalid response   
    else:
        print("You typed incorrect response. The response should be 'l', 'c', or 's'.")

    # If you want to calculate the results again
    election_result = input('Do you want to print election results again? Y/N: ')


