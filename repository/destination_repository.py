from database_connection import get_connection

def insert_destination(destination):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO Destination (City, Country, AirportCode)
            VALUES (?, ?, ?)
        """, (destination.city, destination.country, destination.airport_code))

        conn.commit()
        print("Destination inserted successfully.")

    except Exception as e:
        print("Database error while inserting destination:", e)

    finally:
        conn.close()


def update_country_destination_by_destination_id(destination_id, new_country):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE Destination
            SET Country = ?
            WHERE DestinationId = ?
        """, (new_country, destination_id))

        conn.commit()
        print("Country updated.")

    except Exception as e:
        print("Database error while updating country:", e)

    finally:
        conn.close()



def update_city_destination_by_destination_id(destination_id, new_city):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE Destination
            SET City = ?
            WHERE DestinationId = ?
        """, (new_city, destination_id))

        conn.commit()
        print("City updated.")

    except Exception as e:
        print("Database error while updating city:", e)

    finally:
        conn.close()



def update_airport_code_destination_by_destination_id(destination_id, new_airport_code):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE Destination
            SET AirportCode = ?
            WHERE DestinationId = ?
        """, (new_airport_code, destination_id))

        conn.commit()
        print("Airport code updated.")

    except Exception as e:
        print("Database error while updating airport code:", e)

    finally:
        conn.close()

def select_all_destination():
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT DestinationId, City, Country, AirportCode
            FROM Destination
        """)

        rows = cur.fetchall()
        return rows

    except Exception as e:
        print("Database error while fetching destinations:", e)
        return []

    finally:
        conn.close()


def delete_destination(destination_id):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            DELETE FROM Destination
            WHERE DestinationId = ?
        """, (destination_id,))

        conn.commit()
        print("Destination deleted successfully.")

    except Exception as e:
        print("Database error while deleting destination:", e)

    finally:
        conn.close()