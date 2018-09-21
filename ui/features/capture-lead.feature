# Created by tam.nguyen at 9/21/18
Feature: Lead Capture Form
  # Enter feature description here

  Scenario: Submit valid information
    Given I load "Lead Capture Form"
    When I fill all valid information
    Then I should see correct information on database level

  #Scenario: Check required fields
  #  Given I load "Lead Capture Form"
  #  When I fill all valid information
    #Then I should see correct information update to database

  #Scenario: Check State options
  #  Given I load "Lead Capture Form"
  #  When I fill all valid information
    #Then I should see correct information update to database

  #Scenario: Check datetime picker
  #  Given I load "Lead Capture Form"
  #  When I fill all valid information
    #Then I should see correct information update to database