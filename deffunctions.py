import os
import csv
import pandas as pd
from tkinter import *
from PIL import ImageTk, Image


def Username_validation(Name):  # Validate that the name is an alphabetic



def Password_validation(Name, Password):  # make sure that password is valid (not a blank, not the same as username)



def usernameexistance(Username):  # make sure of existance of a file with the name of the username



def Passwordexistance(Username, Password):  # Checks the existance of the password in the file if it exists return true else it returns false



def Choose1_from2_validation(choice):  # used in inputs that require one of two choices only to make sure user enters only one of these two inputs
 


def Choose1_from3_validation(choice):  # used in inputs that require one of three choices only to make sure user enters only one of these three inputs



def Choose1_from_0_to_4_validation(Service):  # used to make sure the user chose one of the 4 services or chose 0 to close the program



def float_validation(num):  # Make sure user enters numbers only and taken as a float



def positive_validation(num):  # Take integer, Positive values only


def int_validation(num): # Make sure user enters numbers only and taken as an integers



def Report(Username):  # Prints a report to the user by his Expenses, and replace NaN with empty string



fields = ['Username', 'Password', 'Budget','Saving','Limit']
fields2 = {'Type': 'Type', 'Price': 'Price', 'Date': 'Date'}


def New_user(Username, fields, fields2, Password, Budget, Saving, Limit):    # generate a new file with the user’s name and add the fields with its corresponding values and add the fields of Type, Price, Date




def Sign_in(Name):  # This function is called when user decides to sign in(Old User)



def Sign_up(Name):  # This function is called when user decides to sign up(New User)



def get_user_data(Username): #read csv file



def Append_price_type_date(Username, Type, Price, Date,):  # appends the data of the user as he tracks his expenses in the csv file #for old user



def sub_from_budget(Name,Price,Budget):  # subtracts from the budget and returns the old and the new budget and the saving



def remove_user(Username):  # delete user



def Edit_user_data(Username, row, column, new_value):  # reads the data from the file and convert it to a list of lists then change a specific value in it



def Write_Edited(Username, lines):  # writes the updated data again in the same file    `



def specificdata(Username, row, column):  # gets a specific data from the csv file



def Limit(Budget, Saving):  # returns the limit per day



def specificdata2(Username):  # returns the data in form of list of lists
 


def Sum_expenses_perday(Name):  # gets the sum of expenses for a specific date



def Sum_expenses(Name):  # gets the sum of expenses



def Message(Name):
 
