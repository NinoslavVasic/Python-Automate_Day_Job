"""Python script for analyzing the financial records of your company: calculate  month-by-month profit, by analyzing changes from csv file and prints results to a txt file"""

# Import the pathlib and csv library
from pathlib import Path
from os import listdir
import csv
directory = Path.cwd()
print(directory)
print('\n'.join(listdir(directory)))

#defining the path of csv_file from library

csv_data_input = Path('../python-homework/PyBank/budget_data.csv')

# create basic list to iterate to specific rows for variables

month_count = 0
total_profit = 0
this_month_profit = 0
last_month_profit = 0
profit_change = 0

profit_changes = []
months = []


#Open csv in reading mode with context manager


with open(csv_data_input,'r', newline="") as budget:
    csvreader = csv.reader(budget, delimiter= ",")


#skip the header labels to iterate with the values

    header = next(csvreader)

#iterate through the rows to gather monthly changes in profit

    for row in csvreader:

        month_count = month_count + 1
        months.append(row[0])
        this_month_profit = int(row[1])
        total_profit = total_profit + this_month_profit

        if month_count > 1:
            profit_change = this_month_profit - last_month_profit
            profit_changes.append(profit_change)
        last_month_profit = this_month_profit

# analyze the month by month results
sum_profit_changes = sum(profit_changes)
average_change = round(sum_profit_changes / (month_count - 1),2)

max_change = max(profit_changes)
min_change = min(profit_changes)

max_month_index = profit_changes.index(max_change)
min_month_index = profit_changes.index(min_change)


max_month = months[max_month_index]
min_month = months[min_month_index]

#Print Statements

print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total Profit: ${total_profit}")
print(f"Average Profit Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

#Output files

filename = input("")
save_file = filename.strip(".csv") + "_results.txt"
filepath = Path('../python-homework/PyBank', save_file)


with open(filepath,'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------------------------" + "\n")
    text.write(f"Total Months: {month_count}" + "\n")
    text.write(f"Total Profit: ${total_profit}" + "\n")
    text.write(f"Average Profit Change: ${average_change}" + "\n")
    text.write(f"Greatest Increase in Profits: {max_month} (${max_change})" + "\n")
    text.write(f"Greatest Decrease in Profits: {min_month} (${min_change})" + "\n")


