import pytest
from faker import Faker as fake
from pages.create_customer_account import CreateCustomerAccountPage
from pages.my_account import MyAccountPage


random_data = {
    'first_name': fake().first_name(),
    'last_name': fake().last_name(),
    'email': fake().email(),
    'password': fake().password(),
    'alphanumeric': fake().bothify('?' * 4 + '@')
}


@pytest.mark.parametrize("first_name, last_name, email, password, confirm_password", [(
        random_data['first_name'], random_data['last_name'], random_data['email'],
        random_data['password'], random_data['password']),
    (random_data['alphanumeric'], random_data['alphanumeric'], random_data['alphanumeric'], random_data['alphanumeric'], random_data['password'])])
def test_create_customer_account(page, first_name, last_name, email, password, confirm_password):
    create_customer_account_page = CreateCustomerAccountPage(page)
    my_account_page = MyAccountPage(page)
    create_customer_account_page.navigate_to_create_account()
    create_customer_account_page.create_customer_account(first_name, last_name, email, password, confirm_password)
    if random_data['alphanumeric'] not in [first_name, last_name, email, password]:
        assert my_account_page.get_success_message() == 'Thank you for registering with Main Website Store.'
        assert my_account_page.get_welcome_greeting() == f"Welcome, {first_name} {last_name}!"
    else:
        assert create_customer_account_page.get_email_error_message() == ('Please enter a valid email address (Ex: '
                                                                          'johndoe@domain.com).')
        assert create_customer_account_page.get_password_confirmation_error_message() == ('Please enter the same value '
                                                                                          'again.')
