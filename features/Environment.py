# Created by ********  chomri01 at 8/10/2019

# Feature Name :: --

# To Do ::-

from utility import driver_details


def before_feature(context, scenario):
	print("Feature Name is " + str(scenario.name))
	pass


def before_scenario(context, scenario):
	context.browser_name = scenario.tags[0]
	context.Browser=driver_details.load_driver(context.browser_name)
	pass


def after_scenario(context, scenario):
	if not str(scenario.tags).__contains__('@Debug') or not str(scenario.tags).__contains__('@debug'):
		context.Browser.close()
	pass
