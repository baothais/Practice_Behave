# Created by bao at 5/23/21
Feature: Login functional

    Background:
        Given I launch Chrome browser
        When I open WSM home page

    @input_invalid
    Scenario: input valid
        When I input username "admin.wsm@framgia.com.edev.test" and password "123456"
        And I click on login buttons
        Then I login succesfully

    @input_invalid
    Scenario Outline: input invalid
        When I input username "<username>" and password "<password>"
        And I click on login buttons
        Then I login failed

        Examples:
        |   username    |   password    |
        |   username    |   password    |
        |   username    |   password    |




