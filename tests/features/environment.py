from tests.lib.logger import *
from tests.lib.environment import GetEnvironment


log = BehaveLogger().get_behave_logger()
env = GetEnvironment("staging")

# Do not call project libraries from hooks functions!


def before_all(context):
    context.log = log
    context.env = env


def after_step(context, step):
    context.log.info(" ")
