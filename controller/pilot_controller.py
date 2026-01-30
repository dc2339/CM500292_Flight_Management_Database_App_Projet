from model.pilot import Pilot
from repository.pilot_repository import insert_pilot, select_all_pilots


def add_pilot():
    fn = input("First name: ")
    sn = input("Second name: ")
    ln = input("License Number: ")
    ey = input("Experince Year: ")
    rid = input("Role id: ")
    em = input("Email: ")
    tn = input("Telephone number: ")

    pilot = Pilot(fn, sn, ln, ey, rid, em, tn)
    insert_pilot(pilot)

    print("Pilot added")

def view_all_pilots():
    pilots = select_all_pilots()

    for pilot in pilots:
        print(pilot)
