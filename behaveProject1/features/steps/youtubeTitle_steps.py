from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()

@when('open YouTube home page')
def openYoutube(context):
    context.driver.get("https://www.youtube.com/")

@then('verify that title YouTube on home page')
def verifyTitle(context):
    title = context.driver.title
    assert title == "YouTube"

@then('close browser')
def closeBrowser(context):
    time.sleep(5)
    context.driver.close()
