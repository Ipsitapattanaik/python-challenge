import csv #Import csv module

with open ('PyBank/ Resources/budget_data.csv') as csvfile: #Start csv file handling

    csvreader=csv.reader(csvfile, delimiter=',') #Specify delimiter and variable that holds contents
    header=next(csvreader) #Read the header row first

    #Variables declaration
    months=[] #Generate list for the "Date" column
    prolosses=[] #Generate list for the "Profit/Losses" column

    #Set start conditions
    total=0
    amt_change=0
    mon_change=0
    mon_count=0
    incProfit=0
    decProfit=0
    delta_line1=0
    delta_line2=0
    loop1=0
    loop2=0

    #The total number of months included in the dataset
    #Read in each row of data and write data into lists above
    for row in csvreader:
        month=row[0] #Assign column 0 as month
        proloss=row[1] #Assign column 1 as proloss
        months.append(month) #Add next line to list months
        prolosses.append(proloss) #Add next line to list prolosses
    
    mon_count = len(months) #Count total of months from "Date" column
    #print(mon_count)

    #Begin data analysis

#The net total amount of "Profit/Losses" over the entire period
#First loop is through list prolosses (variable loop1 as loop index counter)
for loop1 in range (mon_count):
    total=total+int(prolosses[loop1]) #Calculate total amount
#print(total)

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#Second loop is through list prolosses (variable loop2 as loop index counter)
for loop2 in range (mon_count-1): #Restrict loop to avoid overflow (last line +1)
    amt_change=amt_change+(float(prolosses[loop2+1])-float(prolosses[loop2])) #Calculate sum of changes
#print(a_change/(mon_count-1))

    mon_change=(float(prolosses[loop2+1])-float(prolosses[loop2])) #Calculate monthly change
    #Determine greatest increase
    if mon_change>incProfit: 
        incProfit=mon_change
        delta_line1=loop2
    else:
        incProfit=incProfit

#print(incProfit)

#print(months[delta_line1+1])

    #Determin greatest decrease
    if mon_change<decProfit: 
        decProfit=mon_change
        delta_line2=loop2
    else:
        decProfit=decProfit

#print(decProfit)

#print(months[delta_line2+1])

#generate output lines

print_analysis=f'\
Financial Analysis\n\
----------------------------\n\
Total Months: {mon_count}\n\
Total Amount: ${total}\n\
Average Change: ${round(amt_change/(mon_count-1),2)}\n\
Greatest Increase in Profits: {months[delta_line1+1]} (${int(incProfit)})\n\
Greatest Decrease in Profits: {months[delta_line2+1]} (${int(decProfit)})\n'

print(print_analysis) #results on screen

#Write into text file named pybank.txt

file1=open("pybank.txt","w") #Open or create file under analisis folder
file1.writelines(print_analysis) #Write analysis to pybank.txt
file1.close() #Close pybank.txt