__author__ = 'point'

import json

environment_config_path = "/Users/strevus/PycharmProjects/StrevusLoginTest/tests/env/env.json"

class LoadConfig(object):
    def __new__(cls, name, path=environment_config_path):
        with open(path, 'r') as dcf:
            config = json.load(dcf)
            env_config = config[name]
        return env_config

class GetEnvironment(object):
    def __new__(cls, name):
        return LoadConfig(name)
