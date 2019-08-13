# Created by ********  chomri01 at 8/13/2019

# Feature Name :: --

# To Do ::-
import logging
import os

dir_path = os.getcwd() + '\\testdata\\logger.log'
print(dir_path)
if os.path.exists(dir_path):
	os.remove(dir_path)
	open(dir_path, 'w')
	logging.basicConfig(filename=dir_path, format='%(asctime)s: %(levelname)s: %(message)s', level=logging.DEBUG)
else:
	open(dir_path, 'w')
	logging.basicConfig(filename=dir_path, format='%(asctime)s: %(levelname)s: %(message)s', level=logging.DEBUG)


def start_logger():
	logging.debug("message 1 message 2")
