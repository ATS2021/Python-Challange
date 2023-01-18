
import pandas as pd

file = "Resources/budget_data.csv"

file_df = pd.read_csv(file)

# calculate the total number of months
months = file_df['Date'].count()

total_revenue = file_df['Profit/Losses'].sum()

profit_changes = file_df['Profit/Losses'].diff()
file_df["Profit Changes"] = profit_changes.fillna("0")
avg_change = profit_changes.mean()

file_df = file_df.astype({"Profit Changes": int}, errors='raise')

sorted_file_df = file_df.sort_values("Profit Changes", ascending=False)

new_index_df = sorted_file_df.reset_index(drop = True)

print("Finanical Analysis")
print("---------------------------------------------------")
print("Total Months: "+ str(months))
print("Total : $"+ str(total_revenue))
print("Average Change : $"+ str(avg_change))
print(f"Greatest Increase: {new_index_df.iloc[0, 0]} $ {new_index_df.iloc[0, 2]}")
print(f"Greatest Decrease: {new_index_df.iloc[-1, 0]} $ {new_index_df.iloc[-1, 2]}")

with open("analysis/analysis_results.txt", "w") as file:
    file.write("Finanical Analysis\n")
    file.write("---------------------------------------------------\n")
    file.write(f"Total Months:  {months}\n")
    file.write(f"Total : $ {total_revenue}\n")
    file.write(f"Average Change : $ {avg_change}\n")
    file.write(f"Greatest Increase: {new_index_df.iloc[0, 0]} $ {new_index_df.iloc[0, 2]}\n")
    file.write(f"Greatest Decrease: {new_index_df.iloc[-1, 0]} $ {new_index_df.iloc[-1, 2]}\n")
