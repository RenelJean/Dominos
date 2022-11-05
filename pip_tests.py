from behave import *
import domino


@Given('I have created a new pip object')
def step_impl(context):
    pass


@When('I create the new class')
def step_impl(context):
    new_pip = domino.Pips(6)
    context.num_of_pips = 6
    assert new_pip is not None
    context.pip_holder = new_pip


@Then('the number of pips should be recorded')
def step_impl(context):
    assert context.pip_holder.count == context.num_of_pips


@Given('I have a set of dominoes')
def step_impl(context):
    context.domino_set = domino.Set(6)
    assert context.domino_set is not None


@When('I draw a domino')
def step_impl(context):
    context.num_of_dominoes = len(context.domino_set.set_of_dominoes)
    context.drawn_domino = context.domino_set.draw()
    assert context.drawn_domino is not None


@Then('It is removed from the stack')
def step_impl(context):
    assert len(context.domino_set.set_of_dominoes) < context.num_of_dominoes
    assert context.drawn_domino not in context.domino_set.set_of_dominoes


@When('I shuffle them')
def step_impl(context):
    context.original_set = context.domino_set.set_of_dominoes[0:]
    assert context.original_set is not None
    context.domino_set.scramble()


@Then('The order has changed')
def step_impl(context):
    assert context.original_set != context.domino_set.set_of_dominoes
