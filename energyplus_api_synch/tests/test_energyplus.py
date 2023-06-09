from unittest import TestCase

from energyplus_api_synch.energyplus import EnergyPlus


class TestEnergyPlus(TestCase):
    def test_download_and_install(self):
        e = EnergyPlus()
        e.download_and_extract()
        pass
