from database_connection import get_connection

def view_pilot_schedule(pilot_id):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT 
                P.FirstName,
                P.SecondName,
                P.TelephoneNumber,

                F.FlightNumber,
                F.FlightDate,
                F.ScheduledDepartureTime,
                F.ScheduledArrivalTime,

                D1.City AS DepartureCity,
                D2.City AS ArrivalCity,

                FS.FlightStatusName

            FROM Pilot P

            INNER JOIN FlightPilot FP ON P.PilotId = FP.PilotId
            INNER JOIN Flight F ON FP.FlightId = F.FlightId

            INNER JOIN Destination D1 ON F.DepartureDestinationId = D1.DestinationId
            INNER JOIN Destination D2 ON F.ArrivalDestinationId = D2.DestinationId

            INNER JOIN FlightStatus FS ON F.FlightStatusId = FS.FlightStatusId

            WHERE P.PilotId = ?
        """, (pilot_id,))

        rows = cur.fetchall()
        return rows

    except Exception as e:
        print("Database error while fetching pilot schedule:", e)
        return []

    finally:
        conn.close()