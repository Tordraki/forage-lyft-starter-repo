from abc import ABC

class NubbinBattery(Battery):

    def __init__(self, last_service_date, date):
            self.last_service_date = last_service_date
            self.date = date

    def display2(self):
        return date-last_service_date >= 4