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

# open election results and reaqd File
with open (file_to_load) as election_data:

    #To do: read and analyze the data here.
      # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Read and Print header row
    headers = next(file_reader)
    print (headers)

    #Print each row in the CSV file.
    #for row in file_reader:
        #print (row)


# Create a filename variable to a direct or indirect path to the file.

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in Election\n-----------------\nArapahoe\nDenver\nJefferson")





#Close file

