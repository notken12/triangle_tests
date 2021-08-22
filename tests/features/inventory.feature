Feature: manage inventory
  As an Amazon seller I want to manage my item inventory.
  I would like to be able to add or remove items of certain quantity and know the current quantity of each item type.

  Scenario Outline: add items to inventory
    Given there are <x> units of items of <item_type> in the inventory
    When <y> units of the item are added
    Then the inventory has <z> units of the item in total
    Examples:
      | item_type | x | y | z |
      | a         | 0 | 2 | 2 |
      | b         | 2 | 3 | 5 |
