from datetime import datetime

def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")

def get_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("Please enter a valid number.")

def get_date(prompt):
    while True:
        value = input(prompt).strip()
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

def get_time(prompt, optional=False):
    while True:
        value = input(prompt).strip()

        if optional and value == "":
            return None

        try:
            datetime.strptime(value, "%H:%M")
            return value
        except ValueError:
            print("Invalid time format. Use HH:MM (24-hour).")