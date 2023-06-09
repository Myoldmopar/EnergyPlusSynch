from os import environ
from unittest import TestCase

from energyplus_api_synch.configuration import VersionMap
from energyplus_api_synch.coordinator import Coordinator


class TestCoordinator(TestCase):
    def test_coordinator(self):
        ep_version = environ.get('EP_SYNCH_EP_VERSION', "23.1")
        ep_object = VersionMap[ep_version]
        Coordinator(ep_object)
