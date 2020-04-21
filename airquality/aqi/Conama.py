from .Pollutant import Pollutant
from decimal import Decimal
from .AQI import AQI
import math


class Conama(AQI):
    """Class containing air quality standards established by CONAMA Resolution
    No. 491/2018

    Attributes
    -------
    standard: {}
        Dictionary with established standards
    """

    standard = {
        'aqi': [
            (Decimal('0'), Decimal('50')),
            (Decimal('51'), Decimal('100')),
            (Decimal('101'), Decimal('199')),
            (Decimal('200'), Decimal('299')),
            (Decimal('300'), Decimal('399')),
            (Decimal('400'), Decimal(math.inf)),
        ],
        'bp': {
            Pollutant.PM10: [
                (Decimal('0'), Decimal('40')),
                (Decimal('40.1'), Decimal('120')),
                (Decimal('120.1'), Decimal('250')),
                (Decimal('250.1'), Decimal('420')),
                (Decimal('420.1'), Decimal('500')),
                (Decimal('500.1'), Decimal(math.inf)),
            ],
            Pollutant.PM25: [
                (Decimal('0'), Decimal('20')),
                (Decimal('20.1'), Decimal('60')),
                (Decimal('60.1'), Decimal('125')),
                (Decimal('125.1'), Decimal('210')),
                (Decimal('210.1'), Decimal('250')),
                (Decimal('250.1'), Decimal(math.inf)),
            ],
            Pollutant.SO2: [
                (Decimal('0'), Decimal('40')),
                (Decimal('40.1'), Decimal('125')),
                (Decimal('125.1'), Decimal('800')),
                (Decimal('800.1'), Decimal('1600')),
                (Decimal('1600.1'), Decimal('2100')),
                (Decimal('2100.1'), Decimal(math.inf)),
            ],
            Pollutant.NO2: [
                (Decimal('0'), Decimal('60')),
                (Decimal('60.1'), Decimal('260')),
                (Decimal('260.1'), Decimal('1130')),
                (Decimal('1130.1'), Decimal('2260')),
                (Decimal('2260.1'), Decimal('3000')),
                (Decimal('3000.1'), Decimal(math.inf)),
            ],
            Pollutant.CO: [
                (Decimal('0'), Decimal('4.5')),
                (Decimal('4.6'), Decimal('9.0')),
                (Decimal('9.1'), Decimal('15')),
                (Decimal('15.1'), Decimal('30')),
                (Decimal('30.1'), Decimal('40')),
                (Decimal('40.1'), Decimal(math.inf)),
            ],
            Pollutant.O3: [
                (Decimal('0'), Decimal('70')),
                (Decimal('70.1'), Decimal('140')),
                (Decimal('140.1'), Decimal('200')),
                (Decimal('200.1'), Decimal('400')),
                (Decimal('400.1'), Decimal('600')),
                (Decimal('600.1'), Decimal(math.inf)),
            ],
        },
        'desc': [
            'good',
            'moderate',
            'inadequate',
            'bad',
            'terrible',
            'critical',
        ],
    }
