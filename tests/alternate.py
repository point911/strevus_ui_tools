import os
import sys
import json
import logging
from lettuce import *
from lib.driver import Driver
from lib.environment import GetEnvironment

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class InitWorld():
    __metaclass__ = Singleton

    def __init__(self):
        self.users_path = "/Users/strevus/PycharmProjects/StrevusLoginTest/tests/source/users.json"

        current_path = os.path.dirname(__file__)
        self.project_path = os.path.abspath(os.path.join(current_path, os.pardir))
        world.project_path = self.project_path
        sys.path.append(self.project_path)

        self.config_logger()
        world.log = logging.getLogger(self.steps_log_config)


        world.init_driver = Driver
        world.env = GetEnvironment('staging')

        world.users = self.GetUsers()

        world.log.info("USERS IN ALTERNATE: {0}".format(world.users))


    def config_logger(self):
        self.steps_log_config = logging.basicConfig(filename='steps.log',
                                       filemode='w',
                                       level=logging.INFO)

    def tear_down_world(self):
        os.system("killall -9 phantomjs")

    def GetUsers(self):
        with open(self.users_path, 'r') as usrs:
            users = json.load(usrs)
        return users
