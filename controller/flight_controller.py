from model.flight import Flight
from repository.flight_repository import *


def add_flight():
    
    fn = input("Flight Number: ")
    fd = input("Flight Date (YYYY-MM-DD): ")
    dep = input("Departure Destination ID: ")
    arr = input("Arrival Destination ID: ")
    sd = input("Scheduled Departure Time (HH:MM): ")
    sa = input("Scheduled Arrival Time (HH:MM): ")
    ad = input("Actual Departure Time (HH:MM) or leave empty: ")
    aa = input("Actual Arrival Time (HH:MM) or leave empty: ")
    sid = input("Flight Status ID: ")

    # Convert empty actual times to None
    ad = ad if ad else None
    aa = aa if aa else None

    flight = Flight(fn, fd, dep, arr, sd, sa, ad, aa, sid)

    insert_flight(flight)

    print("Flight added")

def view_flights_by_status():

    status_id = input("Enter Flight Status ID: ")
    flights = view_flight_by_status_id(status_id)

    print("\nFlights with this status:")
    for flight in flights:
        print(flight)


def view_flights_by_departure():

    departure_id = input("Enter Departure Destination ID: ")
    flights = view_flight_by_departure_id(departure_id)

    print("\nFlights departing from this destination:")
    for flight in flights:
        print(flight)


def view_flights_by_arrival():

    arrival_id = input("Enter Arrival Destination ID: ")
    flights = view_flight_by_arrival_id(arrival_id)

    print("\nFlights arriving at this destination:")
    for flight in flights:
        print(flight)


def view_flights_by_date():
    flight_date = input("Enter Flight Date (YYYY-MM-DD): ")
    flights = view_flight_by_flight_date(flight_date)

    print("\nFlights on this date:")
    for flight in flights:
        print(flight)


def view_flights_by_number():
    flight_number = input("Enter Flight Number: ")
    flights = view_flight_by_fligth_number(flight_number)

    print("\nFlights with this number:")
    for flight in flights:
        print(flight)

def view_all_flight():

    flights = view_all_flights()

    print("\n All flights: ")
    for flight in flights:
        print(flight)
