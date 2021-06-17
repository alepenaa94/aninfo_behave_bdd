Feature: User virtual wallet

  As a user 
  I a want to add money in a virtual wallet
  So that i could be able to make a cashless purcharse

  Scenario: Create account successfully
    Given Pedro have not create any account
    When Pedro request the creation of an account
    Then Pedro will have in the account 0 dollar balance available
  
  Scenario: Create account unsuccessfully
    Given Pedro has an account with 10 dollar balance available
    When Pedro try to create another account
    Then An exception occurs

  Scenario: Delete account with money in account
    Given Pedro has an account with 10 dollar balance available
    When Pedro try to delete his account
    Then Pedro account has not been deleted 
    And An exception occurs

  Scenario: Delete account without money in account
    Given Pedro has an account with 10 dollar balance available
    When Pedro extract all balance available in account
    Then Pedro can delete his account

  Scenario: Deposit money
    Given Pedro has an account with 10 dollar balance available
    When Pedro add 150 dollar to the wallet
    Then Pedro will have in the account 160 dollar balance available

  Scenario: Withdrawal money
    Given Pedro has an account with 160 dollar balance available
    When Pedro extract 160 dollar
    Then Pedro will have in the account 0 dollar balance available

  Scenario: Buy a product
    Given Pedro has an account with 160 dollar balance available
    When Pedro buy a product of 159 dollar
    Then Pedro will have in the account 1 dollar balance available
    