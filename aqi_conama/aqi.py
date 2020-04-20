# -*- coding: utf-8 -*-
from .Pollutant import Pollutant
from decimal import Decimal
import math

good = {
    "idx": (Decimal("0"), Decimal("50")),
    Pollutant.PM10: (Decimal("0"), Decimal("40")),
    Pollutant.PM25: (Decimal("0"), Decimal("20")),
    Pollutant.SO2: (Decimal("0"), Decimal("40")),
    Pollutant.NO2: (Decimal("0"), Decimal("60")),
    Pollutant.CO: (Decimal("0"), Decimal("4.5")),
    Pollutant.O3: (Decimal("0"), Decimal("70")),
}
moderate = {
    "idx": (Decimal("51"), Decimal("100")),
    Pollutant.PM10: (Decimal("40.1"), Decimal("120")),
    Pollutant.PM25: (Decimal("20.1"), Decimal("60")),
    Pollutant.SO2: (Decimal("40.1"), Decimal("125")),
    Pollutant.NO2: (Decimal("60.1"), Decimal("260")),
    Pollutant.CO: (Decimal("4.6"), Decimal("9.0")),
    Pollutant.O3: (Decimal("70.1"), Decimal("140")),
}
inadequate = {
    "idx": (Decimal("101"), Decimal("199")),
    Pollutant.PM10: (Decimal("120.1"), Decimal("250")),
    Pollutant.PM25: (Decimal("60.1"), Decimal("125")),
    Pollutant.SO2: (Decimal("125.1"), Decimal("800")),
    Pollutant.NO2: (Decimal("260.1"), Decimal("1130")),
    Pollutant.CO: (Decimal("9.1"), Decimal("15")),
    Pollutant.O3: (Decimal("140.1"), Decimal("200")),
}
bad = {
    "idx": (Decimal("200"), Decimal("299")),
    Pollutant.PM10: (Decimal("250.1"), Decimal("420")),
    Pollutant.PM25: (Decimal("125.1"), Decimal("210")),
    Pollutant.SO2: (Decimal("800.1"), Decimal("1600")),
    Pollutant.NO2: (Decimal("1130.1"), Decimal("2260")),
    Pollutant.CO: (Decimal("15.1"), Decimal("30")),
    Pollutant.O3: (Decimal("200.1"), Decimal("400")),
}
terrible = {
    "idx": (Decimal("300"), Decimal("399")),
    Pollutant.PM10: (Decimal("420.1"), Decimal("500")),
    Pollutant.PM25: (Decimal("210.1"), Decimal("250")),
    Pollutant.SO2: (Decimal("1600.1"), Decimal("2100")),
    Pollutant.NO2: (Decimal("2260.1"), Decimal("3000")),
    Pollutant.CO: (Decimal("30.1"), Decimal("40")),
    Pollutant.O3: (Decimal("400.1"), Decimal("600")),
}
critical = {
    "idx": (Decimal("400"), Decimal(math.inf)),
    Pollutant.PM10: (Decimal("500.1"), Decimal(math.inf)),
    Pollutant.PM25: (Decimal("250.1"), Decimal(math.inf)),
    Pollutant.SO2: (Decimal("2100.1"), Decimal(math.inf)),
    Pollutant.NO2: (Decimal("3000.1"), Decimal(math.inf)),
    Pollutant.CO: (Decimal("40.1"), Decimal(math.inf)),
    Pollutant.O3: (Decimal("600.1"), Decimal(math.inf)),
}

aqis = {
    "good": good,
    "moderate": moderate,
    "inadequate": inadequate,
    "bad": bad,
    "terrible": terrible,
    "critical": critical,
}


def get_aqi(c: float, specie: Pollutant) -> {str: Decimal}:
    """function to calculate the air quality index using the CONAMA Resolution
    No. 491/2018 standard

    Parameters
    ----------
    c : float
        pollutant concentration
    specie : Pollutant
        pollutant of the Pollutant type

    Returns
    -------
    {str: Decimal}
        returns the dictionary containing the qualification of the index and
        its value
    """
    c = Decimal(f"{c}")
    for aqi in aqis:
        qual = aqis[aqi]
        ch = qual[specie][1]
        cl = qual[specie][0]
        if cl <= round(c, 1) <= ch:
            ih = qual["idx"][1]
            il = qual["idx"][0]
            return {aqi: ((ih - il) / (ch - cl)) * (c - cl) + il}
