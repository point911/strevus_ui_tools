Feature: InternalContact
    In order to check data
    As internal contact
    We'll implement login functionality

    Background:
        Given I am signed in as "Internal Contact"
        Then I should see "Internal Contact Entities"

    Scenario: Check if Page Entities linked to me has correct information, check after assign contact (Internal Contacts)
        When I check "any" legal entity detail
        Then I see myself "Internal Contact" assigned in contacts
