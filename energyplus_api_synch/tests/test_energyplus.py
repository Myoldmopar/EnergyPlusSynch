from pathlib import Path
from tempfile import mkdtemp
from unittest import TestCase

from energyplus_api_synch.configuration import Ubuntu20, EnergyPlus231
from energyplus_api_synch.energyplus import EnergyPlus


class TestEnergyPlus(TestCase):
    def test_download_and_install(self):
        e = EnergyPlus()
        temp_directory = Path(mkdtemp())
        new_eplus_root = temp_directory / f"eplus_install_{EnergyPlus231.version}"
        e.download_and_extract(EnergyPlus231, new_root_dir=new_eplus_root)
        expected_idd = new_eplus_root / 'Energy+.idd'
        self.assertTrue(expected_idd.exists())
