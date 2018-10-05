Feature: Login
  # Enter feature description here

  Scenario: Login succeed
    Given I load "Test App" page
    When I submit valid credentials
    Then I should see "My Note" page

