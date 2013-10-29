Feature: Smoke Dashboard
    In order to check basic dashboard functionality
    As CustomerOutreachTeamMember
    We'll try to use basic dashboard elements

    Background:
        Given I am signed in as "CustomerOutreachTeamMember"
        Then I should see "Dashboard"

    Scenario: Check if Dashboard has global search field and it's possible to perform search request
        Given I put "any" entity name to search field
        Then I found "any" entity in search result