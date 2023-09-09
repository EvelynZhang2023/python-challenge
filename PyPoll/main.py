import os

# Module for reading CSV files
import csv

totalvotes=0
candidatelist = []
candidatedictionary = {}
csvpath = os.path.join('Resources', 'election_data.csv')
outpath = os.path.join('analysis', 'election_analysis.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')



    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        totalvotes+=1
        candidatename=row[2]
        if candidatename not in candidatelist:
           candidatelist.append(candidatename)
           candidatedictionary[candidatename] = 0
        candidatedictionary[candidatename] += 1



    
    print(totalvotes)
    print(candidatedictionary)