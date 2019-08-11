Feature: This feature file is related to Smoke Test cases

@chrome
  Scenario: verify BrowserOpen
    Given the user opens browser
     When  the user navigates to url "http://automationpractice.com/index.php"
     Then "My Store" is opend

  @chrome
  @login
  Scenario: Verify login successful
    Given the user opens browser
     When  the user navigates to url "http://automationpractice.com/index.php"
      And  the user clicks on Signin
     Then Sign in page is opned
     When the user enters user id "xyz@abc.com" passwod "xyzas124"
      And the user clicks on sigin button
     Then the user gets success message
