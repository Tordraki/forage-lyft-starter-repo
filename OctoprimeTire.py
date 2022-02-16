from abc import ABC

class OctoprimeTire(Tire):

    def __init__(self, tireStatus):
            self.tireStatus = tireStatus

    def needs_service(self):
        return tireStatus.sum()>3