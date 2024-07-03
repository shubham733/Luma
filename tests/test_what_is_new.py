import enum

import pytest

from faker import Faker as fake
from pages.what_is_new import WhatIsNewPage
from pages.my_wishlist import MyWishListPage
from conftest import login_customer


class Operations(enum.Enum):
    ADD = 'Add'
    UPDATE = 'Update'
    REMOVE = 'Remove'


@pytest.fixture()
def test_data():
    dictionary = dict()
    dictionary['product_name'] = 'Wayfarer Messenger Bag'
    dictionary['product_quantity'] = '6'
    return dictionary


@pytest.mark.parametrize('operation', [Operations.ADD, Operations.UPDATE, Operations.REMOVE])
def test_add_update_remove_product_from_cart(page, login_customer, operation, test_data):
    what_is_new_page = WhatIsNewPage(page)
    what_is_new_page.navigate_to_what_is_new_tab()
    what_is_new_page.add_product_to_cart(test_data["product_name"])
    what_is_new_page.go_to_cart_dialog()
    if operation is Operations.ADD:
        assert what_is_new_page.get_product_name_from_cart_dialog() == test_data["product_name"]
        assert what_is_new_page.get_success_message() == f'You added {test_data["product_name"]} to your shopping cart.'
    if operation is Operations.UPDATE:
        what_is_new_page.update_product_quantity_from_cart_dialog(test_data["product_name"], test_data["product_quantity"])
        assert what_is_new_page.get_product_quantity_from_cart_dialog(test_data["product_name"]) == test_data["product_quantity"]
    if operation is Operations.REMOVE:
        what_is_new_page.remove_product_from_cart_dialog(test_data["product_name"])
        what_is_new_page.go_to_cart_dialog()
        assert what_is_new_page.get_empty_product_message_from_cart_dialog() == ('You have no items in your shopping '
                                                                                 'cart.')


@pytest.mark.parametrize('operation', [Operations.ADD, Operations.UPDATE, Operations.REMOVE])
def test_add_update_remove_product_from_wishlist(page, login_customer, operation, test_data):
    what_is_new_page = WhatIsNewPage(page)
    my_wishlist_page = MyWishListPage(page)
    what_is_new_page.navigate_to_what_is_new_tab()
    what_is_new_page.add_product_to_wishlist(test_data["product_name"])
    if operation is Operations.ADD:
        assert what_is_new_page.get_product_name_from_my_wishlist() == test_data["product_name"]
        assert what_is_new_page.get_success_message() == (f'{test_data["product_name"]} has been added to your Wish List. Click '
                                                          'here to continue shopping.')
    if operation is Operations.UPDATE:
        my_wishlist_page.update_product_quantity_from_wishlist(test_data["product_name"], test_data['product_quantity'])
        assert my_wishlist_page.get_success_message() == f"{test_data['product_name']} has been updated in your Wish List."
    if operation is Operations.REMOVE:
        what_is_new_page.remove_product_from_wishlist(test_data["product_name"])
        assert what_is_new_page.get_success_message() == f'{test_data["product_name"]} has been removed from your Wish List.'
