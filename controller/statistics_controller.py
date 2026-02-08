from repository.statistics_repository import (
    count_arrivals_per_destination,
    count_departures_per_destination,
    count_flights_per_pilot
)


def show_arrivals_per_destination():
    rows = count_arrivals_per_destination()
    print_destination_stats(rows, "Flights ARRIVING per Destination")


def show_departures_per_destination():
    rows = count_departures_per_destination()
    print_destination_stats(rows, "Flights DEPARTING per Destination")


def show_flights_per_pilot():
    rows = count_flights_per_pilot()
    print_flights_per_pilot(rows)


def print_destination_stats(rows, title):
    if not rows:
        print("\nNo data found.\n")
        return

    print(f"\n{title}")
    print("=" * 55)
    print(f"{'CITY':<18} {'CODE':<8} {'FLIGHTS':<8}")
    print("=" * 55)

    for r in rows:
        print(f"{r[0]:<18} {r[1]:<8} {r[2]:<8}")

    print("=" * 55 + "\n")

def print_flights_per_pilot(rows):
    if not rows:
        print("\nNo data found.\n")
        return

    print("\nFlights per Pilot")
    print("=" * 45)
    print(f"{'PILOT':<22} {'FLIGHTS':<8}")
    print("=" * 45)

    for r in rows:
        name = f"{r[0]} {r[1]}"
        print(f"{name:<22} {r[2]:<8}")

    print("=" * 45 + "\n")