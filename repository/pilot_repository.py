from database_connection import get_connection

def insert_pilot(pilot):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""

    INSERT INTO Pilot(
                 FirstName, SecondName, LicenseNumber, ExperienceYears, RoleId, Email, TelephoneNumber  
                
                ) VALUES (?, ?, ?, ?, ?, ?, ?)           
                
    """, (pilot.first_name, pilot.second_name, pilot.license_number, pilot.experience_years, pilot.role_id, pilot.email, pilot.telephone_number)
    )

    conn.commit()
    conn.close()


def select_all_pilots():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM Pilot")

    rows = cur.fetchall()
    conn.close

    return rows