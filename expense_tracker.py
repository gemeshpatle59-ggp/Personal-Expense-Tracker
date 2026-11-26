from datetime import date
import json
import os


class Expance:
    def __init__(self):
        if os.path.exists("expenses.json"):
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)
        else:
            self.expenses = []



    def save_expense(self):
        with open("expenses.json","w") as file:
            json.dump(self.expenses,file,indent=4)
                
    def add_expance(self,amount,category,description):
        if self.expenses:
            new_id =  max(expense["id"] for expense in self.expenses) + 1
        else:
            new_id = 1
        self.expenses.append({
            "id": new_id,
            "amount" : amount,
            "category" : category,
            "description" : description,
            "date" : str(date.today())

        })
        print("\nnew expense is added......\n")
        

    def see_expanses(self):
        print("\n===== PERSONAL EXPENSE TRACKER =====")

        for expenses in self.expenses:
            print(f"\nid : {expenses['id']}")
            print(f"amount : {expenses['amount']}")
            print(f"category : {expenses['category']}")
            print(f"description : {expenses['description']}")
            print(f"date : {expenses['date']}")            


    def total_expance(self):
        total = 0
        print('\n--- Total expenses is,,,')
        for expenses in self.expenses:
            total += expenses["amount"]
        print(total)

    def  cate_wise_expances(self):
        total = 0
        print("\n ----- Category Wise Expenses")
        for expense in self.expenses:
            total += expense["amount"]
            print(f"{expense["category"]} : {expense["amount"]}")
        print(f"total : {total}")    
        print("\n.....")

    def update_espense(self,n,amount):
        for expenses in self.expenses:
            if expenses["id"] == n:
                expenses["amount"] = amount
                print("expenses updated..")
                print("\n...")
                break
        else:
            print("Expense id not found")

    def del_expense(self,n):
        for expense in self.expenses:
            if expense["id"] == n:
                self.expenses.remove(expense)
                print("Expense deleted")
                break

        else:
            print("id not found ") 

a1 = Expance()

print("\n====================================")
print("===== PERSONAL EXPENSE TRACKER =====")
print("====================================")
print("\n....")

while True:
    print("\n1.TO ADD Your Expenses")
    print("2.To See Your Expenses")
    print("3.To See the Category Wise Expensews")
    print("4.To See The Total Expenses")
    print("5.To Update the Expenses")
    print("6.To delete Your expenses")
    print("7.To Exist")
    print("\n.....")
    

    choice = input("enter your choice from ( 1 to 7)..: ")

    try:
        if choice == "1":
            a = int(input("Enter the amount you spent..: "))
            c = input("Enter on which you spend your amount..: ")
            d = input("What did you buy with the amount..: ")

            a1.add_expance(a,c,d)
            a1.save_expense()

        elif choice == "2":
            a1.see_expanses()

        elif choice == "3":
            a1.cate_wise_expances()   

        elif choice == "4":
            a1.total_expance()

        elif choice == "5":
            n = int(input("enter ths id no. of expense to update..: "))
            amt = int(input("\nEnter amount to update..: "))
            a1.update_espense(n,amt)
            a1.save_expense()

        elif choice == "6":
            n = int(input("Enter id of expense to delete..: "))
            a1.del_expense(n)
            a1.save_expense()
            # print("expense is deleted.")


        elif choice == "7":
            print("-----thank you ----")       
            print("\n.....") 
            break

        else:
            print("check the choice properly ...")

    except ValueError:
        print("something went wrong")
        
