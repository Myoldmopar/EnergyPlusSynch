from unittest import TestCase

from energyplus_api_synch.coordinator import main as main_coordinator


class TestCoordinator(TestCase):
    def test_coordinator(self):
        main_coordinator()
