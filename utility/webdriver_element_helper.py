# Created by ********  chomri01 at 8/12/2019

# Feature Name :: --

# To Do ::-
import sys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def implicit_wait(context, time=10):
	context.Browser.implicitly_wait(time_to_wait=time)
	pass


def explicit_wait(browser, *locator, time=10):
	try:

		wait = WebDriverWait(browser, timeout=time)
		element = wait.until(EC.presence_of_element_located(*locator))
		print("Element is displayed")
		return element.is_displayed()


	except TimeoutException as timeout:
		print("Loading took too much time!")
		return False
	except Exception as e:
		e = sys.exc_info()
		print("There are some error occurred " + str(e))
		return False
