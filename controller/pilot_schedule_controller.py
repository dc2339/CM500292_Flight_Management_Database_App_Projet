from repository.pilot_schedule_repository import view_pilot_schedule
from helper_validator import get_int

def show_pilot_schedule():
    pilot_id = get_int("Enter Pilot ID: ")

    schedule = view_pilot_schedule(pilot_id)

    print_pilot_schedule(schedule)


def print_pilot_schedule(rows):
    if not rows:
        print("\nNo flights assigned to this pilot.\n")
        return

    # Pilot info from first row
    first_name, last_name, phone = rows[0][0], rows[0][1], rows[0][2]

    print("\n" + "=" * 80)
    print(f"Pilot: {first_name} {last_name} | Phone: {phone}")
    print("=" * 80)

    header = (
        f"{'FLIGHT':<8} "
        f"{'DATE':<12} "
        f"{'FROM':<15} "
        f"{'TO':<15} "
        f"{'DEP':<6} "
        f"{'ARR':<6} "
        f"{'STATUS':<10}"
    )

    print(header)
    print("-" * len(header))

    for r in rows:
        print(
            f"{r[3]:<8} "
            f"{r[4]:<12} "
            f"{r[7]:<15} "
            f"{r[8]:<15} "
            f"{r[5]:<6} "
            f"{r[6]:<6} "
            f"{r[9]:<10}"
        )

    print("=" * 80 + "\n")