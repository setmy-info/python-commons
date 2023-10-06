from behave import *

from smi_python_commons.environment.variables import set_environment_variable


@given('environment variable "{variable_name}" have value "{variable_value}"')
def step_given_environment_variable(context, variable_name, variable_value):
    set_environment_variable(variable_name, variable_value)
