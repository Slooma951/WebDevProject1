Feature: User Login
  As a registered user
  I want to log into the system
  So that I can access my dashboard

  Scenario: Successful login
    Given a user exists with email "coach@club.com" and password "password"
    When the user logs in with valid credentials
    Then they should be redirected to the dashboard
