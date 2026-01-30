from model.destination import Destination
from repository.destination_repository import (insert_destination, select_all_destination, update_city_destination_by_destination_id, update_country_destination_by_destination_id,update_airport_code_destination_by_destination_id)

def add_destination():
    city = input("City: ")
    country = input("Country: ")
    airport_code = input("Airport Code: ")

    destination = Destination(city, country, airport_code)
    insert_destination(destination)

    print("Destination added")


def view_all_destinations():
    destinations = select_all_destination()

    for destination in destinations:
        print(destination)


def update_destination_city():
    did = input("Destination ID: ")
    new_city = input("New City: ")

    update_city_destination_by_destination_id(did, new_city)
    print("City updated")


def update_destination_country():
    did = input("Destination ID: ")
    new_country = input("New Country: ")

    update_country_destination_by_destination_id(did, new_country)
    print("Country updated")


def update_destination_airport_code():
    did = input("Destination ID: ")
    new_code = input("New Airport Code: ")

    update_airport_code_destination_by_destination_id(did, new_code)
    print("Airport code updated")
