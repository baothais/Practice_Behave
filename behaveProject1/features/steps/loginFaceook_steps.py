from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@given('I launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()

@when('I open Facebook home page')
def openFacebook(context):

    # get link facebook
    context.driver.get("https://www.facebook.com/")

    # maximize window
    context.driver.maximize_window()

@when('I enter username "{username}" and password "{password}"')
def enterAccount(context, username, password):

    # enter username
    context.driver.find_element_by_css_selector("#email").send_keys(username)

    # enter password
    context.driver.find_element_by_css_selector("#pass").send_keys(password)

@when('I click on login button')
def loginFacebook(context):

    # click login button
    context.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()

@then('User must be succesfully login to home page Facebook')
def succesfullyFacebook(context):

    time.sleep(5)
    context.driver.close()
