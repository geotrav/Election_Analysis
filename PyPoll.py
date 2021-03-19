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
    for candidate_name in candidate_options:
        votes = candidate_votes[candidate_name]
        vote_percentage = (float(votes)/float(total_votes)*100)
        print (f"{candidate_name}:received {vote_percentage:.1f}% of the vote.")





        #print (row)
print (total_votes)
print (candidate_options)
print (candidate_votes)



# Create a filename variable to a direct or indirect path to the file.

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in Election\n-----------------\nArapahoe\nDenver\nJefferson")





#Close file

