import os
import csv


Pybank1 = os.path.join('raw_data','budget_data_1.csv')

#create the txt file
Pybank1summary = os.path.join('raw_data','budget1_summary.txt')


# just trying it another way
Total_Months = sum(1 for line in open(Pybank1)) - 1


# begining variables
Total_Revenue = 0
change_list = []
month_to_month_Change = []
last_month = 0
greatest_increase = []
greatest_decrease = []

#read original csv
with open(Pybank1) as data:
    csvreader = csv.DictReader(data)

    for row in csvreader:
        
        #Total Revenue
        Total_Revenue =  Total_Revenue + (int(row['Revenue']))
        
        # monthly average change
        current_change = int(row['Revenue']) - last_month
        last_month = int(row['Revenue'])
        change_list = change_list + [current_change]
        month_to_month_Change = month_to_month_Change + [row['Date']]

               
#answering average revenue 
Average_revenue = sum(change_list) / len(change_list)



greatest_increase = max(change_list)
greatest_decrease = min(change_list)


#  I COULDNT FIGURE OUT HOW TO ADD THE MONTH OF THE CHANGE...

# changes = zip(month_to_month_Change,change_list)

# for change in changes:
#     if max_increase == changes[1]:
#         greatest_increase[0] = changes[0]
#         greatest_increase[1] = changes[1]
        
#     elif max_decrease == changes[1]:
#         greatest_decrease[0] = changes[0]
#         greatest_decrease[1] = changes[1]


#didn't get around to changing number formats such as rounding
Answers = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {Total_Months}\n"
    f"Total Revenue: ${Total_Revenue}\n"
    f"Average Revenue Change: ${Average_revenue}\n"
    f"Greatest Increase in Revenue: (${greatest_increase})\n"
    f"Greatest Decrease in Revenue: (${greatest_decrease})\n")


print(Total_Months)
print(Total_Revenue)
print(Average_revenue)
print(greatest_increase)
print(greatest_decrease)



#create/populate the txt file
with open(Pybank1summary, "w") as txt_file:
    txt_file.write(Answers)

             