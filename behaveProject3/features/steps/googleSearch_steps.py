from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@given(u'I launch Chrome browser')
def launchChrome(context):

    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when(u'I open google homepage')
def openGoogle(context):

    # get url "https://www.google.com.vn/?client=safari&channel=iphone_bm"
    context.driver.get("https://www.google.com.vn/?client=safari&channel=iphone_bm")

@when(u'I input "{my_str}" to search on google homepage')
def enterString(context, my_str):

    # input string
    elemenInput = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
    inputString = context.driver.find_element_by_xpath(elemenInput)
    inputString.send_keys(my_str, Keys.CLEAR)

@when(u'I click on button search')
def clickSearch(context):

    # click search button
    element_btnSearch = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]"
    play_btnSearch = context.driver.find_element_by_xpath(element_btnSearch)
    play_btnSearch.click()

@when(u'I verify that text Muon roi ma sao con on google search')
def verifyText(context):

    try:
        text = context.driver.find_element_by_xpath('//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input').text
    except:
        assert text == "Muon roi ma sao con"

@then(u'User must be successfully searched on google homepage')
def succesfullySearch(context):

    # close website
    context.driver.close()
