
from piny import YamlLoader
from pathlib import Path


class Config:
    def __init__(self):
        raise EnvironmentError(
            "Config is designed to be instantiated using the `Config.from_file()` method"
        )

    @staticmethod
    def _load_config(config_file):
        if Path(config_file).is_file():
            return YamlLoader(path=config_file).load()
        else:
            raise ValueError(f"{config_file} not found.")

    @staticmethod
    def _merge(default_config, active_config):
        """
        Merge two dictionaries
        :param default_config: default configurations
        :param active_config: active configurations
        :return: a merged dictionary
        """
        if default_config is None:
            return active_config
        elif active_config is None:
            return default_config
        else:
            return {**default_config, **active_config}

    @classmethod
    def from_file(cls, config_file, proj_env):
        """
        Get configurations for an active proj environment
        :param config_file: path to config file
        :param proj_env: active project environment: qa, prod, etc.
        :return: a dictionary that contains default and active config
        """
        config = cls._load_config(config_file)
        if "default" in config:
            default_config = config["default"]
        else:
            raise ValueError("You must provide a default configuration")
        if proj_env in config:
            active_config = config[proj_env]
        else:
            raise ValueError(f"Please provide {proj_env} parameters in {config_file}")
        merged_config = cls._merge(default_config, active_config)
        return merged_config
