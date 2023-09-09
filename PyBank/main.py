import os

# Module for reading CSV files
import csv

#vtotal number of months included in the dataset
month = []
#The net total amount of "Profit/Losses" over the entire period
totalamount = []
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
changelist = []
counter = 0
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
        month.append(row[0])
        totalamount.append(int(row[1]))
        if counter > 0 :
           changelist.append(int(row[1])-previousvalue)
        previousvalue = int(row[1])
        counter += 1
        


    sumtotal = sum(totalamount)
    avgchange = round(sum(changelist)/len(changelist),2)
    maxchange = max(changelist)
    minchange = min(changelist)

    maxindex = changelist.index(maxchange)
    minindex = changelist.index(minchange)
    maxmonth = month[maxindex+1]
    minmonth = month[minindex+1]
    
    outputtext = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {len(month)}\n"
        f"Total: ${sumtotal}\n"
        f"Average Change: ${avgchange}\n"
        f"Greatest Increase in Profits: {maxmonth} (${maxchange})\n"
        f"Greatest Decrease in Profits: {minmonth} (${minchange})"


    )
    
    print(outputtext)
   
with open(outpath,"w") as textfile:
    textfile.write(outputtext)
    
    


