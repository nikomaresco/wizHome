'''
Created on Sep 30, 2016

@author: niko
'''

import logging


log_level = logging.DEBUG
log_format = "%(asctime)s %(LevelName)s: %(message)s"

logger = logging.getLogger("main log")
logger.setLevel(log_level)


console_handler = logging.StreamHandler()

formatter = logging.Formatter(log_format)

console_handler.setLevel(log_level)
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

#logging.basicConfig(filename="log.log",level=log_level)

