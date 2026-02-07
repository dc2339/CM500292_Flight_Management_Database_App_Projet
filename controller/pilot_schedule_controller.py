from repository.pilot_schedule_repository import view_pilot_schedule

def show_pilot_schedule():

    pilot_id = input("Enter Pilot ID: ")
    schedule = view_pilot_schedule(pilot_id)

    print("\n PILOT SCHEDULE\n")

    for row in schedule:
        print(row)