from .base import Chassis, Wheels, Engine, Breaks
from .tweaks import Vanilla, Handling, Acceleration, Breaking


__all__ = ["PARTS", "CHASSIS", "WHEELS", "ENGINES", "BREAKS"]


PARTS = {}
CHASSIS = {}
WHEELS = {}
ENGINES = {}
BREAKS = {}

POSTFIXES = (
    ("", Vanilla),
    ("+H", Handling),
    ("+A", Acceleration),
    ("+B", Breaking)
)

PREFIXES = (
    ("Chassis", Chassis,    CHASSIS),
    ("Wheels",  Wheels,     WHEELS),
    ("Engine",  Engine,     ENGINES),
    ("Breaks",  Breaks,     BREAKS)
)

SERIES = (
    ("Newbie", 10),
    ("Starter", 20),
    ("A30", 30),
    ("A40", 40),
    ("A50", 50),
    ("B70", 70),
    ("B80", 80),
    ("B99", 99),
)

PARTS["Stock"] = {}

for prefix, part_type, part_dict in PREFIXES:
    series_name = "Stock"
    series = 0
    part_dict[series_name] = {}
    PARTS[series_name][prefix] = {}
    if part_type is Chassis:
        part = part_type(series_name, series)
    else:
        part = part_type(series_name, series, Vanilla)
    part_dict[series_name][series_name] = \
        PARTS[series_name][prefix][series_name] = part


for series_name, series in SERIES:
    series_dict = PARTS[series_name] = {}
    for prefix, _, part_dict in PREFIXES:
        series_dict[prefix] = {}
        part_dict[series_name] = {}
    CHASSIS[series_name] = \
        series_dict["Chassis"][series_name] =\
        Chassis(series_name, series)
    for postfix, tweak in POSTFIXES:
        for prefix, part_type, part_dict in PREFIXES[1:]:
            name = "%s %s%s" % (prefix, series_name, postfix)
            part_dict[series_name][name] =\
                series_dict[prefix][name] =\
                part_type(name, series, tweak)