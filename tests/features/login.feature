Feature: Login
    In order to play with Lettuce
    As beginners on local environment
    We'll implement login functionality

    Scenario: Check if User able to sing-in as Customer Outreach Team Member
        Given I am signed in as single user
        Then I should see landing page

    Scenario: Remember email on the login form
        Given I want to remember my login nick@fd.com after sign in
        When I sign out from application
        Then I see login page with pre-populated email nick@fd.com
