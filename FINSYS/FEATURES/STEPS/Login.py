import time

import allure
import FINSYS.FEATURES.Environment as U
#import FINSYS.Utility as U
from allure_commons.types import AttachmentType
from behave import given,when,then
from selenium import webdriver

@given(u'user opens the "{strURL}" url')
def OpenBrowser(context,strURL):
     browsername = context.config.userdata['browser']
     #browsername = "ch"
     print(browsername)
     if browsername == "ch":
          driver = webdriver.Chrome(context.config.userdata["ch_webdriver_exe"])
          #driver = webdriver.Chrome("D:\ejagruti_selenium_python\Drivers\chromedriver_win32\chromedriver.exe")
          context.driver = driver
     elif browsername == "ie":
          driver = webdriver.Ie(context.config.userdata["ie_webdriver_exe"])
          context.driver = driver
     print(strURL+" ####################")
     context.driver.get(strURL)
     print("done")
     context.driver. maximize_window()

@given(u'user is on the application login page')
def checkLoginPage(context):
     title = context.driver.title
     expectedTitle = "SBDC - Small Business Development Co."
     log_file = "D:\\ejagruti_selenium_python\\selenium_finsys\\FINSYS\\Logs\\Urlcheck.txt"
     pass_message = "Answered correctly - Question Number"
     fail_message = "Answered incorrectly - Question Number"
     if title == expectedTitle:
          print("Verfiy login page sucessfully")
          U.log("INFO",pass_message,log_file)
     else:
          print("Loging page verification faile")
          U.log("ERROR",fail_message,log_file)

@when(u'user enters "{strUsername}" as username')
def enterUsername(context,strUsername):
     context.driver.find_element_by_xpath("//input[@type='text']").send_keys(strUsername)

@when(u'user enters "{strPassword}" as password')
def enterPassword(context,strPassword):
     context.driver.find_element_by_xpath("//span/input[@type='password']").send_keys(strPassword)

@when(u'user clicks on login button')
def clickOnLoginbutton(context):
     context.driver.find_element_by_xpath("//span[@class='l-btn-text']").click()

@then(u'user is on the application home page')
def VerifyHomePage(context):
     homeTitle= context.driver.title
     ExptectTitle = "FinSys (SBDC) - eJagruti Educational Services"
     time.sleep(2)
     title_status = homeTitle == ExptectTitle
     time.sleep(2)
     assert title_status is True

@then(u'user gets the message starting with "{strWelcome}" on the top')
def getWelcomeMeg(context,strWelcome):
     welComeMsg= context.driver.find_element_by_xpath("//body/div/span").get_attribute("innerHTML")
     status = strWelcome in welComeMsg
     print(status)
     assert status is True

@then(u'user is on the application login page')
def verifyLoginPage(context):
     title = context.driver.title
     expectedTitle = "SBDC - Small Business Development Co."
     login_title_status = title == expectedTitle
     true_boolean = bool(login_title_status)
     assert true_boolean is True


@then(u'user gets the error message starting with "{strErrorMsg}" on the bottom')
def verifyInvalidError(context,strErrorMsg):
     actulaerror= context.driver.find_element_by_xpath("//div[@id='error']").get_attribute("innerHTML")
     error_status = strErrorMsg in actulaerror
     true_error_status = bool(error_status)
     allure.attach(context.driver.get_screenshot_as_png(), name='login_error_msg',
                   attachment_type=AttachmentType.PNG)
     assert true_error_status is True






