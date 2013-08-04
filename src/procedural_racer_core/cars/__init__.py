from . import parts, base, tweaks, exceptions
__all__ = ["parts", "base", "tweaks", "exceptions", "Car"]

class Car(object):
    def __init__(self,
                 name,
                 chassis,
                 wheels,
                 engine,
                 breaks):
        self.name = name
        self.chassis = chassis
        self.wheels = wheels
        self.engine = engine
        self.breaks = breaks