# Created by bao at 5/26/21

  Feature: Login functional

    Background:
      Given I launch Chrome browser
      When I open Supplier homepage

    @input_valid
    Scenario: Login with valid accout
      When I input username "supplier@phptravels.com" and password "demosupplier"
      And I click on login button
      Then User must be login successfully

    @input_invalid
    Scenario Outline: Login with multiple invalid accounts
      When I input username "<username>" and password "<password>"
      And I click on login button
      Then User must be login unsuccessfully

      Examples:
      | username                    | password      |
      | supplier1@phptravels.com    | demosupplier  |
      | supplier2@phptravels.com    | demosupplier  |
      | supplier3@phptravels.com    | demosupplier  |