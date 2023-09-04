from behave import *

from environment.variables import set_environment_variable, get_environment_variables_list, \
    get_boolean_environment_variable, get_int_environment_variable, get_float_environment_variable
from environment.variables import get_environment_variable


@given('environment variable "{variable_name}" have value "{variable_value}"')
def step_given_environment_variable(context, variable_name, variable_value):
    set_environment_variable(variable_name, variable_value)


@when('getting "{variable_name}" environment variable')
def step_when_get_environment_variable(context, variable_name):
    context.actual_value = get_environment_variable(variable_name)


@when('getting "{variable_name}" environment variable as list')
def step_when_get_environment_variable(context, variable_name):
    context.actual_value = get_environment_variables_list(variable_name)


@when('getting "{variable_name}" as boolean')
def step_impl(context, variable_name):
    context.actual_value = get_boolean_environment_variable(variable_name)


@when('getting "{variable_name}" as integer')
def step_impl(context, variable_name):
    context.actual_value = get_int_environment_variable(variable_name)


@when('getting "{variable_name}" as float')
def step_impl(context, variable_name):
    context.actual_value = get_float_environment_variable(variable_name)


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
