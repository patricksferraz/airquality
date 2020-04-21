from os import path
import setuptools
import airquality

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='airquality',
    version=airquality.__version__,
    author='Patrick Silva Ferraz',
    author_email='patrick.ferraz@outlook.com',
    description='Package with functions for working with air quality in python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/patricksferraz/airquality',
    packages=setuptools.find_packages(),
    keywords=[
        'conama',
        'air-quality-index',
        'resolution-491-2018',
        'ppm to microgram converter',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    license='MIT',
)
