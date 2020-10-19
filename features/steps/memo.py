from behave import *
from homework import Homework
from datetime import datetime, timedelta

use_step_matcher("re")


@given("we have homework")
def step_impl(context):
    context.homework = Homework(datetime.today())


@when("we turn it in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.homework.turn_in()


@then("the homework is marked as done")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert(context.homework.is_done())


@when("the due date arrives")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.homework.update(datetime.today() + timedelta(hours=1))


@then("the homework is marked as missing")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert(context.homework.is_missing())


@given("we have missing homework")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    yesterday = datetime.today() - timedelta(days=1)
    context.homework = Homework(due_date=yesterday)
    context.homework.update(datetime.today())


@then("the homework is marked as late")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert (context.homework.is_late())
