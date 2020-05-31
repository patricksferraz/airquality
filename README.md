# aqi-conama

Package with functions for working with air quality in python

## Install

`pip install git+git://github.com/patricksferraz/airquality.git`

## Usage

### aqi.Conama

Module to calculate the air quality index based on the standards established by CONAMA Resolution No. 491/2018

```python
from airquality.aqi import Pollutant, Conama

conama = Conama()

# pollutant lists available
conama.list_pollutants()
# out: ['Pollutant.PM10', 'Pollutant.PM25', 'Pollutant.SO2', 'Pollutant.NO2', 'Pollutant.CO', 'Pollutant.O3']

# PM10 concentration = 40
conama.get_aqi(c=40, elem=Pollutant.PM10)
# out: {'good': Decimal('50.00')}

# PM10 concentration = 120.5
conama.get_aqi(c=120.5, elem=Pollutant.PM10)
# out: {'inadequate': Decimal('101.3017705927636643571978445')}

# SO2 concentration = 1620.5
conama.get_aqi(c=1620.5, elem=Pollutant.SO2)
# out: {'terrible': Decimal('304.0400080016003200640128026')}
```
