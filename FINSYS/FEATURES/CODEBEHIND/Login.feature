#StoryType=WEB
#Owner=ejagruti
#CreationDate=24-12-2017 Sunday
@Login
Feature: Login Feature

  Background:user is successfully logged in
  Given user opens the "http://localhost:90/finsys" url

   @Smoke @EndToEnd
   Scenario: Login Functionality for valid username and password  behave
    Given user is on the application login page
    When user enters "dummyfm" as username
    And user enters "passw0rd" as password
    And user clicks on login button
    Then user is on the application home page
    And user gets the message starting with "Welcome" on the top


  @Smoke @EndToEnd
  Scenario: Login Functionality for Invalid username and Invalid password behave
    Given user is on the application login page
    When user enters "invalidun" as username
    And user enters "invalidpass" as password
    And user clicks on login button
    Then user is on the application login page
    And user gets the error message starting with "Please Enter Valid" on the bottom


