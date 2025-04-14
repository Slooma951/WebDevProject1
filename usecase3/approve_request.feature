Feature: Approve Item Request
  As an admin
  I want to approve or reject item requests
  So that I can control equipment allocation

  Scenario: Admin approves a request
    Given a request is pending for a football
    When the admin clicks "Approve"
    Then the request status should be updated to "Approved"
