Feature: InternalContact
    In order to check data
    As internal contact
    We'll implement login functionality

    Background:
        Given I am signed in as "fred.wilson@ibank.com"
        Then I should see "Internal Contact Entities"

    Scenario: Check if Page Entities linked to me has correct information, check after assign contact (Internal Contacts)
        When I check "any" legal entity detail
        Then I see "myself" as "internal contact"