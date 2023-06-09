from pathlib import Path
from platform import system, version
from os import environ
from shutil import copytree
from subprocess import check_call, CalledProcessError
from tempfile import mkdtemp
from typing import Optional

from energyplus_api_helpers.import_helper import EPlusAPIHelper

from energyplus_api_synch.configuration import (
    OperatingSystem as OpSys, EnergyPlusVersion as EpVer,
    Ubuntu20, Ubuntu22, Windows, Mac
)


class EnergyPlus:
    def __init__(self):
        self.eplus_root_dir: Optional[Path] = None

    def download_and_extract(self, ep: EpVer, new_root_dir: Optional[Path] = None):
        # Automatically detect the OS and version
        if system() == 'Windows':
            os = Windows
        elif system() == 'Darwin':
            os = Mac
        elif system() == 'Linux' and '20.04' in version():
            os = Ubuntu20
        elif system() == 'Linux' and '22.04' in version():
            os = Ubuntu22
        else:
            raise Exception("Could not match an Operating System Version, aborting")

        # Handle setting the path to the wget tool
        if 'CI' in environ and system() == 'Windows':
            wget = Path("C:") / "msys64" / "usr" / "bin" / "wget.exe"
        else:
            wget = "wget"  # assuming it's available on PATH

        # Handle setting up an ultimate EnergyPlus root dir
        if new_root_dir:
            self.eplus_root_dir = new_root_dir
        else:
            self.eplus_root_dir = Path(__file__).parent.parent / f"eplus_install_{ep.version}"
        if self.eplus_root_dir.exists():
            print(f"EnergyPlus root dir already exists at {self.eplus_root_dir}, skipping the download/extract")
            return

        # Download the EnergyPlus archive
        file_name = f"EnergyPlus-{ep.version}-{ep.sha}-{os.nickname}-{os.with_version}-{os.architecture}"
        file_name_with_ext = f"{file_name}{os.archive_extension}"
        target_download_path = Path(__file__).parent.parent / file_name_with_ext  # should be in repo root
        if target_download_path.exists():
            print(f"EnergyPlus archive already downloaded at {target_download_path}, skipping the download")
        else:
            full_url = f"https://github.com/NREL/EnergyPlus/releases/download/v{ep.version}/{file_name_with_ext}"
            try:
                check_call([str(wget), full_url, "-O", str(target_download_path)])
            except CalledProcessError:  # pragma: no cover
                raise Exception(
                    f"Could not download EnergyPlus archive from {full_url} or download to {target_download_path}"
                )

        # Extract the EnergyPlus archive, first into a temp dir, then grab the EnergyPlus-Blah subdirectory
        temp_extract_dir = mkdtemp()
        temp_extract_path = Path(temp_extract_dir)
        extract_command_line = os.archive_tool.split(' ')
        extract_command_line.extend([target_download_path, '-C', temp_extract_dir])
        try:
            check_call(extract_command_line)
        except CalledProcessError:  # pragma: no cover
            raise Exception(f"Could not execute extract operation; full command line: {extract_command_line}")
        subdirectories_in_temp_dir = [p for p in temp_extract_path.iterdir() if p.is_dir()]  # should be 1
        extracted_eplus_root = subdirectories_in_temp_dir[0]
        copytree(extracted_eplus_root, self.eplus_root_dir)

    def get_api_helper(self) -> EPlusAPIHelper:
        if not self.eplus_root_dir:
            raise Exception("Need to call download_and_extract() to set up the E+ install first!")
        return EPlusAPIHelper(self.eplus_root_dir)
