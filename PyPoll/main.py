import pandas as pd

file = "Resources/election_data.csv"

file_df = pd.read_csv(file)

total_votes = file_df["Ballot ID"].count()

vote_count = file_df["Candidate"].value_counts()

#creating the vote count values into a dataframe for later use
file2_df = vote_count.to_frame()

#resetting index for the new dataframe
file2_df = file2_df.reset_index()

#naming columns in the new dataframe
file2_df.columns = ["Candidate", "Votecount",]

#calcuate the percentage for candidates votes
file2_df["Percent_vote"] = file2_df["Votecount"]/ file2_df["Votecount"].sum()* 100

#sort values to be able to call index 0 for winning for candidate
sorted_file_df = file2_df.sort_values("Percent_vote", ascending=False)

#print election results
print("Election Results")
print("-------------------------------")
print("Total votes: " + str(total_votes) )
print("-------------------------------")
print(sorted_file_df)
print("-------------------------------")
print(f"Winner :   {sorted_file_df.iloc[0, 0]}")
print("-------------------------------")

#print results into a text file
with open("analysis/analysis_results.txt", "w") as file:
    file.write("Election Results\n")
    file.write("---------------------------------------------------\n")
    file.write(f"Total votes:  {total_votes}\n")
    file.write("---------------------------------------------------\n")
    file.write(f"{sorted_file_df}\n")
    file.write("---------------------------------------------------\n")
    file.write(f"Winner :   {sorted_file_df.iloc[0, 0]}\n")
    file.write("-------------------------------")





  
        
    

        

