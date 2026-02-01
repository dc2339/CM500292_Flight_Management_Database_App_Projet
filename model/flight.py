class Flight:

    def __init__(self, flightNumber, flight_date, dep_id, arr_id, sched_dep, sched_arr, act_dep, act_arr, status_id):

        self.flightNumber = flightNumber
        self.flight_date = flight_date
        self.dep_id = dep_id
        self.arr_id = arr_id
        self.sched_dep = sched_dep
        self.sched_arr = sched_arr
        self.act_dep = act_dep
        self.act_arr = act_arr
        self.status_id = status_id