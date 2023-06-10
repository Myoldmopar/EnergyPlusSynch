from unittest import TestCase

from energyplus_api_synch.configuration import EnergyPlus231
from energyplus_api_synch.coordinator import worker


class TestCoordinator(TestCase):
    def test_coordinator(self):
        worker(EnergyPlus231)
