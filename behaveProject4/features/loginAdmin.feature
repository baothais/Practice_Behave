# Create by bao at 22/05/2021
# Updated by bao at 26/05/2021

Feature: Login Succesfully

  Background:
    Given I launch Chrome browser
    When I open Phptravels admin homepage

  @input_valid
  Scenario: Login to Phptravels admin homepage with valid account
    When I enter username "admin@phptravels.com" and password "demoadmin"
    And I click on login button
    Then User must be login successfully

  @input_invalid
  Scenario Outline: Login to Phptravels admin homepage with invalid account
    When I enter username "<username>" and password "<password>"
    And I click on login button
    Then User must be login unsuccessfully

    Examples:
      | username               |  password      |
      | admin1@phptravels.com  |  demoadmin     |
      | admin2@phptravels.com  |  demoadmin     |
      | admin3@phptravels.com  |  demoadmin     |