Feature: Parts
  
  Scenario Outline: Chassis creation
    Given I create a series <series> chassis
    Then its stats are <handling>, <acceleration> and <breaking>

    Examples: Chassis
    | series | handling | acceleration | breaking |
    | 10     | 10       | 5            | 5        |
    | 20     | 20       | 10           | 10       |
    | 40     | 40       | 20           | 20       |

  Scenario Outline: Part creation
    Given I create a series <series> <part> with  <tweak> tweak
    Then its stats are <handling>, <acceleration> and <breaking>

    Examples: Wheels
    | part        | series | tweak        | handling | acceleration | breaking |
    | Wheels      | 10     | Vanilla      | 2        | 0.5          | 0.5      |
    | Wheels      | 10     | Handling     | 2.5      | 0.45         | 0.45     |
    | Wheels      | 10     | Acceleration | 1.8      | 0.625        | 0.45     |
    | Wheels      | 10     | Breaking     | 1.8      | 0.45         | 0.625    |

Feature: Part catalogue