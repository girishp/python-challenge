import csv

total = 0
total_months = 0
previous_profit = 0
greatest_increase_in_profit = 0
greatest_decrease_in_profit = 0
date_of_greatest_increase = ""
date_of_greatest_decrease = ""
total_change_in_profit = 0

with open("./PyBank/Resources/budget_data.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)

    rows_done = 0

    for row in csv_reader:
        total_months = total_months + 1

        total = total + int(row['Profit/Losses'])

        current_profit = int(row['Profit/Losses'])
        
        if(rows_done > 0):
            change_in_profit = current_profit - previous_profit

            if(change_in_profit < greatest_decrease_in_profit):
                greatest_decrease_in_profit = change_in_profit
                date_of_greatest_decrease = row['Date']
            if(change_in_profit > greatest_increase_in_profit):
                greatest_increase_in_profit = change_in_profit
                date_of_greatest_increase = row['Date']

            total_change_in_profit = total_change_in_profit + change_in_profit
        
        previous_profit = current_profit
        
        rows_done = rows_done + 1

average_change_in_profit = total_change_in_profit / (total_months - 1)
average_change_in_profit = round(average_change_in_profit, 2)

line = ""
with open("./PyBank/analysis/results.txt", "w") as file:
    line = "Financial Analysis"
    print(line)
    file.write(line + '\n')
    line = "------------------------------"
    print(line)
    file.write(line + '\n')
    line = f"Total Months: {total_months}"
    print(line)
    file.write(line + '\n')
    line = f"Total: ${total}"
    print(line)
    file.write(line + '\n')
    line = f"Average Change: ${average_change_in_profit}"
    print(line)
    file.write(line + '\n')
    line = f"Greatest Increase in Profits: {date_of_greatest_increase} (${greatest_increase_in_profit})"
    print(line)
    file.write(line + '\n')
    line = f"Greatest Decrease in Profits: {date_of_greatest_decrease} (${greatest_decrease_in_profit})"
    print(line)
    file.write(line + '\n')

