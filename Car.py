from abc import ABC

class Car(ABC):
    def __init__(self, engine, battery):
        self.battery = battery
        self.engine = engine

    def needs_service(self):
        return (engine.needs_service()) or (battery.needs_service())