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