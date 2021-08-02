import sys
import os
import time
from datetime import date
import random
from random import randint
import database
from frontend import *
from database import *



class BackEnd():

    def __init__(self):
        # Check whether database file is present or not

        self.check_database = os.path.isfile('./bank_database.csv')

        if self.check_database == False:
            New_User_DataBase.create_new(self)

    def new_user(self, nu_name, nu_age, nu_password, nu_deposit):
        self.name = nu_name
        self.age = int(nu_age)

        # Calling age_check() method to validate the age entered by the user

        self.age_check_result = self.age_check(self.age)

        # Ask the user to create a password 

        self.bank_password = nu_password

        # Generating a 9-digit account number for the user  

        self.generated_account_number = random.randint(100000000, 999999999)
        self.string_account_number = str(self.generated_account_number)
        a = self.string_account_number[:3]
        b = self.string_account_number[3:6]
        c = self.string_account_number[6:9]
        self.final_account_number = a + " " + b + " " + c

        # Generating a 3-digit CVV for the user (Remember to keep your CVV secret :D ) 

        self.cvv = random.randint(100, 999)

        # Asking the user to input a amount which has to be deposited into tha account

        self.deposited_amount = int(nu_deposit)

        # Calling amt_check() method to validate if the amount entered by the user is greater than minimum or not

        self.amt_check_result = self.amt_check(self.deposited_amount)

        # Determining date and time of successful deposit

        self.today = date.today()
        t = time.localtime()
        self.current_time = time.strftime("%H:%M:%S", t)

        # Passing the values to DataBase script for adding the new user to data base

        if self.age_check_result and self.amt_check_result is True:
            New_User_DataBase.existing_database(self, self.name, self.age, self.bank_password,
                                                self.final_account_number, self.deposited_amount, self.cvv, self.today,
                                                self.current_time)
            account_created_successfully(self.final_account_number, self.cvv, self.deposited_amount)
        elif self.age_check_result is True and self.amt_check_result is False:
            deposit_error()
        elif self.age_check_result is False and self.amt_check_result is True:
            age_error()

    # A method for validating the age entered by the user    

    def age_check(self, age):
        if age < 16:
            return False
        else:
            pass

        return True

    def amt_check(self, deposited_amount):
        if deposited_amount < 1000:
            return False
        else:
            pass

        return True

    def existing_user(self, name, acc_no, password):
        self.ex_check_database = os.path.isfile(f"./user_db/{name}_{acc_no}_{password}.csv")
        # print(self.ex_check_database)
        if self.ex_check_database is True:
            login_validated()
        else:
            login_failure()




