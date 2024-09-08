import configparser
from pathlib import Path
from .schema.bookmark import Config


def read_config():
    """Read and convert configuration file to Config model"""
    config_path = Path(__file__).parent.parent / "config.toml"
    config = configparser.ConfigParser()
    config.read(config_path)

    db_section = "database"
    if not config.has_section(db_section):
        raise configparser.Error(
            f"'{db_section}' section not defined in the config.toml file."
        )

    section_data = dict(config[db_section])
    return Config(**section_data)
