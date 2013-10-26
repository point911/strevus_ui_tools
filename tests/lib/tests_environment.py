import json

environment_config_path = "/Users/strevus/PycharmProjects/StrevusLoginTest/tests/env/env.json"
users_path = "/Users/strevus/PycharmProjects/StrevusLoginTest/tests/source/users.json"


class LoadConfig(object):
    def __new__(cls, name, path=environment_config_path):
        with open(path, 'r') as dcf:
            config = json.load(dcf)
            env_config = config[name]
        return env_config

class LoadUsers(object):
    def __new__(cls, path=users_path):
        with open(users_path, 'r') as usrs:
            users = json.load(usrs)
        return users


class GetUsers(object):
    def __new__(cls):
        return LoadUsers()

class GetEnvironment(object):
    def __new__(cls, name):
        return LoadConfig(name)



