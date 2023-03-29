import yaml


class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = yaml.load(open(self.config_file, "r"), Loader=yaml.FullLoader)

    def _merge(self):
        return

    def get(self, proj_env):
        return
