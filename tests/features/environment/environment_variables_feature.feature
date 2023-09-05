Feature: Testing Environment Variables

    Scenario: Accessing and parsing environment variables
        Given environment variable "TEST_ENVIRONMENT_VARIABLE" have value "abc,def,ghi"
        When getting "TEST_ENVIRONMENT_VARIABLE" environment variable
        Then I should get value as "abc,def,ghi"

    Scenario: Getting un-trimmed environment variables
        Given environment variable "TEST_ENVIRONMENT_VARIABLE_2" have value " abc , def , ghi   "
        When getting "TEST_ENVIRONMENT_VARIABLE_2" environment variable
        Then I should get value as " abc , def , ghi   "

    Scenario: Getting un-trimmed environment variables into trimmed list
        Given environment variable "TEST_ENVIRONMENT_VARIABLE_3" have value " abc , def , ghi   "
        When getting "TEST_ENVIRONMENT_VARIABLE_3" environment variable as list
        Then I should get value list "['abc', 'def', 'ghi']"

    Scenario: Getting un-trimmed boolean environment variable
        Given environment variable "TEST_ENVIRONMENT_VARIABLE_5" have value "TRUE"
        When getting "TEST_ENVIRONMENT_VARIABLE_5" as boolean
        Then I should get evaluated value as "True"

    Scenario: Getting un-trimmed int environment variable
        Given environment variable "TEST_ENVIRONMENT_VARIABLE_6" have value "1234"
        When getting "TEST_ENVIRONMENT_VARIABLE_6" as integer
        Then I should get evaluated value as "1234"

    Scenario: Getting un-trimmed float environment variable
        Given environment variable "TEST_ENVIRONMENT_VARIABLE_7" have value "1234.5678"
        When getting "TEST_ENVIRONMENT_VARIABLE_7" as float
        Then I should get evaluated value as "1234.5678"

    Scenario: Getting JSON string environment variable
        Given environment variable "TEST_ENVIRONMENT_VARIABLE_8" have value " { "name":    "John",   "age": 30, "city": "New York"}"
        When getting "TEST_ENVIRONMENT_VARIABLE_8" as JSON
        Then I should get JSON "{"age":30,"city":"New York","name":"John"}"
