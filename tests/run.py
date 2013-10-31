import os
from subprocess import call
os.chdir(os.path.dirname(os.path.realpath(__file__)))
call(["behave"])
