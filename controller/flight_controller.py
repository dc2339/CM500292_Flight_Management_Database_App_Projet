from model.flight import Flight
from repository.flight_repository import (

    insert_flight,
    view_flight_by_status_id,
    view_flight_by_departure_id,
    view_flight_by_arrival_id,
    view_flight_by_flight_date,
    view_flight_by_fligth_number,
    view_all_flights,
    update_scheduled_departure_time,
    update_scheduled_arrival_time,
    update_flight_status,
    update_schedule
)
from helper_validator import *


def add_flight():
    print("\n--- Add New Flight ---")

    fn  = get_non_empty("Flight Number: ")
    fd  = get_date("Flight Date (YYYY-MM-DD): ")
    dep = get_int("Departure Destination ID: ")
    arr = get_int("Arrival Destination ID: ")
    sd  = get_time("Scheduled Departure Time (HH:MM): ")
    sa  = get_time("Scheduled Arrival Time (HH:MM): ")
    ad  = get_time("Actual Departure Time (HH:MM) or press Enter: ", optional=True)
    aa  = get_time("Actual Arrival Time (HH:MM) or press Enter: ", optional=True)
    sid = get_int("Flight Status ID: ")

    flight = Flight(fn, fd, dep, arr, sd, sa, ad, aa, sid)

    try:
        insert_flight(flight)
        print(" Flight added successfully!\n")

    except Exception as e:
        print(" Failed to add flight.")
        print("Error:", e)


def view_flights_by_status():
    status_id = get_int("Enter Flight Status ID: ")

    try:
        flights = view_flight_by_status_id(status_id)
        print_flights(flights)

    except Exception as e:
        print("Something went wrong:", e)


def view_flights_by_departure():
    departure_id = get_int("Enter Departure Destination ID: ")
    flights = view_flight_by_departure_id(departure_id)

    print("\nFlights departing from this destination:")
    print_flights(flights)




def view_flights_by_arrival():
    arrival_id = get_int("Enter Arrival Destination ID: ")
    flights = view_flight_by_arrival_id(arrival_id)

    print("\nFlights arriving at this destination:")
    print_flights(flights)




def view_flights_by_date():
    flight_date = get_date("Enter Flight Date (YYYY-MM-DD): ")
    flights = view_flight_by_flight_date(flight_date)

    print("\nFlights on this date:")
    print_flights(flights)



def view_flights_by_number():
    flight_number = get_non_empty("Enter Flight Number: ")
    flights = view_flight_by_fligth_number(flight_number)

    print("\nFlights with this number:")
    print_flights(flights)


def view_all_flight():
    flights = view_all_flights()

    print("\nAll flights:")
    print_flights(flights)

    

def modify_departure_time():
    print("\n--- Modify Scheduled Departure Time ---")

    flight_id = get_int("Enter Flight ID: ")
    new_time = get_time("New Scheduled Departure Time (HH:MM): ")

    try:
        update_scheduled_departure_time(flight_id, new_time)
        print("Scheduled departure time updated.\n")
    except Exception as e:
        print("Failed to update:", e)



def modify_arrival_time():
    print("\n--- Modify Scheduled Arrival Time ---")

    flight_id = get_int("Enter Flight ID: ")
    new_time = get_time("New Scheduled Arrival Time (HH:MM): ")

    try:
        update_scheduled_arrival_time(flight_id, new_time)
        print("Scheduled arrival time updated.\n")
    except Exception as e:
        print("Failed to update:", e)



def modify_flight_status():
    print("\n--- Modify Flight Status ---")

    flight_id = get_int("Enter Flight ID: ")
    status_id = get_int("Enter New Flight Status ID: ")

    try:
        update_flight_status(flight_id, status_id)
        print("Flight status updated.\n")
    except Exception as e:
        print("Failed to update:", e)

def modify_full_schedule():
    print("\n--- Modify Full Schedule ---")

    flight_id = get_int("Enter Flight ID: ")
    dep_time = get_time("New Departure Time (HH:MM): ")
    arr_time = get_time("New Arrival Time (HH:MM): ")

    try:
        update_schedule(flight_id, dep_time, arr_time)
        print("Flight schedule updated.\n")
    except Exception as e:
        print("Failed to update:", e)


def print_flights(rows):
    if not rows:
        print("\nNo flights found.\n")
        return

    def fmt(v):
        return "-" if v is None else str(v)

    header = (
        f"{'ID':<3} "
        f"{'FLIGHT':<7} "
        f"{'DATE':<11} "
        f"{'FROM':<18} "
        f"{'TO':<18} "
        f"{'DEP':<6} "
        f"{'ARR':<6} "
        f"{'ACT DEP':<7} "
        f"{'ACT ARR':<7} "
        f"{'STATUS':<10}"
    )

    print("\n" + "=" * len(header))
    print(header)
    print("=" * len(header))

    for r in rows:
        from_loc = f"{r[3]} ({r[4]})"
        to_loc   = f"{r[5]} ({r[6]})"

        print(
            f"{r[0]:<3} "
            f"{r[1]:<7} "
            f"{r[2]:<11} "
            f"{from_loc:<18} "
            f"{to_loc:<18} "
            f"{fmt(r[7]):<6} "
            f"{fmt(r[8]):<6} "
            f"{fmt(r[9]):<7} "
            f"{fmt(r[10]):<7} "
            f"{r[11]:<10}"
        )

    print("=" * len(header) + "\n")