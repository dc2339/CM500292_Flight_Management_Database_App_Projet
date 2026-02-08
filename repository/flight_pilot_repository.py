from database_connection import get_connection

def assign_pilot_to_flight(flight_id, pilot_id):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO FlightPilot (FlightId, PilotId)
            VALUES (?, ?)
        """, (flight_id, pilot_id))

        conn.commit()
        print("Pilot assigned to flight successfully.")

    except Exception as e:
        print("Failed to assign pilot to flight:", e)

    finally:
        conn.close()