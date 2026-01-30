from db_init import init_database, insert_lookup_tables
from controller.pilot_controller import add_pilot, view_all_pilots


def main():

    init_database()
    insert_lookup_tables()

    while True: 
        print("\n PILOT MANAGEMENT")
        print("Press 1 to insert a new Pilot")
        print("Press 2 to view all Pilots")
        print("Press 3 to exit")

        choice = input("Select an option: ")

        if(choice == "1"):
            add_pilot()

        elif(choice == "2"):
            view_all_pilots()

        elif(choice == "3"):
            print("Exting the application ...")
            break
        
        else:
            print("Invalid option, please try agin.")


if __name__ == "__main__":
    main()
            
