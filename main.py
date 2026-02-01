from db_init import init_database, insert_lookup_tables
from controller.pilot_controller import add_pilot, view_all_pilots
from controller.destination_controller import * 
from controller.flight_controller import *
from insert_data import insert_data, reset_database

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


def main():

    reset_database()
    init_database()
    insert_lookup_tables()
    insert_data()

    while True: 
        print("\n MAIN MENU")
        print("Press 1 to add a flight")
        print("Press 6 to View/Update Destination Information")
        print("Press 10 for the pilot managemnt")
        print("Press 7 to exit")

        choice = input("Select an option: ")

        if(choice == "1"):
            print("\n Add flight ")
            add_flight()

        if(choice == "10"):
           print("\n PILOT MANAGEMENT")
           print("1. Add new Pilot")
           print("2. View all Pilots")
           sub_choice = input("Select an option: ")
           
           if (sub_choice) == "1":
                add_pilot()
           elif (sub_choice == "2"):
                view_all_pilots()

        elif(choice == "6"):
            destination_menu()

        elif(choice == "7"):
            print("Exting the application ...")
            break
        
        else:
            print("Invalid option, please try agin.")


if __name__ == "__main__":
    main()
            
