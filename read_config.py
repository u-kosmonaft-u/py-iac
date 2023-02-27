import yaml
from pathlib import Path

"""
Class for read config file
"""

default_config = """
main:
  ssh:
    pub: ~/.id_rsa.pub
  git:
    user:
    password:
  ee:
"""


def read_conf(conf):
    try:
        with open(conf) as file:
            config_file: list = yaml.safe_load(file)
    except Exception as e:
        print(f"Error open config file {e}")
        exit(1)
    return config_file


class ConfigReader(object):

    def __init__(self, config="pyiac_conf.yaml"):
        self.config = config

        config_file = Path(str(Path.home()) + "/" + config)
        try:
            config_file.resolve(strict=True)
        except FileNotFoundError:
            print("No config file found! Creating...")
            load = yaml.safe_load(default_config)
            with open(config_file, 'w') as file:
                yaml.dump(load, file)
                read_conf(config_file)
        else:
            read_conf(config_file)
