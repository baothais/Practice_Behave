Feature: Facebook login

  Scenario: I login Facebook with account valid
    Given I launch chrome browser
    When I open Facebook home page
    And I enter username "0901142169" and password "0901142169Yy"
    And I click on login button
    Then User must be succesfully login to home page Facebook
