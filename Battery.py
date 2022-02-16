from abc import ABC

class Battery(ABC):
    def needs_service(self):
            raise NotImplementedError("Must override needs_service")