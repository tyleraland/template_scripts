import os
import sys

from os import path
from csv import DictReader
from ConfigParser import SafeConfigParser
from SCons.Script import (Decider, Variables, Environment)

Decider('MD5-timestamp')

DATA_CONF = 'data.conf'

data = SafeConfigParser()
data.read(DATA_CONF)

venv = path.abspath('env')
activate_this = path.join(venv, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
os.environ['VIRTUAL_ENV'] = venv

PATH = [
    path.join(venv, 'bin'),
    'bin',
    '/usr/local/bin',
    '/usr/bin',
    '/bin'
]
parent_env = Environment(
    ENV = dict(os.environ, PATH=':'.join(PATH)),
    SHELL = 'bash',
)

parent_env['output'] = path.join(path.abspath('.'), 'output')
