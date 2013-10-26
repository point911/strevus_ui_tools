Feature: Login
    In order to play with Behave
    As beginners on local environment
    We'll implement login functionality

    Scenario Outline: Check if User able to sing-in as any user type
        Given I am signed in as "<user_type>"
        Then I should see "<landing_page>"

    Examples: set1
        | user_type                    | landing_page               |
        | CustomerOutreachTeamMember   | Dashboard                  |
        | Tax Person                   | Dashboard                  |
        | Internal Contact             | Internal Contact Entities  |


