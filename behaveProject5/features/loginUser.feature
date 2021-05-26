# Created by bao at 5/23/21

Feature: Logged in successfully

  Background:
    Given I launch Chrome browser
    When I open the Phptravels user page

  @valid_user
  Scenario: Login to Phptravels with valid user account
    When I iinput username "user@phptravels.com" and password "demouser"
    And I click on the login button
    Then User must be succesfully login to the homepage

  @invalid_user
  Scenario Outline: Login to Phptravels with multiple invalid user accounts
    When I iinput username "<username>" and password "<password>"
    And I click on the login button
    Then User failed to login

    Examples:
    | username              | password    |
    | user2@phptravels.com  | demouser    |
    | user3@phptravels.com  | demouser    |
    | user4@phptravels.com  | demouser    |






