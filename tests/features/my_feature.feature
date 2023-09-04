Feature: Testing Environment Variables

    Scenario: Accessing and parsing environment variables
        Given environment variable "TEST_ENVIRONMENT_VARIABLE" have value "abc,def,ghi"
        When getting "TEST_ENVIRONMENT_VARIABLE" environment variable
        Then I should get value as "abc,def,ghi"
