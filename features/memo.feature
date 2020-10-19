Feature: Testing Google Classroom-esque homework

  Scenario: deliver homework
     Given we have homework
      When we turn it in
      Then the homework is marked as done

  Scenario: miss homework
     Given we have homework
      When the due date arrives
      Then the homework is marked as missing

  Scenario: deliver missing homework
     Given we have missing homework
      When we turn it in
      Then the homework is marked as late