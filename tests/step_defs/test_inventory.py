from pytest_bdd import scenario, given, when, then
from my_package.inventory import Inventory


@scenario('../features/inventory.feature', 'add items to inventory',
          example_converters={'x': int, 'y': int, 'z': int})
def test_add_items():
    pass


@given('there are <x> units of items of <item_type> in the inventory', target_fixture='inventory')
def step_imp(item_type, x):
    inv = Inventory()
    inv.set_item_quantity(item_type, x)
    return inv


@when('<y> units of the item are added')
def step_imp(inventory, item_type, y):
    inventory.add_items(item_type, y)


@then('the inventory has <z> units of the item in total')
def step_imp(inventory, item_type, z):
    actual_quantity = inventory.get_item_quantity(item_type)
    assert actual_quantity == z
