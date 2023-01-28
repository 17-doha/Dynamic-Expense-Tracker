import deffunctions
from datetime import date
Service = '-1'
print('Hello to your Dynamic Expense Tracker\nWe wish you have great time with our service\nHave a good day ^^')
Name = deffunctions.Username_validation(input('Enter your name: '))  # User enter his name and must be valid according to valdiation func (Do not contain numbers)
print('1.sign up\n2.sign in')
choice = deffunctions.Choose1_from2_validation(input('Choose 1 or 2: '))  # User choose on of the two choices to sign up or sign in
if choice == '1':
    deffunctions.Sign_up(Name)  # Calling the sign up function to take the needed inputs from the user
    print('Please sign in again')
    deffunctions.Sign_in(Name)  # Calling the sign in function to check the username and password existance to allow the user to log in
else:
    deffunctions.Sign_in(Name)  # Calling the sign in function to check the username and password existance to allow the user to log in
while Service != '0':
        print('Choose 1 if you want to Update your data')
        print('Choose 2 if you want to Track your Expense')
        print('Choose 3 if you want to show your Report')
        print('Choose 4 if you want to delete your account')
        print('Choose 0 if you want to Exit the Program')
        Service = deffunctions.Choose1_from_0_to_4_validation(input('Enter your Service: '))  # Asks the user to enter his choice and checks if the user enters one of the 4 choices
        if Service == '0':
            print('Exiting the program..')
            break
        if Service == '1':
            print('Choose 1 if you want to update your budget')
            print('Choose 2 if you want to update your amount of money you want to save')
            Choice = deffunctions.Choose1_from2_validation(input('Enter your Choice: '))  # Asks the user to enter his choice and checks if the user enters one of the 2 choices
            if Choice == '1':
                Budget = deffunctions.float_validation(input("Enter your New Budget: ")) - float(deffunctions.specificdata(Name, 1, 3))  # Asks the user to enter his budget and validate float or integer only
                deffunctions.Write_Edited(Name, deffunctions.Edit_user_data(Name, 1, 2, Budget))  # writes the new budget on the csv file
                deffunctions.Write_Edited(Name, deffunctions.Edit_user_data(Name, 1, 4, deffunctions.Limit(
                    float(Budget)+float(deffunctions.specificdata(Name, 1, 3)),
                    float(deffunctions.specificdata(Name, 1, 3)))))
                # Calculates the limit again and write it in the csv file
                print(f'Your budget is updated successfully!\n Your budget now is {Budget}')
            elif Choice == '2':
                Saving = deffunctions.float_validation(input("Enter your amount of money you want to save: "))  # Validate Float only
                Budget = float(deffunctions.specificdata(Name, 1, 2)) + float(deffunctions.Sum_expenses(Name)) - float(Saving)
                deffunctions.Write_Edited(Name, deffunctions.Edit_user_data(Name, 1, 3, Saving))  # Write the new Savings after updating it on the csv file
                deffunctions.Write_Edited(Name, deffunctions.Edit_user_data(Name, 1, 2, Budget))   # Write the new budget after updating the saving on the csv file
                deffunctions.Write_Edited(Name, deffunctions.Edit_user_data(Name, 1, 4, deffunctions.Limit(
                    float(Budget) + float(deffunctions.specificdata(Name, 1, 3)),
                    float(deffunctions.specificdata(Name, 1, 3)))))
                # Calculates the limit again and write it in the csv file
                print(f'Your amount of money you want to save is updated successfully!\n Your amount of money you want to save is {Saving}')
        elif Service == '2':
            print(f'Your limit expense per day is {float(deffunctions.specificdata(Name,1,4))}')
            Type = input("Enter the type of your expense: ")
            Price = deffunctions.float_validation(input("Enter the price: "))  # Asks the user to enter the type of his expense
            Date = date.today()  # Adds the date of which the user is using the program
            deffunctions.Append_price_type_date(Name, Type, Price, Date)  # Writes the data on the csv file
            deffunctions.sub_from_budget(Name, Price, deffunctions.specificdata(Name, 1, 2))  # Subtracts the price from the main budget
            print(f'You spent {Price} on {Type} and your budget now is {deffunctions.specificdata(Name, 1, 2)}')
            deffunctions.Message(Name)
        elif Service == '3':
            print('Here is your report')
            deffunctions.Report(Name)
            deffunctions.Message(Name)
        elif Service == '4':
            print('Your File is successfully removed')
            deffunctions.remove_user(Name)  # We do not need to check existance of the file as this is an old user so he already exists
            break
