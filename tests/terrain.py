__author__ = 'point'

import os
import sys
import logging
from lettuce import world

current_path = os.path.dirname(__file__)
project_path = os.path.abspath(os.path.join(current_path, os.pardir))
sys.path.append(project_path)

steps_log_config = logging.basicConfig(filename='steps.log',
                                       filemode='w',
                                       level=logging.INFO)


world.log = logging.getLogger(steps_log_config)
world.project_path = project_path

from lib.driver import Driver
from lib.environment import GetEnvironment


print("1 INIT WORLD")
world.init_driver = Driver
world.env = GetEnvironment('local')
print("2 WORLD IS: {0}".format(world))

