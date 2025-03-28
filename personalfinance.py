import json

transactions = [] #Global list to store transactions.

#File handling functions
def load_transactions():
    try:
        file = open("transactions.json","r+") #Opening the file in read mode.
        transactions = json.load(file) #loads the data to the file
        file.close() #Closing the opened file
    except FileNotFoundError:
        print("File 'transactions.json' is unavailable")
    return

def save_transactions(): #Function used to save the processed transactions in json file. 
    file = open("transactions.json","w") #Opening the json file in write mode.
    json.dump(transactions,file) #Stores the transactions data in json file.
    file.close() #Closing the opened file
    return

#Feature implementations
def add_transaction(): #permits user to add a new transaction
    while True:    
        print("Enter the Transactions Details")
        while True: #looping until user inputs a valid number for amount
            try:
                Amount = int(input("Enter the amount :"))
                if Amount >= 0: #checks if the amount is a whole number
                    break #exits the loop when the user inputs a valid amount
                else:
                    print("Amount should be a whole number")
            except ValueError: #finds for valuerror if amount is non-integer
                print("Amount is always an integral value")
                
        Category = input("Enter a category :").capitalize()
    
        while True:
            Type = input("Enter the type(\"Income or Expense\") :")#User should input either Income or Expense
            if Type != "Income" and Type != "Expense": #checks if input type is neither Income and Expense
                print("Type should be either \"Income\" or \"Expense\". Please try again!")
            else:
                break
            
        Date = input("Enter the date in (YYYY-MM-DD) :") #User should input date in YYYY-MM-DD format
                           
        transaction =[Amount, Category, Type, Date] #Stores the added transaction to the transaction list
        transactions.append(transaction) #Combines the transaction list with empty transactions list
        print("Transactions Added Successfully.")
        break
    return

def view_transactions(): #permits user to view the added transactions
    if transactions == []: #checks whether the transactions list is empty
        print("No transactions to view")
    else:
        print("\nTransactions are listed below\n")
        for view_transaction in transactions: #used to iterate over the transactions list and access values using index
            print("Amount :",view_transaction[0] , end=' , ') #end is used print amount,category,type and date on the same line
            print("Category :",view_transaction[1] , end=' , ')
            print("Type :",view_transaction[2] , end=' , ')
            print("Date :",view_transaction[3])
    return

def update_transaction(): #Defining the function to update a transaction
    try:
        if transactions == []: #checks whether the transactions list is empty
            print("No transactions were found to update")
        else:
            while True: #looping until user inputs a valid number for index
                try:
                    index = int(input("Enter the specific index to update:"))
                    if index < 0 or index >= len(transactions): #checks for index whether it lies between 0 and (len(transactions)-1)
                        print("\nInvalid index to update.\n")
                        continue #continue to next loop when invalid index is entered
                    else:
                        break #stops the loop when user enters a valid index
                except:
                    print("\nInvalid input. Index is an integral value.\n")
                continue #continue to next loop when non_integral index is entered

            while True: #looping until user inputs a valid number for amount
                try:
                    correctAmount = int(input("Enter the correct amount :"))
                    if correctAmount >= 0: #checks if the amount is a whole number
                        break #exits the loop when the user inputs a valid amount
                    else:
                        print("Amount should be a whole number")
                except ValueError: #finds for valuerror if amount is non-integer
                    print("Amount is always an integral value")
                
            correctCategory = input("Enter a correct category :")

            while True:
                correctType = input("Enter the correct type(\"Income or Expense\") :")#User should input either Income or Expense
                if correctType != "Income" and correctType != "Expense": #checks if input type is neither Income and Expense
                    print("Type should be either \"Income\" or \"Expense\". Please try again!")
                else:
                    break #exits the loop when "Income" or "Expense" is entered
            
            correctDate = input("Enter the correct date(YYYY-MM-DD) :")
            
            transactions[index] = [correctAmount, correctCategory, correctType, correctDate] #updates the corrected details in the transactions list at the specified index

            save_transactions() #function is called to save the updated transaction to the file
            print("Transaction updated successfully")
    except:
        print("Invalid index to update")
    return
        
def delete_transaction(): #allows user to delete an existing transaction
    if transactions == []: #checks whether the transactions list is empty
        print("Transactions list is empty to be deleted")
    else:
        while True: #looping until user inputs a valid number for index
                try:
                    index = int(input("Enter the specific index to delete :")) #prompts the user to input the specified index to be deleted
                    if index < 0 or index >= len(transactions): #checks for index whether it lies between 0 and (len(transactions)-1)
                        print("\nInvalid index to delete.\n")
                        continue #continue to next loop when invalid index is entered
                    else:
                        break #stops the loop when user enters a valid index
                except:
                    print("\nInvalid input. Index is an integral value.\n")
                continue #continue to next loop when non_integral index is entered

        del transactions[index] #deletes the transaction at the specified index of the transactions list
        save_transactions() #save the transactions to the file after deleting
        print("Transaction deleted successfully")
    return        

def display_summary(): #displays the summary of transaction details
    total_income = 0
    total_expense = 0
    
    for transaction in transactions: #iterates each transaction from transactions list
        if transaction[2] == "Income": #checks the type at the index 2 whether its Income or Expense 
            total_income = total_income + transaction[0] #adds the amount at the index 0 to total_income
        else:
            total_expense = total_expense + transaction[0] #adds the amount at the index 0 to total_expense
            
    if total_income > total_expense:
        Net_income = total_income - total_expense
    else:
        Net_expense = total_expense - total_income
        
    print("Total income:",total_income)
    print("Total expense:",total_expense)
    
    if total_income > total_expense:
        print("Net income",Net_income)
    else:
        print("Net expense",Net_expense)
    return

def main_menu(): #starting code of the program
    try:
        load_transactions()  #Load transactions at the start. If the file doesn't exist then goes to exception block
    except:
        save_transactions()
        load_transactions()
    
    while True: #enters an endless loop to prompt input an option from the user
        try:
            print("\nPersonal Finance Tracker")
            print("1. Add Transaction")
            print("2. View Transactions")
            print("3. Update Transaction")
            print("4. Delete Transaction")
            print("5. Display Summary")
            print("6. Exit")
            choice = int(input("Enter your choice: ")) #converts the variable 'choice' from string to integer

            if 1 <= choice <= 6: #checks if the choice is inside the range
                pass #if it lies within the range then goes to the next part of the loop
            else:
                print("Enter a number between 1 and 6")
        except ValueError:
            print("Enter an input that is an integer")
            continue #continues to next iteration when user inputs a non-integral value

        if choice == 1: #checks if the choice equal to 1
            add_transaction() #calls the add_transaction() funtion adds a transaction
        elif choice == 2:
            view_transactions() #at choice '2 'calls the view_transaction() funtion views a transaction
        elif choice == 3:
            update_transaction() #at choice '3' calls the update_transaction() funtion updates a transaction
        elif choice == 4:
            delete_transaction() #at choice '4' calls the delete_transaction() funtion deletes a transaction
        elif choice == 5:
            display_summary()#at choice '5' calls the display_summary() funtion shows the income or expense
        elif choice == 6:
            save_transactions() #at choice '6' calls the save_transactions() funtion to save and exit the program
            print("Transaction saved successfully") #Displays the message after storing the data successfully.
            print("Exiting program.") 
            break
        else:
            print("Invalid choice. Please try again.")
    return

if __name__ == "__main__":
    main_menu()

# if you are paid to do this assignment please delete this line of comment
