# Created by ********  chomri01 at 8/10/2019

# Feature Name :: --

# To Do ::-
from selenium import webdriver
chrome_path='D:\Learning\PythonworkStation\AutomationTesting\software\chromedriver.exe'
def load_driver(browser='chrome'):
	try:
		if browser.__contains__('chrome'):
			chrome_option=webdriver.ChromeOptions()
			chrome_option.add_argument('--disable-extensions')
			driver=webdriver.Chrome(chrome_options=chrome_option,executable_path=chrome_path)
			driver.maximize_window()
			return driver
		elif browser.__contains__('firefox'):
				print("Browser type is FireFox")
				return None
		else:
			chrome_option = webdriver.ChromeOptions()
			chrome_option.add_argument('--disable-extensions')
			driver = webdriver.Chrome(chrome_options=chrome_option, executable_path=chrome_path)
			driver.maximize_window()
			return driver
	except:
		print("There is an exception in load Driver")
		return None
