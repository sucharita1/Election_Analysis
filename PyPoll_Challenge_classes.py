# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
local_file_to_load = os.path.join("Resources", "local_election_results.csv")
senate_file_to_load = os.path.join("Resources", "senate_election_results.csv")
congress_file_to_load = os.path.join("Resources", "congress_election_results.csv")

# Add a variable to save the file to a path.
local_file_to_save = os.path.join("analysis", "local_election_analysis.txt")
senate_file_to_save = os.path.join("analysis", "senate_election_analysis.txt")
congress_file_to_save = os.path.join("analysis", "congress_election_analysis.txt")

class Election:
    def __init__(self, loading_file, saving_file):
        # Initialize a total vote counter.
        self.total_votes = 0
        self.loading_file = loading_file
        self.saving_file = saving_file

        # Candidate Options and candidate votes.
        self.candidate_options = []
        self.candidate_votes = {}

        # Create a county list and county votes dictionary.
        self.county_options = []
        self.county_votes = {}

        # Track the winning candidate, vote count and percentage
        self.winning_candidate = ""
        self.winning_count = 0
        self.winning_percentage = 0

        # Track the largest county and county voter turnout.
        self.largest_county = ""
        self.largest_votes = 0

    
    def get_results(self):
        # Read the csv and convert it into a list of dictionaries
        with open(self.loading_file) as election_data:
            reader = csv.reader(election_data)

            # Read the header
            header = next(reader)

            # For each row in the CSV file.
            for row in reader:

                # Add to the total vote count
                self.total_votes += 1

                # Get the candidate name from each row.
                self.candidate_name = row[2]

                # 3: Extract the county name from each row.
                self.county_name = row[1]

                # If the candidate does not match any existing candidate add it to
                # the candidate list
                if self.candidate_name not in self.candidate_options:

                    # Add the candidate name to the candidate list.
                    self.candidate_options.append(self.candidate_name)

                    # And begin tracking that candidate's voter count.
                    self.candidate_votes[self.candidate_name] = 0

                # Add a vote to that candidate's count
                self.candidate_votes[self.candidate_name] += 1

                # Write an if statement that checks that the
                # county does not match any existing county in the county list.
                if self.county_name not in self.county_options:

                    # Add the existing county to the list of counties.
                    self.county_options.append(self.county_name)

                    # Begin tracking the county's vote count.
                    self.county_votes[self.county_name] = 0

                # Add a vote to that county's vote count.
                self.county_votes[self.county_name] += 1

        #return self.total_votes, self.candidate_votes, self.county_votes

  
    def save_results(self):
         # Save the results to our text file.
        with open(self.saving_file, "w") as txt_file:

            # Print the final vote count (to terminal)
            election_results = (
                f"\nElection Results\n"
                f"-------------------------\n"
                f"Total Votes: {self.total_votes:,}\n"
                f"-------------------------\n\n"
                f"County Votes:\n")
            print(election_results, end="")

            txt_file.write(election_results)

            # 6a: Write a for loop to get the county from the county dictionary.
            for county_name in self.county_votes:
                # 6b: Retrieve the county vote count.
                votes = self.county_votes.get(county_name)
                # 6c: Calculate the percentage of votes for the county.
                vote_percentage = float(votes) / float(self.total_votes) * 100

                # 6d: Print the county results to the terminal.
                county_results = (
                    f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
                
                print(county_results)

                # 6e: Save the county votes to a text file.
                txt_file.write(county_results)

                # 6f: Write an if statement to determine the winning county and get its vote count.
                if votes > self.largest_votes:
                    self.largest_county = county_name
                    self.largest_votes = votes

            # 7: Print the county with the largest turnout to the terminal.
            largest_county_summary = (
                f"-------------------------\n"
                f"Largest County Turnout: {self.largest_county}\n"
                f"-------------------------\n"
            )
            print(largest_county_summary)


            # 8: Save the county with the largest turnout to a text file.
            txt_file.write(largest_county_summary)

            # Save the final candidate vote count to the text file.
            for candidate_name in self.candidate_votes:

                # Retrieve vote count and percentage
                votes = self.candidate_votes.get(candidate_name)
                vote_percentage = float(votes) / float(self.total_votes) * 100
                candidate_results = (
                    f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

                # Print each candidate's voter count and percentage to the
                # terminal.
                print(candidate_results)
                #  Save the candidate results to our text file.
                txt_file.write(candidate_results)

                # Determine winning vote count, winning percentage, and candidate.
                if (votes > self.winning_count) and (vote_percentage > self.winning_percentage):
                    self.winning_count = votes
                    self.winning_candidate = candidate_name
                    self.winning_percentage = vote_percentage

            # Print the winning candidate (to terminal)
            winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {self.winning_candidate}\n"
                f"Winning Vote Count: {self.winning_count:,}\n"
                f"Winning Percentage: {self.winning_percentage:.1f}%\n"
                f"-------------------------\n")
            print(winning_candidate_summary)

            # Save the winning candidate's name to the text file
            txt_file.write(winning_candidate_summary)

# Setting a variable so that election results can be calculated multiple times using a while loop
election_result = 'Y'
while election_result.upper() == "Y":
    # Menu to choose which election data you want to print on screen and save to file loacal/congressional/senatorial
    type_of_election = input("Enter the type of election results you need. (l)ocal, (c)ongress, (s)enatorial: ")
    
    # If you want to print and save the local elections results
    if type_of_election.lower() == 'l':
        local = Election(local_file_to_load, local_file_to_save)
        local.get_results()
        local.save_results()

    # If you want to print and save the congressional elections results    
    elif type_of_election.lower() == 'c':
        congress = Election(congress_file_to_load, congress_file_to_save)
        congress.get_results()
        congress.save_results()

    # If you want to print and save the senatorial elections results
    elif type_of_election.lower() == 's':
        senate = Election(senate_file_to_load, senate_file_to_save)
        senate.get_results()
        senate.save_results()

    # If you enter an invalid response  
    else:
        print("You typed incorrect response. The response should be 'l', 'c', or 's'.")

    # If you want to calculate the results again
    election_result = input('Do you want to print election results again? Y/N: ')

