__all__ = ["SpecError", "InvalidSeries", "InvalidTweak"]


class SpecError(TypeError):
    pass


class InvalidSeries(SpecError):
    pass


class InvalidTweak(SpecError):
    pass
