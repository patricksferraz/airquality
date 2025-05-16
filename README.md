# Air Quality Index (AQI) for Python

[![PyPI version](https://badge.fury.io/py/airquality.svg)](https://badge.fury.io/py/airquality)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/patricksferraz/airquality)](https://github.com/patricksferraz/airquality/issues)
[![GitHub stars](https://img.shields.io/github/stars/patricksferraz/airquality)](https://github.com/patricksferraz/airquality/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/patricksferraz/airquality)](https://github.com/patricksferraz/airquality/network)

A Python package for calculating the Air Quality Index (AQI) based on the standards established by CONAMA Resolution No. 491/2018. This package provides a simple and efficient way to work with air quality data in Python.

## Table of Contents
- [Air Quality Index (AQI) for Python](#air-quality-index-aqi-for-python)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Quickstart](#quickstart)
  - [API Overview](#api-overview)
  - [Contributing](#contributing)
  - [License](#license)

## Features
- Calculate the Air Quality Index (AQI) for various pollutants.
- Supported pollutants: PM10, PM25, SO2, NO2, CO, O3.
- Easy-to-use API for quick integration into your projects.

## Installation
You can install the package directly from GitHub using pip:

```bash
pip install git+git://github.com/patricksferraz/airquality.git
```

## Quickstart
Here's a quick example of how to use the package:

```python
from airquality.aqi import Pollutant, Conama

conama = Conama()

# List available pollutants
conama.list_pollutants()
# Output: ['Pollutant.PM10', 'Pollutant.PM25', 'Pollutant.SO2', 'Pollutant.NO2', 'Pollutant.CO', 'Pollutant.O3']

# Calculate AQI for PM10 concentration = 40
conama.get_aqi(c=40, elem=Pollutant.PM10)
# Output: {'good': Decimal('50.00')}

# Calculate AQI for PM10 concentration = 120.5
conama.get_aqi(c=120.5, elem=Pollutant.PM10)
# Output: {'inadequate': Decimal('101.3017705927636643571978445')}

# Calculate AQI for SO2 concentration = 1620.5
conama.get_aqi(c=1620.5, elem=Pollutant.SO2)
# Output: {'terrible': Decimal('304.0400080016003200640128026')}
```

## API Overview
The package provides the following main classes and methods:

- **Conama**: A class that inherits from `AQI` and implements the standards established by CONAMA Resolution No. 491/2018.
  - `get_aqi(c: float, elem: Pollutant)`: Calculates the AQI for a given pollutant concentration.
  - `list_pollutants()`: Returns a list of all available pollutants.

- **Pollutant**: An enumeration of supported pollutants (PM10, PM25, SO2, NO2, CO, O3).

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
