Feature: get triangle type
  I would like to know what kind of triangle, if possible,
  can be made from 3 sides with given lengths.

  Scenario Outline: get triangle type
    Given there are sides with length <a>, <b>, and <c>
    Then a triangle of <tri_type> can be constructed
    Examples:
      | a | b | c | tri_type    |
      | 0 | 2 | 1 | invalid     |
      | 3 | 3 | 3 | equilateral |
      | 4 | 4 | 2 | isosceles   |
      | 5 | 6 | 3 | scalene     |
      |-1 | 3 | 8 | invalid     |
      | 1000000000 | 2 | 1 | invalid     |
      | 300 | 300 | 300 | equilateral |
      | 123456 | 123456 | 2 | isosceles   |
      | 100 | 200 | 250 | scalene     |
      |-846713908492 | 3732894 | 0 | invalid     |