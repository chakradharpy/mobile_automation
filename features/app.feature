Feature: App Functionality

Scenario: Automate video playback and settings
    When I log in with PIN "WVMVHWBS"
    And I navigate to "Test automation project"
    And I switch to the "Details" tab
    And I switch back to the "Videos" tab
    And I play the video
    Then I should be able to pause the video
    And I replay the video using the Continue Watching button
    Then I pause the video and navigate back
    And I log out of the app
