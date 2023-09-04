import os

from behave import *


@given('environment variable "{variable_name}" have value "{variable_value}"')
def step_given_environment_variable(context, variable_name, variable_value):
    os.environ[variable_name] = variable_value


@when('getting "{variable_name}" environment variable')
def step_when_get_environment_variable(context, variable_name):
    context.actual_value = os.getenv(variable_name)


@then('I should get value as "{expected_value}"')
def step_then_check_environment_variable(context, expected_value):
    assert context.actual_value == expected_value, f"Expected value: {expected_value}, Actual value: {context.actual_value}"
