from repository.flight_pilot_repository import assign_pilot_to_flight
from helper_validator import get_int

def assign_pilot():
    print("\n--- Assign Pilot To Flight ---")

    flight_id = get_int("Enter Flight ID: ")
    pilot_id = get_int("Enter Pilot ID: ")

    try:
        assign_pilot_to_flight(flight_id, pilot_id)
    except Exception as e:
        print("Failed to assign pilot:", e)