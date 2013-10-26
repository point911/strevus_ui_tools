import logging


class BehaveLogger(object):
    def __init__(self):
        self.steps_log_config = logging.basicConfig(filename="steps.log",
                                                    filemode='w',
                                                    level=logging.INFO)

    def get_behave_logger(self):
        return logging.getLogger(self.steps_log_config)


