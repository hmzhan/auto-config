import yaml


class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = yaml.load(open(self.config_file, "r"), Loader=yaml.FullLoader)

    @staticmethod
    def _merge(default_config, active_config):
        """
        Merge two dictionaries
        :param default_config: default configurations
        :param active_config: active configurations
        :return: a merged dictionary
        """
        if len(default_config) == 0:
            return default_config
        elif len(active_config) == 0:
            return active_config
        else:
            return {**default_config, **active_config}

    def get(self, proj_env):
        """
        Get configurations for an active proj environment
        :param proj_env: active project environment: qa, prod, etc.
        :return: a dictionary that contains default and active config
        """
        default_config = self.config["default"]
        try:
            active_config = self.config[proj_env]
            merged_config = self._merge(default_config, active_config)
            return merged_config
        except:
            print(f"Please provide {proj_env} parameters")

