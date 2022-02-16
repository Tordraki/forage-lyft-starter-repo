from abc import ABC

from car import Car


class SternmanEngine(Car, ABC):
    def __init__(self, last_service_mileage, current_mileage, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        return warning_light_is_on
