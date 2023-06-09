class OperatingSystem:
    def __init__(self, name: str, with_version: str, archive_extension: str, archive_tool: str, arch: str = 'x86_64'):
        self.nickname = name
        self.with_version = with_version
        self.archive_extension = archive_extension
        self.archive_tool = archive_tool
        self.architecture = arch


Ubuntu20 = OperatingSystem("Linux", "Ubuntu20.04", ".tar.gz", "tar -xf")
Ubuntu22 = OperatingSystem("Linux", "Ubuntu22.04", ".tar.gz", "tar -xf")
Mac = OperatingSystem("Darwin", "macOS12.1", ".tar.gz", "tar -xf")
Windows = OperatingSystem("Windows", "", ".zip", "7z x")


class EnergyPlusVersion:
    def __init__(self, version_string: str, sha: str):
        self.version = version_string
        self.sha = sha


EnergyPlus221 = EnergyPlusVersion("22.1.0", "ed759b17ee")
EnergyPlus222 = EnergyPlusVersion("22.2.0", "c249759bad")
EnergyPlus231 = EnergyPlusVersion("23.1.0", "87ed9199d4")
VersionMap = {"22.1": EnergyPlus221, "22.2": EnergyPlus222, "23.1": EnergyPlus231}
