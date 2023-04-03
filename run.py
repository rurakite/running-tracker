import gspread
from google.oauth2.service_account import Credentials
import datetime


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("running_tracker")


def get_valid_date():
    while True:
        date_str = input("Enter the date of your run (DD-MM-YYYY): ")
        try:
            datetime.datetime.strptime(date_str, "%d-%m-%Y")
            return date_str
        except ValueError:
            print("Invalid date format. Please enter in DD-MM-YYYY format.")


def get_valid_weight():
    while True:
        weight_str = input("Enter your weight in kg: ")
        try:
            weight = float(weight_str)
            if weight > 0:
                return weight
            else:
                print("Weight must be greater than zero.")
        except ValueError:
            print("Invalid data. Please enter a number.")


def get_valid_time():
    while True:
        time_str = input("Enter time of your run in minutes: ")
        try:
            time = float(time_str)
            if time > 0:
                return time
            else:
                print("Time must be greater than zero.")
        except ValueError:
            print("Invalid data. Please enter a number.")


def get_valid_distance():
    while True:
        distance_str = input("Enter the distance you done in km: ")
        try:
            distance = float(distance_str)
            if distance > 0:
                return distance
            else:
                print("Distance must be greater than zero.")
        except ValueError:
            print("Invalid data. Please enter a number.")


def calculate_avg_speed(distance, time):
    speed = round(distance / (time / 60), 2)
    return speed


def calculate_pace(distance, time):
    pace = round(time / distance, 2)
    return pace


def calculate_burned_calories(weight, distance):
    return round(distance * weight * 0.75)


def update_worksheet(data):
    log = SHEET.worksheet("log")
    log.append_row(data)
    print("Your Running Tracker updated successfully !")


def main():
    date = get_valid_date()
    weight = get_valid_weight()
    time = get_valid_time()
    distance = get_valid_distance()
    print("Calculating your stata...")
    pace = calculate_pace(distance, time)
    print(f"Your pace is {pace} m/km.")
    speed = calculate_avg_speed(distance, time)
    print(f"Your average speed  is {speed} km/h.")
    burned_calories = calculate_burned_calories(weight, distance)
    print(f"You have burned {burned_calories} calories.")
    run_data = [date, distance, time, pace, speed, burned_calories]
    update_worksheet(run_data)
    print(run_data)


print("Welcome to Running Training Tracker!")
main()