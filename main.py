from db_init import init_database, insert_lookup_tables
from controller.pilot_controller import add_pilot, view_all_pilots
from controller.destination_controller import * 
from controller.flight_controller import *
from insert_data import insert_data, reset_database
from controller.flight_pilot_controller import assign_pilot
from controller.pilot_schedule_controller import show_pilot_schedule

def destination_menu():
    while True:
        print("\n DESTINATION MANAGEMENT")
        print("1. Add Destination")
        print("2. View all Destinations")
        print("3. Update Destination City")
        print("4. Update Destination Country")
        print("5. Update Destination Airport Code")
        print("6. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            add_destination()

        elif choice == "2":
            view_all_destinations()

        elif choice == "3":
            update_destination_city()

        elif choice == "4":
            update_destination_country()

        elif choice == "5":
            update_destination_airport_code()

        elif choice == "6":
            break

        else:
            print("Invalid option, please try again.")


def flight_view_menu():
    while True:
        print("\n FLIGHT VISUALIZATION")
        print("1. View flights by Status")
        print("2. View flights by Departure Destination")
        print("3. View flights by Arrival Destination")
        print("4. View flights by Flight Date")
        print("5. View flights by Flight Number")
        print("6. View all flights")
        print("7. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            view_flights_by_status()

        elif choice == "2":
            view_flights_by_departure()

        elif choice == "3":
            view_flights_by_arrival()

        elif choice == "4":
            view_flights_by_date()

        elif choice == "5":
            view_flights_by_number()

        elif choice == "6":
            view_all_flight()

        elif choice == "7":
            break

        else:
            print("Invalid option, please try again.")


def flight_schedule_menu():
    while True:
        print("\n FLIGHT SCHEDULE MODIFICATION")
        print("1. Modify Scheduled Departure Time")
        print("2. Modify Scheduled Arrival Time")
        print("3. Modify Flight Status")
        print("4. Modify Full Schedule (Departure & Arrival)")
        print("5. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            modify_departure_time()

        elif choice == "2":
            modify_arrival_time()

        elif choice == "3":
            modify_flight_status()

        elif choice == "4":
            modify_full_schedule()

        elif choice == "5":
            break

        else:
            print("Invalid option, please try again.")


def flight_assignment_menu():
    while True:
        print("\n FLIGHT CREW ASSIGNMENT")
        print("1. Assign Pilot to Flight")
        print("2. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            assign_pilot()

        elif choice == "2":
            break

        else:
            print("Invalid option, please try again.")


def main():

    reset_database()
    init_database()
    insert_lookup_tables()
    insert_data()

    while True: 
        print("\n MAIN MENU")
        print("Press 1 to add a new flight")
        print("Press 2 to view Flight by criteria")
        print("Press 3 to modify the schedule for a flight")
        print("Press 4 to assign Pilot to Flight")
        print("Press 5 to View Pilot Schedule")
        print("Press 6 to View/Update Destination Information")
        print("Press 10 for the pilot managemnt")
        print("Press 7 to exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_flight()

        elif choice == "2":
            flight_view_menu()

        elif choice == "3":
            flight_schedule_menu()

        elif choice == "4":
            flight_assignment_menu()

        elif choice == "5":
            show_pilot_schedule()

        elif choice == "10":
            print("\n PILOT MANAGEMENT")
            print("1. Add new Pilot")
            print("2. View all Pilots")
            sub_choice = input("Select an option: ")

            if sub_choice == "1":
                add_pilot()
            elif sub_choice == "2":
                view_all_pilots()

        elif choice == "6":
            destination_menu()

        elif choice == "7":
            print("Exiting the application ...")
            break

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
            
