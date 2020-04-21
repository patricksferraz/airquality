# -*- coding: utf-8 -*-
from .Pollutant import Pollutant
from decimal import Decimal


class AQI:
    """Class containing the methods for calculating the air quality index

    Attributes
    -------
    standard: {}
        Dictionary with established standards

    Methods
    -------
    get_aqi(self, c: float, elem: Pollutant) -> {str: Decimal}
        Returns the air quality index
    """

    standard = None

    def get_aqi(self, c: float, elem: Pollutant) -> {str: Decimal}:
        """Function to calculate the air quality index using the standard

        Parameters
        ----------
        c : float
            pollutant concentration
        elem : Pollutant
            pollutant of the Pollutant type (e.g NO2 element == Pollutant.NO2)

        Returns
        -------
        {str: Decimal}
            returns the dictionary containing the qualification of the index
            and its value
        """

        def _calc(il, ih, cl, ch):
            return ((ih - il) / (ch - cl)) * (c - cl) + il

        if self.standard is None:
            raise ValueError('standard is not defined')
        if elem not in self.standard['bp'].keys():
            raise NameError('element is not in standard')

        c = Decimal(str(c))

        idx = 0
        for bp in self.standard['bp'][elem]:
            if c <= bp[1]:
                il, ih = self.standard['aqi'][idx]
                cl, ch = bp
                qual = self.standard['desc'][idx]
                return {qual: _calc(il, ih, cl, ch)}
            idx += 1

    @staticmethod
    def list_pollutants() -> [str]:
        """Returns the list of all available pollutants

        Returns
        -------
        [str]
            list with all available pollutants
        """
        return [str(p) for p in Pollutant]
