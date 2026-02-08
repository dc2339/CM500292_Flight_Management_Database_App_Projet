from database_connection import get_connection

def insert_pilot(pilot):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO Pilot(
                FirstName, SecondName, LicenseNumber,
                ExperienceYears, RoleId, Email, TelephoneNumber
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            pilot.first_name,
            pilot.second_name,
            pilot.license_number,
            pilot.experience_years,
            pilot.role_id,
            pilot.email,
            pilot.telephone_number
        ))

        conn.commit()
        print("Pilot inserted successfully.")

    except Exception as e:
        print("Database error while inserting pilot:", e)

    finally:
        conn.close()


def select_all_pilots():
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT 
                P.PilotId,
                P.FirstName,
                P.SecondName,
                P.LicenseNumber,
                P.ExperienceYears,
                R.RoleName,
                P.Email,
                P.TelephoneNumber
            FROM Pilot P

            INNER JOIN Role R
                ON P.RoleId = R.RoleId
        """)

        rows = cur.fetchall()
        return rows

    except Exception as e:
        print("Database error while fetching pilots:", e)
        return []

    finally:
        conn.close()