Feature: Request Item
  As a player or coach
  I want to request equipment
  So that I can use it during training or matches

  Scenario: Submit item request
    Given the user is logged in as a Coach
    And they are viewing a list of items
    When they click "Request" on a football
    Then a request should be created with status "Pending"
