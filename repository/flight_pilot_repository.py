from database_connection import get_connection

def assign_pilot_to_flight(flight_id, pilot_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO FlightPilot (FlightId, PilotId)
        VALUES (?, ?)
    """, (flight_id, pilot_id))

    conn.commit()
    conn.close()