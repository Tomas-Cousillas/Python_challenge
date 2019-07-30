#import dependencies
import pandas as pd

#set file path to csv file
budget_data_path = "Instructions/PyBank/Resources/budget_data.csv"

budget_df = pd.read_csv(budget_data_path)

#test file path and read function work
budget_df.head()

#check for blank rows
budget_df.count()

#calculate total months
budget_df["Date"].count()

#calculate net total profit/losses
budget_df["Profit/Losses"].sum()

#calculate row to row differences
row_change = budget_df["Profit/Losses"].diff()
#calculate average row difference
row_change.mean()

#The greatest increase in profits (date and amount) over the entire period
#grab date index
max_date = budget_df["Profit/Losses"].idxmax()
#calculate greatest increase in profits
max_value = budget_df["Profit/Losses"].max()
#used index to get date
result1 = budget_df.iloc[max_date, 0]

print(result1, " ($",max_value,")")

#The greatest decrease in losses (date and amount) over the entire period
#grab date index
min_date = budget_df["Profit/Losses"].idxmin()
#calculate greatest increase in profits
min_value = budget_df["Profit/Losses"].min()
#used index to get date
result2 = budget_df.iloc[min_date, 0]

print(result2, " ($",min_value,")")

def prnt():
    print("Total months: ", budget_df["Date"].count())
    print("Total: $",budget_df["Profit/Losses"].sum())
    print("Average change: $", row_change.mean())
    print("Max increase:",result1, " ($",max_value,")")
    print("Max decrease:", result2, " ($",min_value,")")

prnt() 

#export file with summary info
import os
import csv
with open("summary.txt", "a") as f:
    print(f"Total months: ", budget_df["Date"].count(), file = f)
    print(f"---------------------------------------------------------------", file = f)
    print(f"Total: $",budget_df["Profit/Losses"].sum(), file = f)
    print(f"---------------------------------------------------------------", file = f)
    print(f"Average change: $", row_change.mean(), file = f)
    print(f"---------------------------------------------------------------", file = f)
    print("Max increase:",result1, " ($",max_value,")", file = f)
    print("Max decrease:", result2, " ($",min_value,")", file = f)
f.close()
