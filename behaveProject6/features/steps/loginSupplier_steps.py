from behave import *
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

@given("I launch Chrome browser")
def launchChrome(context):

    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when("I open Supplier homepage")
def openSupplier(context):

    # get url "https://www.phptravels.net/supplier"
    try:
        context.driver.get("https://www.phptravels.net/supplier")
    except Exception as e:
        print("Has a wrong: {}".format(e))

@when('I input username "{username}" and password "{password}"')
def inputAccount(context, username, password):

    # input username
    elementUsername = "/html/body/div[2]/form[1]/div[1]/label[1]/input"
    inputUsername = context.driver.find_element_by_xpath(elementUsername)
    inputUsername.send_keys(username)

    # input password
    elementPassword = "/html/body/div[2]/form[1]/div[1]/label[2]/input"
    inputPassword = context.driver.find_element_by_xpath(elementPassword)
    inputPassword.send_keys(password)

@step("I click on login button")
def clickLogin(context):

    # click on login button
    elementLogin = "/html/body/div[2]/form[1]/button"
    btnLogin = context.driver.find_element_by_xpath(elementLogin)
    btnLogin.click()

@then("User must be login successfully")
def successfullyLogin(context):

    try:
        title = context.driver.title
    except:
        assert title == "Dashboard"

@then("User must be login unsuccessfully")
def unsuccessfullyLogin(context):

    try:
        title = context.driver.title
    except:
        assert title == "Supplier Login"