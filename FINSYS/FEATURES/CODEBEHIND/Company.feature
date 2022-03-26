#Owner=ejagruti
#CreationDate=29-12-2021 Sunday
@Company
Feature: Company Feature

  Background:user is successfully logged in
  Given user opens the "http://localhost:90/finsys" url

  @Smoke @EndToEnd
  Scenario: Create company with valid data
    Given user is on the application login page
    When user enters "dummyfm" as username
    And user enters "passw0rd" as password
    And user clicks on login button
    Then user is on the application home page
    And user gets the message starting with "Welcome" on the top
    And user click on Manage company link
    And user click on New icon
    And user enter "nmd1" as company name
    And user Select "Manufacturing" as company type
    And user Select "Automobile" as company subtype
    And user enter "Pimple Nilkah Pune-27" as address
    And user enter "1231231233" as phone number
    And user enter "nmd1@yopamil.com" as email adress
    And user enter "ALKPD2696N" as PAN number
    And user enter "ALKPD2696N" as TIN number
    And user enter "1122334455" as mobile number
    And user enter "https://www.abc.com" as website
    And user Select "INDIA" as country
    And user Select "MAHARASHTRA" as state
    And user Select "PIMPRI CHINCHWAD" as city
    And user enter "10" as number of employee
    And user click on Save button
    And user searches for added company name "nmd1"

  @Smoke @EndToEnd
  Scenario: Edit company with valid data
    Given user is on the application login page
    When user enters "dummyfm" as username
    And user enters "passw0rd" as password
    And user clicks on login button
    Then user is on the application home page
    And user gets the message starting with "Welcome" on the top
    And user click on Manage company link
    And user click on Edit company "nmd1" icon
    And user enter "nmd2" as company name
    And user click on Save button
    And user searches for added company name "nmd2"