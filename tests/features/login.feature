Feature: Login
    In order to play with Lettuce
    As beginners on local environment
    We'll implement login functionality

    Scenario: Log in to localhost
        Given I have login url "http://localhost:1025"
        When I login through phantomjs
        Then I see dashboard url "dashboard"

