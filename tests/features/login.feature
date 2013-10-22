Feature: Login
    In order to play with Lettuce
    As beginners on local environment
    We'll implement login functionality

    Scenario: Check if User able to sing-in as Customer Outreach Team Member
        Given I am signed in as single user
        Then I should see landing page