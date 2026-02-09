from model.destination import Destination
from repository.destination_repository import insert_destination, select_all_destination, update_city_destination_by_destination_id, update_country_destination_by_destination_id,update_airport_code_destination_by_destination_id, delete_destination
from helper_validator import get_non_empty, get_int

def get_airport_code(prompt):
    while True:
        code = input(prompt).strip().upper()

        if len(code) == 3 and code.isalpha():
            return code

        print("Airport code must be exactly 3 letters (e.g. FCO, LHR, JFK).")

def add_destination():
    print("\n--- Add Destination ---")

    city = get_non_empty("City: ").title()
    country = get_non_empty("Country: ").title()
    airport_code = get_airport_code("Airport Code (3 letters): ")

    try:
        destination = Destination(city, country, airport_code)
        insert_destination(destination)

    except Exception as e:
        print("Failed to add destination:", e)


def view_all_destinations():
    destinations = select_all_destination()
    print_destinations(destinations)


def update_destination_city():
    print("\n--- Update Destination City ---")

    did = get_int("Destination ID: ")
    new_city = get_non_empty("New City: ").title()

    try:
        update_city_destination_by_destination_id(did, new_city)
    except Exception as e:
        print("Failed to update city:", e)


def update_destination_country():
    print("\n--- Update Destination Country ---")

    did = get_int("Destination ID: ")
    new_country = get_non_empty("New Country: ").title()

    try:
        update_country_destination_by_destination_id(did, new_country)
    except Exception as e:
        print("Failed to update country:", e)


def update_destination_airport_code():
    print("\n--- Update Airport Code ---")

    did = get_int("Destination ID: ")
    new_code = get_airport_code("New Airport Code (3 letters): ")

    try:
        update_airport_code_destination_by_destination_id(did, new_code)
    except Exception as e:
        print("Failed to update airport code:", e)

def print_destinations(rows):
    if not rows:
        print("\nNo destinations found.\n")
        return

    header = f"{'ID':<4} {'CITY':<15} {'COUNTRY':<15} {'CODE':<6}"

    print("\n" + "=" * len(header))
    print(header)
    print("=" * len(header))

    for r in rows:
        print(f"{r[0]:<4} {r[1]:<15} {r[2]:<15} {r[3]:<6}")

    print("=" * len(header) + "\n")


def delete_destination_controller():
    print("\n--- Delete Destination ---")

    did = get_int("Destination ID to delete: ")

    try:
        delete_destination(did)
    except Exception as e:
        print("Failed to delete destination:", e)