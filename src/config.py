import yaml


class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = yaml.load(open(self.config_file, "r"), Loader=yaml.FullLoader)

    def _merge(self, default_config, active_config):
        return {**default_config, **active_config}

    def get(self, proj_env):
        default_config = self.config["default"]
        active_config = self.config[proj_env]
        merged_config = self._merge(default_config, active_config)
        return merged_config
