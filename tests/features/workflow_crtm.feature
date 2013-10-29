Feature: Workflow
    In order to test workflow functionality
    As Customer Response Team Member
    We'll test smoke workflow

    Background:
        Given I am signed in as "CustomerOutreachTeamMember"
        Then I should see "Dashboard"

    Scenario: Check if Page with Legal Entities in Pre-communication status has 4 doughnut charts
        When I click on entities tab
        Then I make choice on outreach status "Pre-communication"
        Then I see four doughunt charts

