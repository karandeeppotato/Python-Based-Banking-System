import pandas as pd
import frontend
from frontend import *
import time
from datetime import date
import glob
import os
import re


class New_User_DataBase():
    def create_new(self):
        bank_dic = {"Name": "", "Age": "", "Password": "", "Account Number": "", "CVV": "", "Amount": "", "Date": "",
                    "Time": ""}
        bank_df = pd.DataFrame(bank_dic, index=[0])
        bank_df.to_csv("bank_database.csv", index=False)

    def existing_database(self, name, age, bank_password, acc_no, amt, cvv, today, current_time):
        bank_dic_updated = {"Name": name, "Age": age, "Password": bank_password, "Account Number": acc_no, "CVV": cvv,
                            "Amount": amt, "Date": today, "Time": current_time}
        bank_df_updated = pd.DataFrame(bank_dic_updated, index=[0])
        bank_df_updated.to_csv("bank_database.csv", mode="a", header=False, index=False)
        balance = amt
        # with_amt = 0
        user_dic = {"Name": name, "Account number": acc_no, "Previous Amount": 0,
                    "Process": "New Account First Deposit",
                    "Amount Change": f"+{amt}", "Balance": balance, "Date": today, "Time": current_time}
        user_dic = pd.DataFrame(user_dic, index=[0])
        user_dic.to_csv(f"user_db/{name}_{acc_no}_{bank_password}.csv", mode='a', index=False)


class Existing_User_DataBase():
    def withdraw_update(self, name, acc_no, password, withdraw_amt):
        ex_user_df = pd.read_csv(f"./user_db/{name}_{acc_no}_{password}.csv")
        last_balance = ex_user_df["Balance"].iloc[-1]
        last_balance = int(last_balance)
        withdraw_amt = int(withdraw_amt)
        if last_balance < withdraw_amt:
            withdraw_error()
        else:
            today = date.today()
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            updated_balance = last_balance - withdraw_amt
            ex_user_dic = {"Name": name, "Account number": acc_no, "Previous Amount": last_balance,
                           "Process": "Withdrawal",
                           "Amount Change": f"-{withdraw_amt}", "Balance": updated_balance, "Date": today,
                           "Time": current_time}
            ex_user_dic = pd.DataFrame(ex_user_dic, index=[0])
            ex_user_dic.to_csv(f"./user_db/{name}_{acc_no}_{password}.csv", mode='a', index=False, header=False)
            withdraw_successful(updated_balance)

    def deposit_update(self, name, acc_no, password, deposit_amt):
        ex_user_df = pd.read_csv(f"./user_db/{name}_{acc_no}_{password}.csv")
        last_balance = ex_user_df["Balance"].iloc[-1]
        last_balance = int(last_balance)
        deposit_amt = int(deposit_amt)
        today = date.today()
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        updated_balance = last_balance + deposit_amt
        plus = "+"
        ex_user_dic = {"Name": name, "Account number": acc_no, "Previous Amount": last_balance,
                       "Process": "Deposit",
                       "Amount Change": f"{plus}{deposit_amt}", "Balance": updated_balance, "Date": today,
                       "Time": current_time}
        ex_user_dic = pd.DataFrame(ex_user_dic, index=[0])
        ex_user_dic.to_csv(f"./user_db/{name}_{acc_no}_{password}.csv", mode='a', index=False, header=False)
        deposit_successful(updated_balance)

    def send_amt(self, from_name, from_accno, from_passkey, amt_send, to_name, to_accno):
        ex_user_df = pd.read_csv(f"./user_db/{from_name}_{from_accno}_{from_passkey}.csv")
        to_file_path = glob.glob(f"./user_db/{to_name}_{to_accno}_*.csv")
        to_file_path_str = to_file_path[0]
        # print(to_file_path_str)
        to_user_df = pd.read_csv(to_file_path_str)
        to_last_balance = to_user_df["Balance"].iloc[-1]
        last_balance = ex_user_df["Balance"].iloc[-1]
        last_balance = int(last_balance)
        amt_send = int(amt_send)
        if last_balance < amt_send:
            withdraw_error()
        else:
            today = date.today()
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            from_updated_balance = last_balance - amt_send
            to_updated_balance = to_last_balance + amt_send
            from_user_dic = {"Name": from_name, "Account number": from_accno, "Previous Amount": last_balance,
                             "Process": f"Amount Send to {to_name}",
                             "Amount Change": f"-{amt_send}", "Balance": from_updated_balance, "Date": today,
                             "Time": current_time}
            from_user_dic = pd.DataFrame(from_user_dic, index=[0])
            from_user_dic.to_csv(f"./user_db/{from_name}_{from_accno}_{from_passkey}.csv", mode='a', index=False, header=False)
            plus = "+"
            to_user_dic = {"Name": to_name, "Account number": to_accno, "Previous Amount": to_last_balance,
                           "Process": f"Amount recieved from {from_name}",
                           "Amount Change": f"{plus}{amt_send}", "Balance": to_updated_balance, "Date": today,
                           "Time": current_time}
            to_user_dic = pd.DataFrame(to_user_dic, index=[0])
            to_user_dic.to_csv(to_file_path_str, mode='a', index=False, header=False)
            send_amount_successful()
