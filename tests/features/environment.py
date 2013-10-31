config_file = './behave.ini'

from ..lib.logger import *
from ..lib.driver import Driver
from ..lib.tests_environment import *

params = {}

with open(config_file, "r") as config:
    for line in config:
        nl = line.split("=")
        try:
            params[nl[0]] = nl[1].rstrip('\n')
        except IndexError:
            pass

log = BehaveLogger().get_behave_logger()
env = GetEnvironment(params['environment'])
drv = Driver
users = GetUsers()

# Do not call project libraries from hook functions!


def before_all(context):
    context.log = log
    context.env = env
    context.users = users


def before_scenario(context, scenario):
    context.driver = drv(params['driver'])


def after_step(context, step):
    context.log.info(" ")


def after_scenario(context, scenario):
    context.log.info("="*20)
    context.driver.delete_all_cookies()
    context.driver.close()
    del context.driver


def after_all(context):
    context.log.info("TESTS ARE FINISHED")