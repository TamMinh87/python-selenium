Feature: Add Note
  # Enter feature description here

  Scenario: Add note
    Given I load "Test App" page
    When I submit valid credentials
    When I add note
    Then I should see a note

