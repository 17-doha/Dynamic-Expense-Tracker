import os
import csv
import pandas as pd
from tkinter import *
from PIL import ImageTk, Image


def Username_validation(Name):  # Validate that the name is an alphabetic
    c = 0
    Name = Name.split(' ')
    for i in Name:
        if i.isalpha():
            c = c+1
    while c != len(Name):
        c = 0
        Name = input('Error! Enter a valid Name: ')
        for i in Name:
            if i.isalpha():
                c = c + 1
    return Name[0]


def Password_validation(Name, Password):  # make sure that password is valid (not a blank, not the same as username)
    while Password == Name:
        Password = input('Error! Your password must be different from your username: ')
    while Password == '':
        Password = input('Error! You must enter a Password: ')
    c=0
    for i in Password:
        if i != ' ':
            c=c+1
    while c!= len(Password):
        Password = input('Error! Enter a valid Password: ')
        c=0
        for i in Password:
            if i != ' ':
                c = c + 1
    return Password


def usernameexistance(Username):  # make sure of existance of a file with the name of the username
    if os.path.exists('%s.csv' % Username):
        return True
    else:
        return False


def Passwordexistance(Username, Password):  # Checks the existance of the password in the file if it exists return true else it returns false
    with open('%s.csv' % Username, 'r') as f:
        for line in f:
            if Password in line:
                return Password
        return False


def Choose1_from2_validation(choice):  # used in inputs that require one of two choices only to make sure user enters only one of these two inputs
    while choice != '1' and choice != '2':
        choice = input('Error! Enter a valid choice: ')
    return choice


def Choose1_from3_validation(choice):  # used in inputs that require one of three choices only to make sure user enters only one of these three inputs
    while choice != '1' and choice != '2' and choice != '3':
        choice = input('Error! Enter a valid choice: ')
    return choice


def Choose1_from_0_to_4_validation(Service):  # used to make sure the user chose one of the 4 services or chose 0 to close the program
    while Service != '0' and Service != '1' and Service != '2' and Service != '3' and Service != '4':
        Service = input('You choose an incorrect option. Please choose 0, 1 ,2, 3 or  4 :')
    return Service


def float_validation(num):  # Make sure user enters numbers only and taken as a float
    try:
        float(num)
        return positive_validation(float(num))
    except ValueError:
        num = float_validation(input('Error! Enter a valid num: '))
    return positive_validation(float_validation(float(num)))


def positive_validation(num):  # Take integer, Positive values only
    if int(num) > 0:
        return int(num)
    else:
        while int(num) < 0:
            num = int(input('Error! Enter a positive num: '))
        positive_validation(num)
        return num


def int_validation(num): # Make sure user enters numbers only and taken as an integers
    try:
        int(num)
        return positive_validation(int(num))
    except ValueError:
        num = input('Error! Enter a valid num: ')
    return positive_validation(int_validation(num))


def Report(Username):  # Prints a report to the user by his Expenses, and replace NaN with empty string
  df = pd.read_csv('%s.csv'%Username)
  df.fillna('', inplace = True)
  print(df.to_string())


fields = ['Username', 'Password', 'Budget','Saving','Limit']
fields2 = {'Type': 'Type', 'Price': 'Price', 'Date': 'Date'}


def New_user(Username, fields, fields2, Password, Budget, Saving, Limit):    # generate a new file with the user’s name and add the fields with its corresponding values and add the fields of Type, Price, Date

    with open('%s.csv' % Username,'w',newline='') as sheet:
        # This def function will be generated each time the user wnats to track his expenses so this will add his expenses to the file with his name
        csv_writer = csv.DictWriter(sheet, fieldnames=fields, delimiter=',')
        csv_writer2 = csv.DictWriter(sheet, fieldnames=fields2, delimiter=',')

        csv_writer.writeheader()
        csv_writer.writerow({'Username': Username, 'Password': Password, 'Budget': Budget, 'Saving': Saving, 'Limit': Limit})
        csv_writer2.writerow(fields2)


def Sign_in(Name):  # This function is called when user decides to sign in(Old User)
    if usernameexistance(Name) == True:
        x = input('Enter the password: ')
        if x == Passwordexistance(Name,x):
            print('Welcome ',Name,'Here are what we could offer to you..')
        else:
            while x != Passwordexistance(Name,x):
                x = input('Error! Please enter the correct password: ')
        while usernameexistance(Name) == False :
            Name = input('Error! Please enter the correct username: ')


def Sign_up(Name):  # This function is called when user decides to sign up(New User)
    while usernameexistance(Name) == True:
        Name = input("This one already exists, please enter another username: ")
    Password = Password_validation(Name,input('Enter your password: '))
    Budget = float_validation(input("Enter your budget: "))
    Saving = float_validation(input('Enter the amount of money you want to save: '))
    New_user(Name, fields, fields2, Password, float(Budget)-float(Saving), Saving, Limit(Budget,Saving))


def get_user_data(Username): #read csv file
  with open('%s.csv' % Username, 'r') as sheet:
    data_reader = csv.reader(sheet)
  return data_reader


def Append_price_type_date(Username, Type, Price, Date,):  # appends the data of the user as he tracks his expenses in the csv file #for old user
     with open('%s.csv' % Username, 'a', newline='') as sheet:
       writer = csv.DictWriter(sheet, fieldnames=[Type, Price, Date], delimiter=',',extrasaction='ignore')
       writer.writeheader()
       writer.writerow({'Type':Type,'Price':Price,'Date':Date})


def sub_from_budget(Name,Price,Budget):  # subtracts from the budget and returns the old and the new budget and the saving
    if float(Price) < float(Budget):
        Saving = float(specificdata(Name, 1, 3))
        NewBudget = float(Budget)-float(Price)
        Write_Edited(Name, Edit_user_data(Name, 1, 2, NewBudget))
        return [NewBudget,Budget,Saving]
    elif float(Price) > float(Budget):
        Budget = float(Budget) - float(Price)
        Saving = float(specificdata(Name, 1, 3))
        NewSaving = float(Saving) + float(Budget)
        Write_Edited(Name, Edit_user_data(Name, 1, 2, 0))
        Write_Edited(Name, Edit_user_data(Name, 1, 3, NewSaving))
        print(f'We have subtracted from your Saving and your Saving now is {NewSaving}')
        return [Saving,Budget,NewSaving]


def remove_user(Username):  # delete user
  if os.path.exists('%s.csv' % Username):
    os.remove('%s.csv' % Username)


def Edit_user_data(Username, row, column, new_value):  # reads the data from the file and convert it to a list of lists then change a specific value in it
  lines = []
  with open('%s.csv' % Username) as sheet:
    sheet = csv.reader(sheet)
    for line in sheet:
      lines.append(line)
  lines[row][column] = new_value
  return lines


def Write_Edited(Username, lines):  # writes the updated data again in the same file    `
 with open('%s.csv' % Username, "w+",newline='') as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(lines)


def specificdata(Username, row, column):  # gets a specific data from the csv file
    lines = []
    with open('%s.csv' % Username) as sheet:
      sheet = csv.reader(sheet)
      for line in sheet:
       lines.append(line)
    return lines[row][column]


def Limit(Budget, Saving):  # returns the limit per day
    limit=(float(Budget)-float(Saving))/30
    return limit


def specificdata2(Username):  # returns the data in form of list of lists
  lines = []
  with open('%s.csv'%Username) as sheet:
    sheet = csv.reader(sheet)
    for line in sheet:
      lines.append(line)
  return lines


def Sum_expenses_perday(Name):  # gets the sum of expenses for a specific date
 from datetime import date
 date = str(date.today())
 sum = 0
 for i in range(3,len(specificdata2(Name)), 2):
    if str(specificdata(Name, i, 2)) == date:
        sum += float(specificdata(Name, i, 1))
 return sum


def Sum_expenses(Name):  # gets the sum of expenses
    sum = 0
    for i in range(3, len(specificdata2(Name)), 2):
        sum += float(specificdata(Name, i, 1))
    return sum


def Message(Name):
    if float(specificdata(Name,1,4))-Sum_expenses_perday(Name) <= 10 and float(specificdata(Name,1,4))-Sum_expenses_perday(Name) >= 0:  # approach the limit
        print('WARNING! you are about to exceed your daily limit')
    elif Sum_expenses_perday(Name) > float(specificdata(Name,1,4)): # greater than the limit
        print('WARNING! you have exceeded your daily limit')
        root = Tk()
        root.title('Dynamic Expense Tracker')
        my_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Doha\Desktop\Comic.jpg"))
        my_label = Label(image=my_img)
        my_label.pack()
        root.mainloop()
