from pytest_bdd import scenario, given, then
from my_package import triangle


@scenario('../features/triangle.feature', 'get triangle type',
          example_converters={'a': int, 'b': int, 'c': int})
def test_get_triangle_type():
    pass


@given('there are sides with length <a>, <b>, and <c>',
       target_fixture='sides')
def step_imp(a, b, c):
    sides = [a, b, c]
    return sides


@then('a triangle of <tri_type> can be constructed')
def step_imp(sides, tri_type):
    constructed = triangle.get_triangle_type(sides)
    assert tri_type == constructed
