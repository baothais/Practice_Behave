Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given I launch Chrome browser
    When I open OrangeHRM home page
    And I enter username "admin" and password "admin123"
    And I click on login button
    Then User must be succesfully login to the Dashboard page


  Scenario Outline: Login to OrangeHRM with Multiple parameters
    Given I launch Chrome browser
    When I open OrangeHRM home page
    And I enter username "<username>" and password "<password>"
    And I click on login button
    Then User must be succesfully login to the Dashboard page

    Examples:
      | username  | password |
      | admin123  | admin    |
      | adminxyz  | admin123 |
      | admin     | adminxyz |
      | admin341  | adminxxx |

