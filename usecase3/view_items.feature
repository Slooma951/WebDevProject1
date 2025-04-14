Feature: View Items
  As a user
  I want to view all available inventory items
  So that I can see what's in stock

  Scenario: Viewing the item list
    Given the inventory contains footballs and cones
    When the user navigates to the items page
    Then they should see a list of available items
