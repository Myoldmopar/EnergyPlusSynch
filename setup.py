from pathlib import Path
from setuptools import setup

from energyplus_api_synch import NAME, VERSION


readme_file = Path(__file__).parent.resolve() / 'README.md'
readme_contents = readme_file.read_text()

setup(
    name=NAME,
    version=VERSION,
    description='A demonstration of synchronously connecting EnergyPlus to other tools.',
    url='',
    license='',
    packages=['energyplus_api_synch'],
    package_data={},
    include_package_data=True,
    long_description=readme_contents,
    long_description_content_type='text/markdown',
    author="Edwin Lee",
    install_requires=['energyplus_api_helpers'],
    entry_points={'gui_scripts': [], 'console_scripts': []},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Utilities',
    ],
    platforms=[
        'Linux (Tested on Ubuntu)', 'MacOSX', 'Windows'
    ],
    keywords=[
        'EnergyPlus', 'eplus', 'Energy+',
        'Building Simulation', 'Whole Building Energy Simulation',
        'Heat Transfer', 'HVAC', 'Modeling',
        'Cosimulation'
    ]
)
