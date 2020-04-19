from os import path
import setuptools
import aqi_conama

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="aqi_conama",
    version=aqi_conama.__version__,
    author="Patrick Silva Ferraz",
    author_email="patrick.ferraz@outlook.com",
    description="Library to calculate the air quality index based on the standards established by CONAMA Resolution No. 491/2018",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/patricksferraz/aqi-conama",
    packages=setuptools.find_packages(),
    keywords=["conama", "air-quality-index", "resolution-491-2018"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    license="MIT",
)
