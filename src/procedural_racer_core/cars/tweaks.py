from abc import ABCMeta, abstractproperty
__all__ = ["TweakBase",
           "Vanilla",
           "Handling",
           "Acceleration",
           "Breaking"]


class TweakBase(object):

    __metaclass__ = ABCMeta

    handling = abstractproperty(float)
    acceleration = abstractproperty(float)
    breaking = abstractproperty(float)

    @classmethod
    def apply(cls, obj):
        obj.handling *= cls.handling
        obj.acceleration *= cls.acceleration
        obj.breaking *= cls.breaking


class Vanilla(TweakBase):
    handling = 1.0
    acceleration = 1.0
    breaking = 1.0


class Handling(TweakBase):
    handling = 1.25
    acceleration = 0.9
    breaking = 0.9


class Acceleration(TweakBase):
    handling = 0.9
    acceleration = 1.25
    breaking = 0.9


class Breaking(TweakBase):
    handling = 0.9
    acceleration = 0.9
    breaking = 1.25
