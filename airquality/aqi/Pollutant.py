# -*- coding: utf-8 -*-
from enum import Enum


class Pollutant(Enum):
    """List of pollutants"""

    PM10 = 0
    PM25 = 1
    SO2 = 2
    NO2 = 3
    CO = 4
    O3 = 5
