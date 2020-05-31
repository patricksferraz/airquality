# -*- coding: utf-8 -*-
"""The `airquality.aqi` module includes the air quality index based on the
standards established by CONAMA Resolution No. 491/2018
"""

from .Pollutant import Pollutant
from .Conama import Conama

__all__ = ['Pollutant', 'Conama']
