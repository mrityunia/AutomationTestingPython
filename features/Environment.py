# Created by ********  chomri01 at 8/10/2019

# Feature Name :: --

# To Do ::-

from utility import driver_details
def before_feature(context,Scenario):
	print("Feature Name is "+str(Scenario.name))
def before_scenario(context,Scenario):
	context.browser_name=Scenario.tags[0]
	context.Browser=driver_details.load_driver(context.browser_name)

