Feature: Login
    In order to play with Lettuce
    As beginners on local environment
    We'll implement login functionality

    Scenario Outline: Check if User able to sing-in as <user_type>
        Given I am signed in as <user>
        Then I should see "<landing_page>"

    Examples:
        | user_type                    | user                    | landing_page                 |
        | "Internal Conatct"           | "fred.wilson@ibank.com" | "Internal Contact Entities"  |
        | "CustomerOutreachTeamMember" | "nick@fd.com"           | "Dashboard"                  |
        | "Tax Person"                 | "lisa.lawk@ibank.com"   | "Dashboard"                  |

    Scenario: Remember email on the login form
        Given I want to remember my login nick@fd.com after sign in
        When I sign out from application
        Then I see login page with pre-populated email nick@fd.com
