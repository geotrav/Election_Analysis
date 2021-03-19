# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes for each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

import csv
import os

#dir (csv)
file_to_load = os.path.join("Election_Analysis","Election_Analysis","Resources","election_results.csv")
# open File
with open (file_to_load) as election_data:

    print (election_data)


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Election_Analysis","Election_Analysis","analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in Election\n-----------------\nArapahoe\nDenver\nJefferson")

#Close file

