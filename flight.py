import json
from datetime import datetime, timedelta


class Flight:
    def __init__(self, destination, origin, departure_hour, time_flight, utc):
        self.origin = origin
        self.destination = destination
        self.departure_hour = departure_hour
        self.time_flight = time_flight
        self.utc = utc

    def estimate_flight(self, origin_utc):
        departure_hour = self.departure_hour.split(":")
        current_time = datetime.now()
        time_to_flight = current_time.replace(hour=int(departure_hour[0]), minute=int(departure_hour[1]))

        hours_added_origin = timedelta(hours=origin_utc)
        origin_time = time_to_flight + hours_added_origin

        hours_added_arrival = timedelta(hours=self.time_flight + self.utc[1])
        estimate_time = origin_time + hours_added_arrival

        return estimate_time.strftime("%m/%d/%Y, %H:%M:%S %p")

    @property
    def flight_dict(self):
        return {
            "origin": self.origin,
            "destination": self.destination,
            "departure_hour": self.departure_hour,
            "time_flight": self.time_flight,
            "utc": self.utc,
        }