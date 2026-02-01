from model.flight import Flight
from repository.flight_repository import insert_flight


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
