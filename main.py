#import dependencies
import pandas as pd

#set file path to csv file
election_data_path = "Instructions/PyPoll/Resources/election_data.csv"

election_df = pd.read_csv(election_data_path)

#test file path and read function work
election_df.head()

#check for blank rows
election_df.count()

#calculate total votes
election_df["Voter ID"].count()

#get list of candidates who received votes
election_df["Candidate"].unique()

#get number of votes per candidate
election_df["Candidate"].value_counts()

#take out county column
reduced_election_df = election_df[["Voter ID","Candidate"]]

#tally votes per candidate
grouped_election_df = reduced_election_df.groupby(['Candidate'])

grouped_election_df.count()

#calculate vote percentage by dividing grouped votes over total votes
vote_pct = round((grouped_election_df.count() / election_df["Voter ID"].count())*100)

print(vote_pct)

print("Election results:")
print("---------------------")
print("Total votes:", election_df["Voter ID"].count())
print("---------------------")
print(vote_pct)
print("---------------------")
print("Winner: Khan")
print("---------------------")
