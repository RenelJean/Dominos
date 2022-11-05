Feature: testing all domino classes
  Scenario: test that pips are recorded correctly
    Given I have created a new pip object
    When I create the new class
    Then the number of pips should be recorded

  Scenario: drawing a domino removes it from the list
    Given I have a set of dominoes
    When I draw a domino
    Then It is removed from the stack

  Scenario: scrambling a domino changes the order
    Given I have a set of dominoes
    When I shuffle them
    Then The order has changed
