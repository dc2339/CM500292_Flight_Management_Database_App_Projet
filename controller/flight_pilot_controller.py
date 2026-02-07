from repository.flight_pilot_repository import assign_pilot_to_flight

def assign_pilot():

    flight_id = input("Enter Flight ID: ")
    pilot_id = input("Enter Pilot ID: ")

    assign_pilot_to_flight(flight_id, pilot_id)

    print("Pilot successfully assigned to flight")