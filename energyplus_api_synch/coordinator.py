from energyplus_api_synch.configuration import EnergyPlusVersion, EnergyPlus231
from energyplus_api_synch.energyplus import EnergyPlus


class Coordinator:
    def __init__(self, ep_version: EnergyPlusVersion):
        # Set up the E+ install
        e = EnergyPlus()
        e.download_and_extract(ep_version)
        api_helper = e.get_api_helper()
        api = api_helper.get_api_instance()
        state = api.state_manager.new_state()
        return_value = api.runtime.run_energyplus(
            state, [
                '-d',
                api_helper.get_temp_run_dir(),
                '-a',
                '-w',
                api_helper.weather_file_path(),
                api_helper.path_to_test_file('5ZoneAirCooled.idf')
            ]
        )


if __name__ == "__main__":  # pragma: no cover
    # add a CLI to switch between E+ versions
    # also respond to the EP_SYNCH_EP_VERSION environment variable too
    Coordinator(EnergyPlus231)
