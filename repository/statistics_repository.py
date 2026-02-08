from database_connection import get_connection

def count_arrivals_per_destination():
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT 
                D.City,
                D.AirportCode,
                COUNT(F.FlightId) AS TotalFlights
            FROM Destination D

            LEFT JOIN Flight F
                ON D.DestinationId = F.ArrivalDestinationId

            GROUP BY D.DestinationId
            ORDER BY TotalFlights DESC
        """)

        return cur.fetchall()

    except Exception as e:
        print("Database error:", e)
        return []

    finally:
        conn.close()


def count_departures_per_destination():
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT 
                D.City,
                D.AirportCode,
                COUNT(F.FlightId) AS TotalDepartures
            FROM Destination D

            LEFT JOIN Flight F
                ON D.DestinationId = F.DepartureDestinationId

            GROUP BY D.DestinationId
            ORDER BY TotalDepartures DESC
        """)

        return cur.fetchall()

    except Exception as e:
        print("Database error:", e)
        return []

    finally:
        conn.close()


def count_flights_per_pilot():
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT
                P.FirstName,
                P.SecondName,
                COUNT(FP.FlightId) AS TotalFlights
            FROM Pilot P

            LEFT JOIN FlightPilot FP
                ON P.PilotId = FP.PilotId

            GROUP BY P.PilotId
            ORDER BY TotalFlights DESC
        """)

        return cur.fetchall()

    except Exception as e:
        print("Database error:", e)
        return []

    finally:
        conn.close()