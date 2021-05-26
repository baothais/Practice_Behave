from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@given('I launch Chrome browser')
def launchChrome(context):
    context.driver = webdriver.Chrome()

@when('I open OrangeHRM home page')
def openOrangeHRM(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@when('I enter username "{username}" and password "{password}"')
def enter(context, username, password):
    context.driver.find_element_by_css_selector("#txtUsername").send_keys(username)
    context.driver.find_element_by_css_selector("#txtPassword").send_keys(password)

@when('I click on login button')
def step_impl(context):
    context.driver.find_element_by_css_selector("#btnLogin").click()

@then('User must be succesfully login to the Dashboard page')
def succesfullyLogin(context):
    try:
        text = context.driver.find_element_by_css_selector("#content > div > div.head > h1").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    else:
        assert text == "Dashboard", "Succesfully login"
    context.driver.close()
