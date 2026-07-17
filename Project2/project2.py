# Expense Tracker

print("====== Expense Tracker ======")

total = 0

while True:
    expense = float(input("Enter expense amount: Rs. "))
    total =total+ expense

    choice = input("Do you want to add another expense? (yes/no): ").lower()

    if choice != "yes": #THIS MEANS THE CHOICE WAS NO BY THE USER
        break

print("\n===== Expense Summary =====")
print(f"Total Spent: Rs. {total:.2f}") #UPTO 2 DP
print("Thank you for using Expense Tracker!")
