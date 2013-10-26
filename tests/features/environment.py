from tests.lib.logger import *
from tests.lib.driver import Driver
from tests.lib.tests_environment import *


log = BehaveLogger().get_behave_logger()
env = GetEnvironment("staging")
drv = Driver
users = GetUsers()

# Do not call project libraries from hook functions!


def before_all(context):
    context.log = log
    context.env = env
    context.users = users


def before_scenario(context, scenario):
    context.driver = drv("firefox")


def after_step(context, step):
    context.log.info(" ")


def after_scenario(context, scenario):
    context.driver.close()


def after_all(context):
    context.log.info("TESTS ARE FINISHED")