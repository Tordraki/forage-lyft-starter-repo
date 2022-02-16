from abc import ABC

class CarriganTire(Tire):

    def __init__(self, tireStatus):
            self.tireStatus = tireStatus

    def needs_service(self):
        for x in tireStatus:
            if x > 0.9:
                return true
        return false