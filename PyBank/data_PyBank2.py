# -*- coding: utf-8 -*-
"""
Student Do: Trading Log.
"""
# This script demonstrates how to perform basic analysis of trading profits/losses
# over the course of a month (86 months).

# Initialize the metric variables
total_months = 0
total = 0
average_change = 0
greatest_increase_month = ""
greatest_increase_amount = 0
greatest_decrease_month = ""
greatest_decrease_amount = 0

import csv 

# Initialize lists to hold profitable and unprofitable day profits/losses
profitable_months = []
unprofitable_months = []

# Specify the path to your CSV file
csv_file_path = "/Users/helobonetti/Desktop/BERKELEY/python-homework/budget_data.csv"

# Read data from the CSV file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Skip the header row if it exists
    next(csv_reader, None)
    
    # Extract profits/losses into a list
    trading_data = [(row[0], int(row[1])) for row in csv_reader]

# Iterate over each element of the list
for i, (month, month_pnl) in enumerate(trading_data):
    # Cumulatively sum up the total profits/losses and count of trading months
    total += month_pnl
    total_months += 1

    # Calculate the change in profits/losses
    if i > 0:
        change = month_pnl - trading_data[i-1][1]
        average_change += change
        
    # Logic to determine minimum and maximum values
    if change < greatest_decrease_amount:
            greatest_decrease_month = month
            greatest_decrease_amount = change
        elif change > greatest_increase_amount:
            greatest_increase_month = month
            greatest_increase_amount = change

# Calculate the average change
average_change /= (total_months - 1) if total_months > 1 else 1  # Avoid division by zero

# Print or use the calculated metrics as needed
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})")

