import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("running_tracker")


def get_user_data():
    while True:
        print("Please enter data of your run.")
        print("Date of your run (dd/mm/yyyy).")
        print("Your weight in kg.")
        print("Distance in km.")
        print("Time spent in minutes.")
        print("All data must be separated by commas.")
        print("Example: 23/03/23,80,4.5,58")

        data_str = input("Enter your data here:\n")
        data = data_str.split(",")
        if validate_data(data):
            print("Data is valid!")
            break
    return data


def validate_data(data):
    try:
        date = datetime.strptime(data[0], '%d/%m/%Y')
    except ValueError:
        print("Incorrect data format, should be MM/DD/YYYY")
    try:
        weight = float(data[1])
        distance = float(data[2])
        time = float(data[3])
        if weight <= 0 or distance <= 0 or time <= 0:
            raise ValueError
        
        return (date, weight, distance, time)
    except (ValueError, IndexError):
        print('Invalid input data! Please try again.\n')
        return None


get_user_data()