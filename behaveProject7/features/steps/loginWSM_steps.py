from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@given("I launch Chrome browser")
def openChrome(context):

    # create object driver
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when("I open WSM home page")
def openWSM(context):

    # get link WSM with basic authen
    try:
        context.driver.get("https://wsm:dangnhap_wsm@edev.sun-asterisk.vn/")
    except Exception as e:
        return "Can't access the website {}".format(e)

    # click login button
    element_btnLogin = "body > div.wsm-index > div.slide-wsm-content.display-none > a"
    play_btnLogin = context.driver.find_element_by_css_selector(element_btnLogin)
    play_btnLogin.click()


@when('I input username "{username}" and password "{password}"')
def input(context, username, password):

    # input username
    element_txtUsername = "#user_email"
    input_txtUsername = context.driver.find_element_by_css_selector(element_txtUsername)
    input_txtUsername.send_keys(username)

    # input password
    element_txtPassword = "#user_password"
    input_txtPassword = context.driver.find_element_by_css_selector(element_txtPassword)
    input_txtPassword.send_keys(password)


@when("I click on login buttons")
def clickLogin(context):

    # click Ok button to login
    element_btnOK = "#wsm-login-button"
    play_btnOK = context.driver.find_element_by_css_selector(element_btnOK)
    play_btnOK.click()


@then("I login succesfully")
def loginSuccesfully(context):

    try:
        title = context.driver.current_url()
        assert title == "Bảng thời gian của bạn | Working space"
    except Exception as e:
        return "Something wrong {}".format(e)

@then("I login failed")
def loginFailed(context):

    try:
        title = context.driver.title
        assert title == "Working space"
    except Exception as e:
        return "Something wrong {}".format(e)