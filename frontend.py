from backend import *
import tkinter as tk
import tkinter.ttk as ttk
import csv
from tkinter import *
import database


def main_menu():
    mm_window = Tk()
    mm_window.title("Bank Main Menu")
    mm_window.geometry("700x400")
    mm_window.config(bg='#FFBCBC')
    photo = PhotoImage(file = "./icon/favicon.png")
    mm_window.iconphoto(False, photo)

    # Setting and placing up the introduction label

    intro_label = Label(mm_window, text='Python based Banking System', width=57, height=2, fg='black', bg='#F8485E',
                        relief=tk.FLAT, borderwidth=6)
    intro_label.config(font=('Helvetica', 15, 'bold'))
    intro_label.place(x=1, y=1)

    new_user_button = Button(mm_window, text=' Click to apply for new account ', fg='Black', bg='#FF9642',
                             command=new_user_window)
    new_user_button.config(font=('Helvetica', 10, 'bold'))
    existing_user_button = Button(mm_window, text=' Click here if you are an existing user ', fg='Black', bg='#FF9642',
                                  command=existing_user)
    existing_user_button.config(font=('Helvetica', 10, 'bold'))
    exit_button = Button(mm_window, text=' Exit ', fg='Black', bg='red', command=mm_window.destroy)
    exit_button.config(font=('Helvetica', 10, 'bold'))

    new_user_button.place(x=235, y=250)
    existing_user_button.place(x=214, y=290)
    exit_button.place(x=600, y=350)


def new_user_window():
    nu_window = Tk()
    nu_window.title('Apply for new account')
    nu_window.geometry("700x400")
    nu_window.config(bg='#FFBCBC')

    def submit_data():
        nu_name = nu_name_field.get()
        nu_age = nu_age_field.get()
        nu_password = nu_password_field.get()
        nu_deposit = nu_deposit_field.get()
        BackEnd.new_user(BackEnd(), nu_name, nu_age, nu_password, nu_deposit)

    # Name label and entry field

    Label(nu_window, text="Name :", fg='Black', bg='#F8485E', relief=tk.FLAT).place(x=74, y=250)
    nu_name_field = Entry(nu_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER)
    nu_name_field.place(x=122, y=250)

    # Age label and entry field

    Label(nu_window, text="Age : ", fg='Black', bg='#F8485E', relief=tk.FLAT).place(x=78, y=300)
    nu_age_field = Entry(nu_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER)
    nu_age_field.place(x=122, y=300)

    # Create_Password label and field 

    Label(nu_window, text="Create Password :", fg='Black', bg='#F8485E', relief=tk.FLAT).place(x=350, y=250)
    nu_password_field = Entry(nu_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER, show='⚈')
    nu_password_field.place(x=452, y=250)

    # Deposit_Amount label and field

    Label(nu_window, text="Deposit Amount : ", fg='Black', bg='#F8485E', relief=tk.FLAT).place(x=345, y=300)
    nu_deposit_field = Entry(nu_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER)
    nu_deposit_field.place(x=452, y=300)

    # Creating a submit button

    Button(nu_window, text="Click to Submit", fg='Black', bg='#79D70F', command=submit_data).place(x=520, y=350)
    Button(nu_window, text="Back", fg='Black', bg="red", command=nu_window.destroy).place(x=630, y=350)


def age_error():
    age_err_window = Tk()
    age_err_window.title('Age Error !!')
    age_err_window.geometry("700x80")
    age_err_label = Label(age_err_window, text="Age Error : you should be at least 16 year old to open a new account",
                          fg="red", bg='yellow')
    age_err_label.place(x=149, y=30)
    age_err_window.config(bg='#FFBCBC')


def deposit_error():
    deposit_err_window = Tk()
    deposit_err_window.title('Amount Deposit Error !!')
    deposit_err_window.geometry("700x80")
    deposit_err_label = Label(deposit_err_window, text="Amount Deposit Error : Minimum deposit amount is $1000",
                              fg="red", bg="yellow")
    deposit_err_label.place(x=165, y=30)
    deposit_err_window.config(bg='#FFBCBC')


def account_created_successfully(accno, cvv, amt):
    acc_created_successfully_window = Tk()
    acc_created_successfully_window.title("Account Created Successfully !! ")
    acc_created_successfully_window.geometry("700x400")
    acc_created_successfully_window.config(bg='#FFBCBC')

    acc_created_successfully_label = Label(acc_created_successfully_window,
                                           text="Your new bank account has been created successfully", bg='#F8485E',
                                           relief=tk.FLAT, width=90, height=2, borderwidth=5)
    acc_created_successfully_label.config(font=('Roboto', 10, 'bold'))
    acc_created_successfully_label.place(x=1, y=1)

    Label(acc_created_successfully_window, text="Your Account Number :", bg='#F8485E').place(x=120, y=250)
    Label(acc_created_successfully_window, text=f"{accno}", bg="yellow", fg="red").place(x=258, y=250)

    Label(acc_created_successfully_window, text="Your CVV :", bg='#F8485E').place(x=453, y=250)
    Label(acc_created_successfully_window, text=f"{cvv}", bg="yellow", fg="red").place(x=520, y=250)

    Label(acc_created_successfully_window, text="Your deposited amount :", bg='#F8485E').place(x=250, y=300)
    Label(acc_created_successfully_window, text=f"{amt}", bg="yellow", fg="red").place(x=393, y=300)

    Button(acc_created_successfully_window, text="Logout", fg='Black', bg='red',
           command=acc_created_successfully_window.destroy).place(x=610, y=350)


def existing_user():
    existing_user_login = Tk()
    existing_user_login.title("Existing user Login")
    existing_user_login.geometry("700x400")
    existing_user_login.config(bg='#FFBCBC')

    def login():
        ex_name = name_ex_user.get()
        ex_accno = acc_no_user.get()
        ex_passkey = passkey.get()
        BackEnd.existing_user(BackEnd(), ex_name, ex_accno, ex_passkey)

    intro_label = Label(existing_user_login, text='Please enter your credentials', width=57, height=2, fg='black',
                        bg='#F8485E',
                        relief=tk.FLAT, borderwidth=6)
    intro_label.config(font=('Helvetica', 15, 'bold'))
    intro_label.place(x=1, y=1)

    Label(existing_user_login, text="Enter your name :  ", bg='#F8485E').place(x=80, y=200)
    name_ex_user = Entry(existing_user_login, bd=3, relief=tk.SUNKEN, justify=tk.CENTER)
    name_ex_user.place(x=190, y=200)

    Label(existing_user_login, text="Account number : ", bg='#F8485E').place(x=80, y=250)
    acc_no_user = Entry(existing_user_login, bd=3, relief=tk.SUNKEN, justify=tk.CENTER)
    acc_no_user.place(x=190, y=250)

    Label(existing_user_login, text="Password :              ", bg='#F8485E').place(x=80, y=300)
    passkey = Entry(existing_user_login, bd=3, relief=tk.SUNKEN, justify=tk.CENTER, show='⚈')
    passkey.place(x=190, y=300)

    Button(existing_user_login, text="Login", fg='Black', bg='#79D70F', command=login).place(x=580, y=350)
    Button(existing_user_login, text="Back", fg='Black', bg='red', command=existing_user_login.destroy).place(x=630,
                                                                                                              y=350)


def login_failure():
    login_failure_window = Tk()
    login_failure_window.title("Error 404")
    login_failure_window.geometry("700x80")
    login_failure_window.config(bg='#FFBCBC')

    Label(login_failure_window, text="Error 404 : User not Found", fg="red").place(x=270, y=10)

    Button(login_failure_window, text="Create New Account", fg='Black', bg='#79D70F', command=new_user_window).place(
        x=520, y=30)
    Button(login_failure_window, text="Back", fg='Black', bg='red', command=login_failure_window.destroy).place(x=480,
                                                                                                                y=30)


def login_validated():
    login_validated_window = Tk()
    login_validated_window.title("Welcome!")
    login_validated_window.geometry("700x400")
    login_validated_window.config(bg='#FFBCBC')

    login_validated_label = Label(login_validated_window, text=" Login Successful !! ", borderwidth=5, fg="Black",
                                  bg='#F8485E', relief=tk.FLAT, width=57, height=2)
    login_validated_label.config(font=('Roboto', 15, 'bold', 'italic'))
    login_validated_label.place(x=1, y=1)

    withdraw_amt_button = Button(login_validated_window, text=' Withdraw Amount ', borderwidth=3, fg="Black",
                                 bg="#FF9642", command=withdraw_amt)
    withdraw_amt_button.place(x=290, y=200)
    Button(login_validated_window, text="Logout", fg='Black', bg='red', command=login_validated_window.destroy).place(
        x=610, y=350)
    deposit_amt_button = Button(login_validated_window, text='Deposit Amount', borderwidth=3, fg="Black",
                                bg="#FF9642", command=deposit_amt)
    deposit_amt_button.place(x=300, y=240)
    send_money_button = Button(login_validated_window, text="Send money to another account", borderwidth=3, fg="Black",
                               bg="#FF9642", command=send_amt)
    send_money_button.place(x=256, y=280)
    passbook_button = Button(login_validated_window, text="Check Passbook", borderwidth=3, fg="Black",
                             bg="#FF9642", command=check_passbook)
    passbook_button.place(x=300, y=320)


def withdraw_amt():
    withdraw_amt_window = Tk()
    withdraw_amt_window.title("Withdraw amount portal")
    withdraw_amt_window.geometry("700x400")
    withdraw_amt_window.config(bg='#FFBCBC')

    def submit_withdraw_data():
        ex_name = name_ex_user.get()
        ex_accno = acc_no_user.get()
        ex_passkey = passkey.get()
        ex_withdraw_amt = withdraw_amt_entry_field.get()
        database.Existing_User_DataBase.withdraw_update(database.Existing_User_DataBase(), ex_name, ex_accno,
                                                        ex_passkey, ex_withdraw_amt)

    Label(withdraw_amt_window, text="Note : We are asking for your name , account number and password again for user "
                                    "verification ", fg="red", bg="yellow").place(x=80, y=120)

    Label(withdraw_amt_window, text="Enter your name :  ", bg='#F8485E').place(x=80, y=200)
    name_ex_user = Entry(withdraw_amt_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER)
    name_ex_user.place(x=190, y=200)

    Label(withdraw_amt_window, text="Account number : ", bg='#F8485E').place(x=80, y=250)
    acc_no_user = Entry(withdraw_amt_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER)
    acc_no_user.place(x=190, y=250)

    Label(withdraw_amt_window, text="Password :              ", bg='#F8485E').place(x=80, y=300)
    passkey = Entry(withdraw_amt_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER, show='⚈')
    passkey.place(x=190, y=300)

    Label(withdraw_amt_window, text="Amount to be withdrawn :", bg='#F8485E').place(x=380, y=250)
    withdraw_amt_entry_field = Entry(withdraw_amt_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER)
    withdraw_amt_entry_field.place(x=530, y=250)
    Button(withdraw_amt_window, text="Click to Submit", fg='Black', bg='#79D70F', command=submit_withdraw_data).place(
        x=520, y=350)
    Button(withdraw_amt_window, text="Back", fg='Black', bg="red", command=withdraw_amt_window.destroy).place(x=630,
                                                                                                              y=350)


def withdraw_error():
    withdraw_error_window = Tk()
    withdraw_error_window.title("Insufficient Balance")
    withdraw_error_window.geometry("700x80")
    withdraw_error_window.config(bg='#FFBCBC')

    Label(withdraw_error_window, text="Insufficient Balance !! ", fg="red", bg="yellow").place(x=270, y=10)

    Button(withdraw_error_window, text="Back", fg='Black', bg='red', command=withdraw_error_window.destroy).place(x=480,
                                                                                                                  y=30)


def withdraw_successful(balance):
    withdraw_successful_window = Tk()
    withdraw_successful_window.title("Withdrawal Process is successful")
    withdraw_successful_window.geometry("700x80")
    withdraw_successful_window.config(bg='#FFBCBC')

    Label(withdraw_successful_window, text=f"Withdrawal Successful !! Your updated balance is {balance}", fg="red",
          bg="yellow").place(x=230, y=10)

    Button(withdraw_successful_window, text="Back", fg='Black', bg='red',
           command=withdraw_successful_window.destroy).place(x=480,
                                                             y=40)


def deposit_amt():
    deposit_amt_window = Tk()
    deposit_amt_window.title("Deposit amount portal")
    deposit_amt_window.geometry("700x400")
    deposit_amt_window.config(bg='#FFBCBC')

    def submit_deposit_data():
        ex_name = name_ex_user.get()
        ex_accno = acc_no_user.get()
        ex_passkey = passkey.get()
        ex_deposit_amt = deposit_amt_entry_field.get()
        database.Existing_User_DataBase.deposit_update(database.Existing_User_DataBase(), ex_name, ex_accno, ex_passkey,
                                                       ex_deposit_amt)

    Label(deposit_amt_window, text="Note : We are asking for your name , account number and password again for user "
                                   "verification ", fg="red", bg="yellow").place(x=80, y=120)

    Label(deposit_amt_window, text="Enter your name :  ", bg='#F8485E').place(x=80, y=200)
    name_ex_user = Entry(deposit_amt_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER)
    name_ex_user.place(x=190, y=200)

    Label(deposit_amt_window, text="Account number : ", bg='#F8485E').place(x=80, y=250)
    acc_no_user = Entry(deposit_amt_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER)
    acc_no_user.place(x=190, y=250)

    Label(deposit_amt_window, text="Password :              ", bg='#F8485E').place(x=80, y=300)
    passkey = Entry(deposit_amt_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER, show='⚈')
    passkey.place(x=190, y=300)

    Label(deposit_amt_window, text="Amount to be Deposited :", bg='#F8485E').place(x=380, y=250)
    deposit_amt_entry_field = Entry(deposit_amt_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER)
    deposit_amt_entry_field.place(x=530, y=250)
    Button(deposit_amt_window, text="Click to Submit", fg='Black', bg='#79D70F', command=submit_deposit_data).place(
        x=520, y=350)
    Button(deposit_amt_window, text="Back", fg='Black', bg="red", command=deposit_amt_window.destroy).place(x=630,
                                                                                                            y=350)


def deposit_successful(balance):
    deposit_successful_window = Tk()
    deposit_successful_window.title("Deposit Process is successful")
    deposit_successful_window.geometry("700x80")
    deposit_successful_window.config(bg='#FFBCBC')

    Label(deposit_successful_window, text=f"Amount successfully deposited !! Your updated balance is {balance}",
          fg="red", bg="yellow").place(x=190, y=10)

    Button(deposit_successful_window, text="Back", fg='Black', bg='red',
           command=deposit_successful_window.destroy).place(x=480,
                                                            y=40)


def send_amt():
    send_amt_window = Tk()
    send_amt_window.title("Amount Transfer Portal")
    send_amt_window.geometry("700x400")
    send_amt_window.config(bg='#FFBCBC')

    def send_amt_data():
        from_name = name_ex_user.get()
        from_accno = acc_no_user.get()
        from_passkey = passkey.get()
        amount_to_send = send_amt_entry.get()
        to_name = name_rec_user.get()
        to_accno = acc_no_rec.get()
        database.Existing_User_DataBase.send_amt(database.Existing_User_DataBase(), from_name, from_accno, from_passkey,
                                                 amount_to_send, to_name, to_accno)

    Label(send_amt_window, text="Enter your name :  ", bg='#F8485E').place(x=40, y=200)
    name_ex_user = Entry(send_amt_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER)
    name_ex_user.place(x=150, y=200)

    Label(send_amt_window, text="Account number : ", bg='#F8485E').place(x=40, y=250)
    acc_no_user = Entry(send_amt_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER)
    acc_no_user.place(x=150, y=250)

    Label(send_amt_window, text="Password :              ", bg='#F8485E').place(x=40, y=300)
    passkey = Entry(send_amt_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER, show='⚈')
    passkey.place(x=150, y=300)

    Label(send_amt_window, text="Amount to send :", bg="#F8485E").place(x=180, y=150)
    send_amt_entry = Entry(send_amt_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER)
    send_amt_entry.place(x=285, y=150)

    # ***************************************************************************************

    Label(send_amt_window, text="Enter receiver's name :           ", bg='#F8485E').place(x=360, y=200)
    name_rec_user = Entry(send_amt_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER)
    name_rec_user.place(x=520, y=200)

    Label(send_amt_window, text=" Receiver's account number :", bg='#F8485E').place(x=360, y=250)
    acc_no_rec = Entry(send_amt_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER)
    acc_no_rec.place(x=520, y=250)

    Button(send_amt_window, text="Send Amount", fg="Black", bg="Green", command=send_amt_data).place(x=440, y=300)
    Button(send_amt_window, text="Back", fg="Black", bg="Red", command=send_amt_window.destroy).place(x=550, y=300)


def send_amount_successful():
    send_amount_successful_window = Tk()
    send_amount_successful_window.title("Amount Successfully sent !")
    send_amount_successful_window.geometry("700x80")
    send_amount_successful_window.config(bg='#FFBCBC')

    Label(send_amount_successful_window, fg="red",
          text="Amount successfully sent !!!", bg="yellow").place(x=190, y=10)

    Button(send_amount_successful_window, text="Back", fg='Black', bg='red',
           command=send_amount_successful_window.destroy).place(x=480,
                                                                y=40)

def check_passbook():
    check_passbook_window = Tk()
    check_passbook_window.title("Check Your Transactions")
    check_passbook_window.geometry("700x400")
    check_passbook_window.config(bg='#FFBCBC')

    def check_passbook_data():
        pass_name = name_ex_user.get()
        acc_no = acc_no_user.get()
        pass_key = passkey.get()
        show_passbook(pass_name,acc_no,pass_key)

    Label(check_passbook_window, text="Enter your name :  ", bg='#F8485E').place(x=40, y=200)
    name_ex_user = Entry(check_passbook_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER)
    name_ex_user.place(x=150, y=200)

    Label(check_passbook_window, text="Account number : ", bg='#F8485E').place(x=40, y=250)
    acc_no_user = Entry(check_passbook_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER)
    acc_no_user.place(x=150, y=250)

    Label(check_passbook_window, text="Password :              ", bg='#F8485E').place(x=40, y=300)
    passkey = Entry(check_passbook_window, bd=3, relief=tk.SUNKEN, justify=tk.CENTER, show='⚈')
    passkey.place(x=150, y=300)

    Button(check_passbook_window, text="Check your transactions", fg="Black", bg="Green", command=check_passbook_data).place(x=440, y=300)
    Button(check_passbook_window, text="Back", fg="Black", bg="Red", command=check_passbook_window.destroy).place(x=610, y=300)

def show_passbook(pass_name,acc_no,pass_key):
    show_passbook_window = Tk()
    show_passbook_window.title(f"{pass_name}'s Passbook")
    show_passbook_window.config(bg='#FFBCBC')
    width = 500
    height = 400
    screen_width = show_passbook_window.winfo_screenwidth()
    screen_height = show_passbook_window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    show_passbook_window.geometry("%dx%d+%d+%d" % (width, height, x, y))
    show_passbook_window.resizable(0, 0)

    TableMargin = Frame(show_passbook_window, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Previous Amount", "Process", "Amount Change", "Balance", "Date", "Time"), height=400, selectmode="extended",
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Previous Amount', text="Previous Amount", anchor=W)
    tree.heading('Process', text="Process", anchor=W)
    tree.heading('Amount Change', text="Amount Change", anchor=W)
    tree.heading('Balance', text="Balance", anchor=W)
    tree.heading('Date', text="Date", anchor=W)
    tree.heading('Time', text="Time", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.column('#4', stretch=NO, minwidth=0, width=100)
    tree.column('#5', stretch=NO, minwidth=0, width=100)
    tree.column('#6', stretch=NO, minwidth=0, width=100)
    tree.pack()

    with open(f'./user_db/{pass_name}_{acc_no}_{pass_key}.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            previous_amount = row['Previous Amount']
            process = row['Process']
            amount_change = row['Amount Change']
            balance = row['Balance']
            date = row['Date']
            toime = row['Time']
            tree.insert("", 0, values=(previous_amount, process, amount_change, balance, date, toime))



if __name__ == '__main__':
    main_menu()
    mainloop()