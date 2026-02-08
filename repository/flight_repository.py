from database_connection import get_connection

def insert_flight(flight):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO Flight(
                FlightNumber, FlightDate, DepartureDestinationId,
                ArrivalDestinationId, ScheduledDepartureTime,
                ScheduledArrivalTime, ActualDepartureTime,
                ActualArrivalTime, FlightStatusId
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            flight.flightNumber,
            flight.flight_date,
            flight.dep_id,
            flight.arr_id,
            flight.sched_dep,
            flight.sched_arr,
            flight.act_dep,
            flight.act_arr,
            flight.status_id
        ))

        conn.commit()

    except Exception as e:
        print("Database error while inserting flight:", e)

    finally:
        conn.close()


'''
Retrival operation
'''

BASE_FLIGHT_VIEW_QUERY = """
    SELECT
        f.FlightId,
        f.FlightNumber,
        f.FlightDate,

        d1.City  AS DepartureCity,
        d1.AirportCode AS DepartureCode,

        d2.City  AS ArrivalCity,
        d2.AirportCode AS ArrivalCode,

        f.ScheduledDepartureTime,
        f.ScheduledArrivalTime,
        f.ActualDepartureTime,
        f.ActualArrivalTime,

        fs.FlightStatusName
    FROM Flight f

    INNER JOIN Destination d1
        ON f.DepartureDestinationId = d1.DestinationId

    INNER JOIN Destination d2
        ON f.ArrivalDestinationId = d2.DestinationId

    INNER JOIN FlightStatus fs
        ON f.FlightStatusId = fs.FlightStatusId
"""



def view_flight_by_status_id(status_id):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(BASE_FLIGHT_VIEW_QUERY + " WHERE f.FlightStatusId = ?", (status_id,))
        return cur.fetchall()

    except Exception as e:
        print("Database error:", e)
        return []
    finally:
        conn.close()




def view_flight_by_departure_id(departure_id):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(BASE_FLIGHT_VIEW_QUERY + " WHERE f.DepartureDestinationId = ?", (departure_id,))
        return cur.fetchall()

    except Exception as e:
        print("Database error:", e)
        return []
    finally:
        conn.close()




def view_flight_by_arrival_id(arrival_id):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(BASE_FLIGHT_VIEW_QUERY + " WHERE f.ArrivalDestinationId = ?", (arrival_id,))
        return cur.fetchall()

    except Exception as e:
        print("Database error:", e)
        return []
    finally:
        conn.close()



def view_flight_by_flight_date(flight_date):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(BASE_FLIGHT_VIEW_QUERY + " WHERE f.FlightDate = ?", (flight_date,))
        return cur.fetchall()

    except Exception as e:
        print("Database error:", e)
        return []
    finally:
        conn.close()


def view_flight_by_fligth_number(flight_number):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(BASE_FLIGHT_VIEW_QUERY + " WHERE f.FlightNumber = ?", (flight_number,))
        return cur.fetchall()

    except Exception as e:
        print("Database error:", e)
        return []
    finally:
        conn.close()

def view_all_flights():
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(BASE_FLIGHT_VIEW_QUERY)
        return cur.fetchall()

    except Exception as e:
        print("Database error:", e)
        return []
    finally:
        conn.close()

'''
update operations
'''

def update_scheduled_departure_time(flight_id, new_time):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE Flight
        SET ScheduledDepartureTime = ?
        WHERE FlightId = ?
    """, (new_time, flight_id))

    conn.commit()
    conn.close()


def update_scheduled_arrival_time(flight_id, new_time):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE Flight
        SET ScheduledArrivalTime = ?
        WHERE FlightId = ?
    """, (new_time, flight_id))

    conn.commit()
    conn.close()

def update_flight_status(flight_id, status_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE Flight
        SET FlightStatusId = ?
        WHERE FlightId = ?
    """, (status_id, flight_id))

    conn.commit()
    conn.close()

def update_schedule(flight_id, dep_time, arr_time):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE Flight
        SET ScheduledDepartureTime = ?,
            ScheduledArrivalTime = ?
        WHERE FlightId = ?
    """, (dep_time, arr_time, flight_id))

    conn.commit()
    conn.close()