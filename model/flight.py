class Flight:

    def __init__(self, flightNumber, flight_date, dep_id, arr_id, shced_dep, sched_arr, status_id):
        
        self.flightNumber = flightNumber
        self.flight_date = flight_date
        self.dep_id =  dep_id
        self.arr_id = arr_id
        self.shced_dep = shced_dep
        self.sched_arr = sched_arr
        self.status_id = status_id