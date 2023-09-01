import os

# Module for reading CSV files
import csv

#vtotal number of months included in the dataset
month = []
#The net total amount of "Profit/Losses" over the entire period
totalamount = []
#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

csvpath = os.path.join('Resources', 'budget_data.csv')
outpath = os.path.join('analysis', 'budget_analysis.txt')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')



    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
        month.append(row[0])
        totalamount.append(int(row[1]))
    print(len(month))
    print(sum(totalamount))