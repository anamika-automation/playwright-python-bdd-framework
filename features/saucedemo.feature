Feature: SauceDemo end to end automation

  Scenario: Complete SauceDemo shopping flow

    Given I am on the SauceDemo login page
    When I login with valid credentials
    And I open the About section
    And I navigate to Mobile App Distribution
    And I request a demo
    And I submit the demo request
    And I return to SauceDemo
    And I add products to the cart
    And I remove selected products
    And I sort the products
    And I open the cart
    And I complete the checkout
    And I logout
    Then I should be logged out successfully