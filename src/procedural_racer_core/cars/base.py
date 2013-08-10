from .exceptions import InvalidSeries, InvalidTweak
from .tweaks import TweakBase, Vanilla
from math import floor, ceil

from abc import ABCMeta


class ComponentBase(object):

    __metaclass__ = ABCMeta

    name = "Stock"
    series = 0
    handling = 0.0
    acceleration = 0.0
    breaking = 0.0

    @property
    def price(self):
        return self.series + ceil(max((self.handling,
                                       self.acceleration,
                                       self.breaking)))


    def __repr__(self):
        return "%s(%r, %r)" % (type(self).__name__, self.name, self.series)

    def __init__(self, name, series):
        if not isinstance(name, str):
            raise TypeError("Component %r name should be a string, given %r" % self, name)
        self.name = name
        if not isinstance(series, int):
            raise InvalidSeries("%r is not an integer" % series)
        self.series = series


class Chassis(ComponentBase):

    def __init__(self, name, series):
        """
        :param name: str
        :param series: int
        """
        super(Chassis, self).__init__(name, series)
        self.handling = series
        self.acceleration = series / 2.0
        self.breaking = series / 2.0


class PartBase(ComponentBase):
    tweak = Vanilla

    def __repr__(self):
        return "%s(%r, %r, %s)" % (
            type(self).__name__,
            self.name,
            self.series,
            self.tweak.__name__)

    def __init__(self, name, series, tweak):
        super(PartBase, self).__init__(name, series)
        if not issubclass(tweak, TweakBase):
            raise InvalidTweak("%r is not a valid tweak" % tweak)
        tweak.apply(self)


class Wheels(PartBase):
    def __init__(self, name, series, tweak):
        self.handling = series / 5.0
        self.acceleration = series / 20.0
        self.breaking = series / 20.0
        super(Wheels, self).__init__(name, series, tweak)


class Engine(PartBase):
    def __init__(self, name, series, tweak):
        self.handling = series / 20.0
        self.acceleration = series / 5.0
        self.breaking = series / 20.0
        super(Engine, self).__init__(name, series, tweak)


class Breaks(PartBase):
    def __init__(self, name, series, tweak):
        self.handling = series / 20.0
        self.acceleration = series / 20.0
        self.breaking = series / 5.0
        super(Breaks, self).__init__(name, series, tweak)
