# Created by ********  chomri01 at 8/10/2019

# Feature Name :: --

# To Do ::-
import sys

from pages.base_page_details import *
from selenium.webdriver.common.by import By

class HomePage(BasePage):

	def __init__(self,context):
		BasePage.__init__(
			self,
			context.Browser,
		)

	locator_dictionary={
			'sign_option':(By.CSS_SELECTOR,'#header > div.nav > div > div > nav > div.header_user_info > a')

		}
	def open_home_page(self,url):
		self.Browser.get(url)

	def get_homepage_title(self):
		return self.Browser.title

	def click_on_signin(self):
		self.Browser.find_element(*self.locator_dictionary['sign_option']).click()
		return None


class Login(BasePage):
	def __init__(self,context):
		BasePage.__init__(
			self,
			context.Browser
		)

	locator_dictionary = {
		"email_id": (By.ID, 'email'),
		"password": (By.ID, 'passwd'),
		"signin_button": (By.ID, 'SubmitLogin')
	}

	def login_success(self,email_id,passwrd):
		try:
			print("User login id "+str(email_id),end='')
			print("User password "+str(passwrd),end='')
			self.Browser.find_element(*self.locator_dictionary['email_id']).send_keys(str(email_id))
			self.Browser.find_element(*self.locator_dictionary['password']).send_keys(str(passwrd))
			self.Browser.click(*self.locator_dictionary['signin_button'])
			print("login Success")

		except Exception as e:
			e = sys.exc_info()[0]
			print("Some error occured at login "+str(e))
		return None
	def get_page_title(self):
		return self.Browser.title