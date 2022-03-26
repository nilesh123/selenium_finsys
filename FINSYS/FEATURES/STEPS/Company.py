import time

import allure
from allure_commons.types import AttachmentType
from behave import given,when,then
from selenium.webdriver.support.select import Select


@then(u'user click on Manage company link')
def clickManageCompanyLink(context):
     context.driver.find_element_by_xpath("//a[@title='Manage Company']").click()

@then(u'user click on New icon')
def clickNewIcon(context):
     context.driver.switch_to.frame("actionid")
     context.driver.find_element_by_xpath("//span[contains(text(),'New')]").click()

@then(u'user enter "{strCompanyname}" as company name')
def enterCompanyName(context,strCompanyname):
     context.driver.find_element_by_xpath("//input[@name='name']").clear()
     context.driver.find_element_by_xpath("//input[@name='name']").send_keys(strCompanyname)

@then(u'user Select "{strCompanyType}" as company type')
def selectCompanyType(context,strCompanyType):
     compType = Select(context.driver.find_element_by_id("companytype"))
     compType.select_by_visible_text(strCompanyType)
     time.sleep(2)

@then(u'user Select "{strCompanySubType}" as company subtype')
def selectCompanySubType(context,strCompanySubType):
     compSubType = Select(context.driver.find_element_by_name("subtype"))
     compSubType.select_by_visible_text(strCompanySubType)

@then(u'user enter "{strCompanyAddress}" as address')
def enterCompanyAddress(context,strCompanyAddress):
     context.driver.find_element_by_xpath("//span/textarea").send_keys("Pimple Nilkah Pune-27")

@then(u'user enter "{strCompanyPhoneNumber}" as phone number')
def enterCompanyPhoneNumber(context,strCompanyPhoneNumber):
     context.driver.find_element_by_xpath("//span/textarea").send_keys(strCompanyPhoneNumber)

@then(u'user enter "{strCompanyEmailAddress}" as email adress')
def enterCompanyEmailAddress(context,strCompanyEmailAddress):
     context.driver.find_element_by_name("email").send_keys(strCompanyEmailAddress)

@then(u'user enter "{strCompanyPanNumber}" as PAN number')
def enterCompanyPanNumber(context,strCompanyPanNumber):
     context.driver.find_element_by_name("pan").send_keys(strCompanyPanNumber)

@then(u'user enter "{strCompanyTinNumber} as TIN number')
def enterCompanyTinNumber(context,strCompanyTinNumber):
     context.driver.find_element_by_name("tin").send_keys(strCompanyTinNumber)

@then(u'user enter "{strCompanyMobileNumber}" as mobile number')
def enterCompanyMobileNumber(context,strCompanyMobileNumber):
     context.driver.find_element_by_xpath("//input[@name='mobile']/preceding-sibling::input").send_keys(strCompanyMobileNumber)


@then(u'user enter "{strCompanyWebsite}" as website')
def enterCompanyWebsite(context,strCompanyWebsite):
     context.driver.find_element_by_xpath("//input[@name='website']").send_keys(strCompanyWebsite)

@then(u'user Select "{strCompanyCountry}" as country')
def SelectCompanyCountry(context,strCompanyCountry):
     country = Select(context.driver.find_element_by_id("countryid"))
     country.select_by_visible_text(strCompanyCountry)
     time.sleep(2)

@then(u'user Select "{strCompanyState}" as state')
def SelectCompanyState(context,strCompanyState):
     state = Select(context.driver.find_element_by_id("stateidlist"))
     state.select_by_visible_text(strCompanyState)
     time.sleep(2)

@then(u'user Select "{strCompanyCity}" as city')
def SelectCompanyState(context,strCompanyCity):
     city = Select(context.driver.find_element_by_id("citylist"))
     city.select_by_visible_text(strCompanyCity)
     time.sleep(2)

@then(u'user enter "{strCompanyEmpolyee}" as number of employee')
def enterCompanyNumberOfEmployee(context,strCompanyEmpolyee):
     context.driver.find_element_by_xpath("//input[@name='totalemployee']/preceding-sibling::input").send_keys(strCompanyEmpolyee)
     time.sleep(2)

@then(u'user click on Save button')
def userClickSaveButton(context):
     context.driver.find_element_by_xpath("//span[contains(text(),'Save')]").click()
     time.sleep(5)

@then(u'user searches for added company name "{strCompanynameN}"')
def getAddedCompanyName(context,strCompanynameN):
     getcompNameCount= len(context.driver.find_elements_by_xpath("//td[@field='name']//div[contains(text(),'"+strCompanynameN+"')]"))
     time.sleep(10)
     print(getcompNameCount)
     compstatus = getcompNameCount > 0
     time.sleep(10)
     print("status for checking:---")
     print(compstatus)
     true_compstatus = bool(compstatus)
     time.sleep(10)
     allure.attach(context.driver.get_screenshot_as_png(), name='company_present',
                   attachment_type=AttachmentType.PNG)
     assert true_compstatus is True

@then(u'user click on Edit company "{strCompanynameE}" icon')
def clickEditCompanyName(context,strCompanynameE):
     context.driver.switch_to.frame("actionid")
     time.sleep(10)
     context.driver.find_element_by_xpath("//td[@field='name']//div[contains(text(),'"+strCompanynameE+"')]/ancestor::*//table[@class='datagrid-btable']/tbody/tr[1]/td[1]//span[1]").click()
     time.sleep(5)
