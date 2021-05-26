from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@given(u'I launch Chrome browser')
def launchChrome(context):

    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when(u'I open Phptravels admin homepage')
def openPhptravels(context):

    # get url "https://www.phptravels.net/admin"
    context.driver.get("https://www.phptravels.net/admin")

@when(u'I enter username "{username}" and password "{password}"')
def enterAccount(context, username, password):

    # input username
    elementUsername = "/html/body/div[2]/form[1]/div[1]/label[1]/input"
    inputUsername = context.driver.find_element_by_xpath(elementUsername)
    inputUsername.send_keys(username)

    # input password
    elementPassword = "/html/body/div[2]/form[1]/div[1]/label[2]/input"
    inputPassword = context.driver.find_element_by_xpath(elementPassword)
    inputPassword.send_keys(password)

@when(u'I click on login button')
def clickLogin(context):

    # click login button
    elementLogin = "/html/body/div[2]/form[1]/button"
    btnLogin = context.driver.find_element_by_xpath(elementLogin)
    btnLogin.click()

@then(u'User must be login successfully')
def succesfullyLogin(context):

    try:
        title = context.driver.title
    except:
        assert title == "Dashboard"

@then(u'User must be login unsuccessfully')
def unsuccesfullyLogin(context):

    try:
        title = context.driver.title
    except:
        assert title == "Adminstator Login"
