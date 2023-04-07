# Running Training Tracker

This project was created to collect and store track of a user's running experience in a Google Spreadsheet. It is a Python program running as CLI application that utilizes the gspread library and the Google Sheets API to update a worksheet in a Google Spreadsheet with the user's running data.

## Features

The current version of the Running Training Tracker allows the user to input the following data:

- Date of the run (in DD-MM-YYYY format)
- Weight of the user (in kg)
- Time of the run (in minutes)
- Distance covered during the run (in km)

The program then calculates and displays the following statistics:

- Average pace (in minutes per kilometer)
- Average speed (in kilometers per hour)
- Calories burned during the run
- The calculated statistics are appended to the worksheet named "log" in the Google Spreadsheet.

## Future Enhancements

The Running Training Tracker has potential for further enhancements, including:

- Additional functions to get total time running, total distance, total calories burned, get a list of last few runs, etc.
- Implementation of additional Python libraries to provide a more visually appealing design for the output
- Addition of a database to store and manage the running data for better organization and retrieval

## Usage

When you run the program, it will prompt you to enter the following information:

1. Date of your run (in DD-MM-YYYY format)
2. Weight (in kg)
3. Time of your run (in minutes)
4. Distance covered during the run (in km)

The program will then calculate and display the average pace, average speed, and calories burned during the run. The calculated statistics will be appended to the "log" worksheet in your Google Spreadsheet.

You can try the program by following the link [Running Tracker](https://running-tracker.herokuapp.com/)

Your data will be stored at the Google Spreadsheet here [Running Log](https://docs.google.com/spreadsheets/d/1DMhw-p8midN1tJXm7lFdg5yxJzQR-mhVR5B3qT8ft5Y/edit#gid=1222898038)