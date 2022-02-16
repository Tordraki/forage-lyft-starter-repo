import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        warning_light_is_on = False

        car = Calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 61000
        last_service_mileage = 0
        warning_light_is_on = True

        car = Calliope(today, last_service_date, current_mileage, last_service_mileage, warning_light_is_on)
        self.assertTrue(car.needs_service())

class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        warning_light_is_on = False

        car = Glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 61000
        last_service_mileage = 0
        warning_light_is_on = True

        car = Glissade(today, last_service_date, current_mileage, last_service_mileage, warning_light_is_on)
        self.assertTrue(car.needs_service())

class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        warning_light_is_on = False

        car = Palindrome(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 61000
        last_service_mileage = 0
        warning_light_is_on = True

        car = Palindrome(today, last_service_date, current_mileage, last_service_mileage, warning_light_is_on)
        self.assertTrue(car.needs_service())

class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        warning_light_is_on = False

        car = Rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 61000
        last_service_mileage = 0
        warning_light_is_on = True

        car = Rorschach(today, last_service_date, current_mileage, last_service_mileage, warning_light_is_on)
        self.assertTrue(car.needs_service())

class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        warning_light_is_on = False

        car = Thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 61000
        last_service_mileage = 0
        warning_light_is_on = True

        car = Thovex(today, last_service_date, current_mileage, last_service_mileage, warning_light_is_on)
        self.assertTrue(car.needs_service())

if __name__ == '__main__':
    unittest.main()
