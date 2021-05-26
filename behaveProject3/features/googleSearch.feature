#Create by bao at 22/05/2021

Feature: Google Search

  Scenario: Search on google
    Given I launch Chrome browser
    When I open google homepage
    And I input "Muon roi ma sao con" to search on google homepage
    And I click on button search
    And I verify that text Muon roi ma sao con on google search
    Then User must be successfully searched on google homepage





