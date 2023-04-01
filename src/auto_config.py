
from piny import YamlLoader
from pathlib import Path


class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self._load_config()

    def _load_config(self):
        if Path(self.config_file).is_file():
            return YamlLoader(path=self.config_file).load()
        else:
            raise Exception(f"{self.config_file} not found.")

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

    def get(self, proj_env):
        """
        Get configurations for an active proj environment
        :param proj_env: active project environment: qa, prod, etc.
        :return: a dictionary that contains default and active config
        """
        if "default" in self.config:
            default_config = self.config["default"]
        else:
            raise Exception("You must provide a default configuration")
        if proj_env in self.config:
            active_config = self.config[proj_env]
        else:
            raise Exception(f"Please provide {proj_env} parameters in {self.config_file}")
        merged_config = self._merge(default_config, active_config)
        return merged_config
