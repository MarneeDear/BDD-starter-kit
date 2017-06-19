from behave import *
from splinter import Browser
from hamcrest import assert_that, equal_to
# from selenium import webdriver

@given('we have behave installed')
def step_impl(context):
    # driver = webdriver.Firefox(executable_path="C:\\webdrivers\\geckdriver.exe")
    # driver.get('http://inventwithpython.com')
    browser = None
    driver_name = "firefox"
    browser = Browser(driver_name=driver_name) # , executable_path="C:\\webdrivers\\geckdriver.exe")
    browser.visit("https://www.google.com")
    if browser is not None:
        browser.quit();
    pass

@when('we implement a test')
def step_impl1(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl2(context):
    assert context.failed is False
