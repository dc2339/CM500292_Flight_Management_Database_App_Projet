from database_connection import get_connection

def insert_flight(flight):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""

    INSERT INTO Flight(
                 FlightNumber, FlightDate, DepartureDestinationId, ArrivalDestinationId, ScheduledDepartureTime, 
                 ScheduledArrivalTime, ActualDepartureTime, ActualArrivalTime, FlightStatusId  
                
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)           
                
    """, (flight.flightNumber, flight.flight_date, flight.dep_id, flight.arr_id, flight.sched_dep, flight.sched_arr,
          flight.act_dep, flight.act_dep, flight.status_id)
    )

    conn.commit()
    conn.close()

def view_flight_by_status_id(status_id):
    
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM Flight
        WHERE FlightStatusId = ?
    """, (status_id,))

    rows = cur.fetchall()
    conn.close()

    return rows

def view_flight_by_departure_id(departure_id):
    
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM Flight
        WHERE DepartureDestinationId = ?
    """, (departure_id,))

    rows = cur.fetchall()
    conn.close()

    return rows


def view_flight_by_arrival_id(arrival_id):
    
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM Flight
        WHERE ArrivalDestinationId = ?
    """, (arrival_id,))

    rows = cur.fetchall()
    conn.close()

    return rows

def view_flight_by_flight_date(flight_date):
    
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM Flight
        WHERE FlightDate = ?
    """, (flight_date,))

    rows = cur.fetchall()
    conn.close()

    return rows


def view_flight_by_fligth_number(flight_number):
    
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM Flight
        WHERE FlightNumber = ?
    """, (flight_number,))

    rows = cur.fetchall()
    conn.close()

    return rows

def view_all_flights():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM Flight")

    rows = cur.fetchall()

    conn.close()

    return rows

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


