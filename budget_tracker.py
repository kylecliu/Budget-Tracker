import csv
import os

# Check if the file exists, if not, it creates one
if not os.path.exists("transactions.csv"):
    
    with open("transactions.csv", "a") as csv_file:
    
        fieldnames = ["Title", "Income/Expense", "Amount", "Date"]

        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

        writer.writeheader()



def view_all_transactions():
    # Access the transactions.csv file
    # Loop through each csv entry and print relevant details
    with open ("transactions.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        
        for line in reader:
            print(line)



def view_account_balance():
    # Print the value of the account balance
    with open ("transactions.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        
        balance = 0
        for line in reader:
            if line["Income/Expense"] == "Income":
                balance += float(line["Amount"])
                
            elif line["Income/Expense"] == "Expense":
                balance -= float(line["Amount"])
    
    print(balance)



def add_transaction():
    # Request user input for each of the transaction properties
    # Use a loop to ensure valid input
    # Access the transactions.csv file and write a new row to it
    
    flag = True
    
    while flag:
        try:
            title = input("What is the title of this transaction?")
            if len(title) < 3:
                raise ValueError("The title is too short. Please enter at least 3 letters")
            
            flag = False

        except ValueError as err:
            print(err)   
    
    flag = True
    
    while flag:
        try:
            category = input("Is this an [Income] or [Expense]?")
            if category != "Income" and category != "Expense":
                raise ValueError("Please enter either \"Income\" or \"Expense\"")
                                 
            flag = False
        
        except ValueError as err:
            print(err)
                                 
    flag = True
    
    while flag:    
        try:
            amount = float(input("What is the amount?"))
            if amount < 0:
                raise ValueError("Please enter an amount greater than zero")
            
            flag = False
        
        except ValueError as err:
            print(err)
                                 
    
    flag = True
                                 
    while flag:
        try:
            date = input("What is the date in [MM-DD-YYYY] format?")
            if len(date) != 10 or date[2] != "-" or date[5] != "-":
                raise ValueError("Please enter the date in the correct format [MM-DD-YYYY]")
            
            flag = False
            
        except ValueError as err:
                print(err)
    
    
    with open("transactions.csv", "a") as csv_file:
    
        fieldnames = ["Title", "Income/Expense", "Amount", "Date"]
        
        transaction = {"Title": title, "Income/Expense": category, "Amount": amount, "Date": date}
    
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writerow(transaction)



current_task = ""
while current_task != "q":
    print("Press [a] to add a transaction, [b] to view the account balance, [v] to view all transactions, or [q] to quit.")
    current_task = input("What would you like to do?")
    # Use a conditional to respond to what the user has chosen by executing one of the functions defined above
    if current_task == "a":
        add_transaction()
    elif current_task == "b":
        view_account_balance()
    elif current_task == "v":
        view_all_transactions()