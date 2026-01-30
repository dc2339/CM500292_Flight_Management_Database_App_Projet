from database_connection import get_connection


def init_database():

    conn = get_connection()
    cur = conn.cursor()

    #Enabling the foreing key constrains for SQLite library 
    cur.execute("PRAGMA foreign_keys = ON;")

    # ---------------- TABLE ROLE --------------------------

    cur.execute("""

    CREATE TABLE IF NOT EXISTS Role(
                
                RoleId INTEGER PRIMARY KEY,
                RoleName VARCHAR(50) NOT NULL
                
                );
    """)


    # ---------------- TABLE PILOT --------------------------

    cur.execute("""

    CREATE TABLE IF NOT EXISTS Pilot(
                
                PilotId INTEGER PRIMARY KEY AUTOINCREMENT,
                FirstName VARCHAR(50) NOT NULL,
                SecondName VARCHAR(50) NOT NULL,
                LicenseNumber VARCHAR(10) UNIQUE NOT NULL,
                ExperienceYears INTEGER,
                RoleId INTEGER NOT NULL, 
                
                FOREIGN KEY(RoleId) REFERENCES Role(RoleId)

                );
    """)


     # ---------------- TABLE DESTINATION --------------------------

    cur.execute("""

    CREATE TABLE IF NOT EXISTS Destination(
                 
                DesrinationId INTEGER PRIMARY KEY AUTOINCREMENT,
                City VARCHAR(50) NOT NULL,
                Country VARCHAR(50) NOT NULL,
                AirportCode VARCHAR(10) UNIQUE NOT NULL
                 
                 );
    """)

    # ---------------- TABLE FLIGHT STATUS --------------------------

    cur.execute("""
                
    CREATE TABLE IF NOT EXISTS FlightStatus(
                    
                FlightStatusId INTEGER PRIMARY KEY, 
                FlightStatusName VARCHAR(50) NOT NULL
                    
                );
    """)

    # ---------------- FLIGHT ----------------

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Flight(
        
        FlightID INTEGER PRIMARY KEY AUTOINCREMENT,
        FlightNumber VARCHAR(10) NOT NULL,
        FlightDate DATE NOT NULL,

        DepartureDestinationId INTEGER NOT NULL,
        ArrivalDestinationId INTEGER NOT NULL,

        ScheduledDepartureTime DATETIME NOT NULL,
        ScheduledArrivalTime DATETIME NOT NULL,
        ActualDepartureTime DATETIME,
        ActualArrivalTime DATETIME,
        FlightStatusId IINTEGER NOT NULL,

        FOREIGN KEY(DepartureDestinationId)REFERENCES Destination(DestinationId) ON DELETE RESTRICT ON UPDATE CASCADE,
        FOREIGN KEY(ArrivalDestinationId) REFERENCES Destination(DestinationId) ON DELETE RESTRICT ON UPDATE CASCADE,
        FOREIGN KEY(FlightStatusId) REFERENCES FlightStatus(FlightStatusId) ON DELETE RESTRICT ON UPDATE CASCADE

        UNIQUE(FlightNumber, FlightDate)
    );
    """)

    # ---------------- TABLE FLIGHT_PILOT --------------------------

    cur.execute("""

    CREATE TABLE IF NOT EXISTS FlightPilot(
                 
                FlightPilotId INTEGER PRIMARY KEY AUTOINCREMENT,
                FlightId INTEGER NOT NULL,
                PilotId INTEGER NOT NULL,
                  
                FOREIGN KEY(FlightId) REFERENCES Flight(FlightId) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY(PilotId) REFERENCES Pilot(PilotId) ON DELETE RESTRICT ON UPDATE CASCADE
                 
    );
    """)

    #Commit eventual change and close the connection to the DB
    conn.commit()
    conn.close()