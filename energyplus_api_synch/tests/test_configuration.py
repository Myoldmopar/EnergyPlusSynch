from unittest import TestCase

from energyplus_api_synch.configuration import OperatingSystem, EnergyPlusVersion


class TestOperatingSystem(TestCase):
    def test_interface(self):
        os = OperatingSystem("a", "b", "c", "d")
        self.assertEqual(os.nickname, "a")
        self.assertEqual(os.with_version, "b")
        self.assertEqual(os.archive_extension, "c")
        self.assertEqual(os.archive_tool, "d")
        self.assertEqual(os.architecture, "x86_64")
        os_with_arch = OperatingSystem("a", "b", "c", "d", "e")
        self.assertEqual(os_with_arch.nickname, "a")
        self.assertEqual(os_with_arch.with_version, "b")
        self.assertEqual(os_with_arch.archive_extension, "c")
        self.assertEqual(os_with_arch.archive_tool, "d")
        self.assertEqual(os_with_arch.architecture, "e")


class TestEnergyPlusVersion(TestCase):
    def test_interface(self):
        ep = EnergyPlusVersion("a", "b")
        self.assertEqual(ep.version, "a")
        self.assertEqual(ep.sha, "b")
