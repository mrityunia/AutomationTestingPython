# Created by ********  chomri01 at 8/10/2019

# Feature Name :: --

# To Do ::-
import sys
import time

from pages.base_page_details import *
from selenium.webdriver.common.by import By
from utility.webdriver_element_helper import *
from utility.logger_report_details import *

class HomePage(BasePage):

	def __init__(self, context):
		BasePage.__init__(
			self,
			context.Browser,
		)

	locator_dictionary = {
		'sign_option': (By.CSS_SELECTOR, '#header > div.nav > div > div > nav > div.header_user_info > a')

	}

	def open_home_page(self, url):
		self.Browser.get(url)

	def get_homepage_title(self):
		return self.Browser.title

	def click_on_signin(self):
		self.Browser.find_element(*self.locator_dictionary['sign_option']).click()
		return None


class Login(BasePage):
	def __init__(self, context):
		BasePage.__init__(
			self,
			context.Browser
		)

	locator_dictionary = {
		"email_id": (By.ID, 'email'),
		"password": (By.ID, 'passwd'),
		"signin_button": (By.ID, 'SubmitLogin'),
		"login_succ_msg": (By.CSS_SELECTOR, '#center_column > div.alert.alert-danger > ol > li')

	}

	def login_success(self, email_id, passwrd):
		try:
			start_logger()
			start_logger()
			start_logger()
			start_logger()
			start_logger()
			print("User login id " + str(email_id), end='')
			print("User password " + str(passwrd), end='')
			self.Browser.find_element(*self.locator_dictionary['email_id']).send_keys(str(email_id))
			self.Browser.find_element(*self.locator_dictionary['password']).send_keys(str(passwrd))
			self.Browser.find_element(*self.locator_dictionary['signin_button']).click()
			print("login Success")
		except Exception as e:
			e = sys.exc_info()[0]
			print("Some error occured at login " + str(e))
		return None

	def get_page_title(self):
		return self.Browser.title

	def get_loginSuccess_message(self):
		try:
			if explicit_wait(self.Browser, self.locator_dictionary['login_succ_msg'], time=11):
				login_message = self.Browser.find_element(*self.locator_dictionary['login_succ_msg']).text
				print("Login message " + str(login_message))
				return login_message
			return None
		except Exception as e:
			e = sys.exc_info()
			print("Login error message " + str(e))
			return None
