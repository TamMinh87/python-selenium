# Created by tam.nguyen at 9/21/18
Feature: Lead Capture Form

  @smoke
  Scenario: Submit valid information
    Given I load "Lead Capture Form"
    When I submit all valid information
    Then I should see "Thank you" page
    Then I should see correct information on database level

  Scenario: Date picker
    Given I load "Lead Capture Form"
    When I submit all valid information with date from date picker
    Then I should see "Thank you" page
    Then I should see correct information on database level

  @negative
  Scenario: Check required fields
    Given I load "Lead Capture Form"
    When I submit empty form
    Then I should see correct error messages below each required field

  @data
  Scenario: Check State options
    Given I load "Lead Capture Form"
    Then I should see correct options under "State dropdown"
