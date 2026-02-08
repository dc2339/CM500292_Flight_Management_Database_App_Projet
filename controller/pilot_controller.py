from model.pilot import Pilot
from repository.pilot_repository import insert_pilot, select_all_pilots
from helper_validator import get_non_empty, get_int


def add_pilot():
    print("\n--- Add Pilot ---")

    fn = get_non_empty("First name: ").title()
    sn = get_non_empty("Second name: ").title()
    ln = get_non_empty("License Number: ").upper()
    ey = get_int("Experience Years: ")
    rid = get_int("Role ID: ")
    em = get_email("Email: ")
    tn = get_phone("Telephone number: ")

    try:
        pilot = Pilot(fn, sn, ln, ey, rid, em, tn)
        insert_pilot(pilot)
    except Exception as e:
        print("Failed to add pilot:", e)

def view_all_pilots():
    pilots = select_all_pilots()
    print_pilots(pilots)


def get_email(prompt):
    while True:
        email = input(prompt).strip()
        if "@" in email and "." in email:
            return email
        print("Enter a valid email address.")

def get_phone(prompt):
    while True:
        phone = input(prompt).strip()
        if phone.isdigit():
            return phone
        print("Phone number must contain digits only.")


def print_pilots(rows):
    if not rows:
        print("\nNo pilots found.\n")
        return

    header = (
        f"{'ID':<4} "
        f"{'NAME':<20} "
        f"{'LICENSE':<10} "
        f"{'EXP':<4} "
        f"{'ROLE':<12} "
        f"{'EMAIL':<25} "
        f"{'PHONE':<12}"
    )

    print("\n" + "=" * len(header))
    print(header)
    print("=" * len(header))

    for r in rows:
        full_name = f"{r[1]} {r[2]}"
        print(
            f"{r[0]:<4} "
            f"{full_name:<20} "
            f"{r[3]:<10} "
            f"{r[4]:<4} "
            f"{r[5]:<12} " 
            f"{r[6]:<25} "
            f"{r[7]:<12}"
        )

    print("=" * len(header) + "\n")