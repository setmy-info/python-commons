import json

from behave import *


@then('I should get value as "{expected_value}"')
def step_then_check_environment_variable(context, expected_value):
    assert context.actual_value == expected_value, f"Expected value: {expected_value}, Actual value: {context.actual_value}"


@then('I should get evaluated value as "{expected_value}"')
def step_then_check_environment_variable(context, expected_value):
    expected_values = eval(expected_value)
    assert context.actual_value == expected_values, f"Expected value: {expected_value}, Actual value: {context.actual_value}"


@then('I should get value list "{expected_value}"')
def step_then_check_environment_variable(context, expected_value):
    expected_values = eval(expected_value)
    assert context.actual_value == expected_values, f"Expected value: {expected_value}, Actual value: {context.actual_value}"


@then('I should get JSON "{expected_value}"')
def step_then_check_environment_variable(context, expected_value):
    expected_values = json.loads(expected_value)
    assert context.actual_value == expected_values, f"Expected value: {expected_value}, Actual value: {context.actual_value}"
