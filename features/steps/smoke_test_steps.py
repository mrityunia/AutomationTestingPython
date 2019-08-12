# Created by ********  chomri01 at 8/10/2019

# Feature Name :: --

# To Do ::-

from pages.home_page_details import *

from behave import given, when, then


@given(u'the user opens browser')
def step_impl(context):
	print("Browser name: " + str(context.browser_name))


@when(u'the user navigates to url "{URL}"')
def step_impl(context, URL):
	print("URL is: " + str(URL))
	page = HomePage(context)
	page.open_home_page(URL)


@when(u'the user clicks on Signin')
def step_impl(context):
	page = HomePage(context)
	page.click_on_signin()


@when(u'the user enters user id "{userid}" passwod "{password}"')
def step_impl(context, userid, password):
	context.userid = userid
	context.passwd = password


@when(u'the user clicks on sigin button')
def step_impl(context):
	page = Login(context)
	page.login_success(context.userid, passwrd=context.passwd)
	pass


@then(u'"{title}" is opend')
def step_impl(context, title):
	print("Page Title is : " + str(title))
	page = HomePage(context)
	assert page.get_homepage_title() in title


@then(u'Sign in page is opned')
def step_impl(context):
	page = Login(context)
	assert page.get_page_title() in "Login - My Store"


@then(u'the user gets success message')
def step_impl(context):
	page = Login(context)
	assert page.get_loginSuccess_message() in ('Authentication failed.')
