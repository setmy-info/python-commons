from behave import *

from environment.variables import get_environment_variable
from environment.variables import get_environment_variables_list, \
    get_boolean_environment_variable, get_int_environment_variable, get_float_environment_variable, \
    get_json_environment_variable
from behave import *

from environment.variables import get_environment_variable
from environment.variables import get_environment_variables_list, \
    get_boolean_environment_variable, get_int_environment_variable, get_float_environment_variable, \
    get_json_environment_variable


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


@when('getting "{variable_name}" as JSON')
def step_getting_json(context, variable_name):
    context.actual_value = get_json_environment_variable(variable_name)
