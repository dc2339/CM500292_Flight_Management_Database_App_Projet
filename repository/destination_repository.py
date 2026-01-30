from database_connection import get_connection

def insert_destination(destination): 

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""

    INSERT INTO Destination(
                City, Country, AirportCode

                ) VALUES (?, ?, ?)

    """, (destination.city, destination.country, destination.airport_code)
    )

    conn.commit()
    conn.close()


def update_country_destination_by_destination_id(destination_id, new_country):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                
                UPDATE Destination 
                SET Country = ? 
                WHERE DestinationId = ?
                
                """, (new_country, destination_id)
    )

    conn.commit()
    conn.close()

def update_city_destination_by_destination_id(destination_id, new_city):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                
                UPDATE Destination 
                SET City = ? 
                WHERE DestinationId = ?
                
                """, (new_city, destination_id)
    )

    conn.commit()
    conn.close()


def update_airport_code_destination_by_destination_id(destination_id, new_airport_code):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                
                UPDATE Destination 
                SET AirportCode = ? 
                WHERE DestinationId = ?
                
                """, (new_airport_code, destination_id)
    )

    conn.commit()
    conn.close()

def select_all_destination():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM Destination")

    rows = cur.fetchall()
    conn.close

    return rows



