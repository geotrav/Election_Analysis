# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes for each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.
#add dependencies
import csv
import os

#dir (csv)
# assign variable to load file to a path
file_to_load = os.path.join("Election_Analysis","Election_Analysis","Resources","election_results.csv")
#assign variable to save file to a path
file_to_save = os.path.join("Election_Analysis","Election_Analysis","analysis", "election_analysis.txt")
# Initialize a total vote counter
total_votes = 0
# Declare list of candidates
candidate_options = []
#Candidate votes dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open election results and reaqd File
with open (file_to_load) as election_data:

    #To do: read and analyze the data here.
      # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Read and Print header row
    headers = next(file_reader)
    print (headers)

    #Print each row in the CSV file.
    for row in file_reader:
      
       #2. Add to toal votes
       total_votes +=1
       #Capture candidate names
       candidate_name = row[2]
       #add candidate name to candidate options
       
       if candidate_name not in candidate_options:
         candidate_options.append(candidate_name)
        #2. Begin counting Candidates votes
         candidate_votes[candidate_name]=0
      #3. Begin counting
       candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
  # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = (float(votes)/float(total_votes)*100)
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
#  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
          winning_count = votes
          winning_percentage= vote_percentage
          winning_candidate= candidate_name
    winning_candidate_summary = (
      f"-------------------------\n"
      f"Winner: {winning_candidate}\n"
      f"Winning Vote Count: {winning_count:,}\n"
      f"Winning Percentage: {winning_percentage:.1f}%\n"
      f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)




        #print (row)
#print (total_votes)
#print (candidate_options)
#print (candidate_votes)



# Create a filename variable to a direct or indirect path to the file.

# Using the open() function with the "w" mode we will write data to the file.
#with open(file_to_save, "w") as txt_file:
    #txt_file.write("Counties in Election\n-----------------\nArapahoe\nDenver\nJefferson")





#Close file

