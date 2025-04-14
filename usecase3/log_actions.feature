Feature: Log Admin Actions
  As a system
  I want to log admin actions
  So that there is an audit trail of system activity

  Scenario: Admin logs an approval
    Given an admin approves a request
    Then the action "Approved request ID 3" should be logged with a timestamp
