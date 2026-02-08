from database_connection import get_connection


def insert_data():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("PRAGMA foreign_keys = ON;")

    # ---------------- DESTINATION SAMPLE DATA ----------------
    cur.execute("SELECT COUNT(*) FROM Destination")
    if cur.fetchone()[0] == 0:
        destinations = [
            ("Rome", "Italy", "FCO"),
            ("London", "UK", "LHR"),
            ("Paris", "France", "CDG"),
            ("Berlin", "Germany", "BER"),
            ("Madrid", "Spain", "MAD"),
            ("New York", "USA", "JFK"),
            ("Dubai", "UAE", "DXB"),
            ("Tokyo", "Japan", "HND"),
            ("Toronto", "Canada", "YYZ"),
            ("Sydney", "Australia", "SYD")
        ]
        cur.executemany("""
            INSERT INTO Destination (City, Country, AirportCode)
            VALUES (?, ?, ?)
        """, destinations)
        print("Sample destinations inserted")

    # ---------------- PILOT SAMPLE DATA ----------------
    cur.execute("SELECT COUNT(*) FROM Pilot")
    if cur.fetchone()[0] == 0:
        pilots = [
            ("John", "Smith", "LIC001", 10, 1, "john@mail.com", "1234567890"),
            ("Anna", "Brown", "LIC002", 8, 2, "anna@mail.com", "1234567891"),
            ("Luca", "Rossi", "LIC003", 12, 1, "luca@mail.com", "1234567892"),
            ("Maria", "Garcia", "LIC004", 6, 2, "maria@mail.com", "1234567893"),
            ("Paul", "White", "LIC005", 15, 1, "paul@mail.com", "1234567894"),
            ("Sara", "Black", "LIC006", 4, 3, "sara@mail.com", "1234567895"),
            ("Tom", "Green", "LIC007", 9, 2, "tom@mail.com", "1234567896"),
            ("Elena", "Blue", "LIC008", 7, 2, "elena@mail.com", "1234567897"),
            ("Mark", "Gray", "LIC009", 11, 1, "mark@mail.com", "1234567898"),
            ("Nina", "Gold", "LIC010", 5, 3, "nina@mail.com", "1234567899")
        ]
        cur.executemany("""
            INSERT INTO Pilot 
            (FirstName, SecondName, LicenseNumber, ExperienceYears, RoleId, Email, TelephoneNumber)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, pilots)
        print("Sample pilots inserted")

    # ---------------- FLIGHT SAMPLE DATA ----------------
    cur.execute("SELECT COUNT(*) FROM Flight")
    if cur.fetchone()[0] == 0:
        flights = [
            ("AZ101", "2026-02-01", 1, 2, "08:00", "10:00", None, None, 1),
            ("AZ102", "2026-02-01", 2, 3, "11:00", "13:00", None, None, 1),
            ("AZ103", "2026-02-02", 3, 4, "09:00", "11:30", None, None, 1),
            ("AZ104", "2026-02-02", 4, 5, "14:00", "16:30", None, None, 1),
            ("AZ105", "2026-02-03", 5, 6, "07:30", "12:00", None, None, 1),
            ("AZ106", "2026-02-03", 6, 7, "13:00", "19:00", None, None, 1),
            ("AZ107", "2026-02-04", 7, 8, "06:00", "15:00", None, None, 1),
            ("AZ108", "2026-02-04", 8, 9, "16:00", "22:00", None, None, 1),
            ("AZ109", "2026-02-05", 9, 10, "10:00", "20:00", None, None, 1),
            ("AZ110", "2026-02-05", 10, 1, "21:00", "06:00", None, None, 1)
        ]
        cur.executemany("""
            INSERT INTO Flight
            (FlightNumber, FlightDate, DepartureDestinationId, ArrivalDestinationId,
             ScheduledDepartureTime, ScheduledArrivalTime,
             ActualDepartureTime, ActualArrivalTime, FlightStatusId)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, flights)
        print("Sample flights inserted")

    # ---------------- FLIGHT PILOT ASSIGNMENTS ----------------
    cur.execute("SELECT COUNT(*) FROM FlightPilot")
    if cur.fetchone()[0] == 0:
        assignments = [
            (1,1),(1,2),
            (2,3),(2,4),
            (3,5),(3,6),
            (4,7),(4,8),
            (5,9),(5,10)
        ]
        cur.executemany("""
            INSERT INTO FlightPilot (FlightId, PilotId)
            VALUES (?, ?)
        """, assignments)
        print("Sample flight-pilot assignments inserted")

    conn.commit()
    conn.close()



'''
use for clean testing
'''
def reset_database():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("PRAGMA foreign_keys = OFF;")

    cur.execute("DROP TABLE IF EXISTS FlightPilot;")
    cur.execute("DROP TABLE IF EXISTS Flight;")
    cur.execute("DROP TABLE IF EXISTS Pilot;")
    cur.execute("DROP TABLE IF EXISTS Destination;")
    cur.execute("DROP TABLE IF EXISTS Role;")
    cur.execute("DROP TABLE IF EXISTS FlightStatus;")

    cur.execute("PRAGMA foreign_keys = ON;")

    conn.commit()
    conn.close()

    print("Database reset completed")