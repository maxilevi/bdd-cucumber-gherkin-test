  Scenario: deliver homework
     Given we have homework
      When we turn it in
      Then the homework is marked as done
