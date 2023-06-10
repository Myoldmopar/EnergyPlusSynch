from os import environ
from typing import Optional

import click

from energyplus_api_synch.configuration import EnergyPlusVersion, VersionMap
from energyplus_api_synch.energyplus import EnergyPlus


class Coordinator:
    def __init__(self, ep_version: EnergyPlusVersion):
        # Set up the E+ install
        e = EnergyPlus()
        e.download_and_extract(ep_version)
        api_helper = e.get_api_helper()
        api = api_helper.get_api_instance()
        state = api.state_manager.new_state()
        self.eplus_exit_code = api.runtime.run_energyplus(
            state, [
                '-d',
                api_helper.get_temp_run_dir(),
                '-a',
                '-w',
                api_helper.weather_file_path(),
                api_helper.path_to_test_file('5ZoneAirCooled.idf')
            ]
        )


def worker(energyplus_version_object: EnergyPlusVersion):
    c = Coordinator(energyplus_version_object)
    return c.eplus_exit_code


@click.command()
@click.option(
    "-e", "--energyplus-version",
    default=None,
    type=click.Choice(['22.1', '22.2', '23.1'], case_sensitive=False),
    required=False,
    help="The EnergyPlus Version to run; can also be set in the EP_SYNCH_EP_VERSION env variable"
)
def main(energyplus_version: Optional[str] = None):  # pragma: no cover  -- only covering the worker() level and below
    if energyplus_version:  # just use it as it is, click() will validate the entry
        pass
    else:  # try getting it from environment variable,
        energyplus_version = environ.get('EP_SYNCH_EP_VERSION', "23.1")
    return worker(VersionMap[energyplus_version])


if __name__ == '__main__':  # pragma: no cover  -- only covering the worker() level and below
    main()
