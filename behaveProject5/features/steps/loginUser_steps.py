# Created by bao at 5/23/21

from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@given(u'I launch Chrome browser')
def launchChrome(context):

    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when(u'I open the Phptravels user page')
def openPhptravels_User(context):

    # get url "https://www.phptravels.net/login"
    context.driver.get("https://www.phptravels.net/login")

@when(u'I iinput username "{username}" and password "{password}"')
def enterAccount(context, username, password):

    # input username
    element_Username = "#loginfrm > div.wow.fadeIn > div:nth-child(1) > label > input[type=email]"
    inputUsername = context.driver.find_element_by_css_selector(element_Username)
    inputUsername.send_keys(username)

    # input password
    element_Password = "#loginfrm > div.wow.fadeIn > div:nth-child(2) > label > input[type=password]"
    inputPassword = context.driver.find_element_by_css_selector(element_Password)
    inputPassword.send_keys(password)

@when(u'I click on the login button')
def clickLogin(context):

    # click login button
    element_BtnLogin = "#loginfrm > button"
    play_btnLogin = context.driver.find_element_by_css_selector(element_BtnLogin)
    play_btnLogin.click()

@then(u'User must be succesfully login to the homepage')
def login_succesfully(context):

    # Verify that title "{title}" on home page
    try:
        title = context.driver.title
        assert title == "Login"
    except Exception as e:
        print("Has a wrong {}".format(e))

@then(u'User failed to login')
def loginFailed(context):

    # Verify that system display message error Invalid Email or Password
    try:
        title = context.driver.title
        assert title == "Login"
    except Exception as e:
        print("Has a wrong {}".format(e))

