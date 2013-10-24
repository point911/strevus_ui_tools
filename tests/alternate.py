import os
import sys
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
        # self.world = world

        current_path = os.path.dirname(__file__)
        self.project_path = os.path.abspath(os.path.join(current_path, os.pardir))
        world.project_path = self.project_path
        sys.path.append(self.project_path)

        self.config_logger()
        world.log = logging.getLogger(self.steps_log_config)


        world.init_driver = Driver
        world.env = GetEnvironment('staging')
        # self.get_world()


    def config_logger(self):
        self.steps_log_config = logging.basicConfig(filename='steps.log',
                                       filemode='w',
                                       level=logging.INFO)

    #def get_world(self):
    #    world = self.world

    def tear_down_world(self):
        os.system("killall -9 phantomjs")