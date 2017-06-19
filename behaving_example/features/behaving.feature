Feature: Text presence

    Background:
        # Given Firefox as the default browser
        Given a browser

    Scenario: Search for BDD
        When I visit "http://www.wikipedia.org/"
        And I fill in "search" with "BDD"
        # And I press "go"
        And I press the element with xpath "//*[@id='search-form']/fieldset/button"
        Then I should see "Behavior-driven development" within 5 seconds