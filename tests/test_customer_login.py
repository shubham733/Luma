import pytest
import os
from faker import Faker as fake
from pages.customer_login import CustomerLoginPage
from pages.my_account import MyAccountPage


random_data = {
    'email': fake().email(),
    'password': fake().password()
}


@pytest.mark.parametrize('email, password', [(os.getenv('USERNAME'), os.getenv('PASSWORD')),
                                             (random_data['email'], random_data['password']),
                                             (os.getenv('USERNAME'), random_data['password']),
                                             (random_data['email'], os.getenv('PASSWORD'))])
def test_customer_login(page, email, password):
    customer_login_page = CustomerLoginPage(page)
    my_account_page = MyAccountPage(page)
    customer_login_page.navigate_to_sign_in()
    customer_login_page.login_customer(email, password)
    if email == random_data['email'] or password == random_data['password']:
        assert customer_login_page.get_error_message() == ('The account sign-in was incorrect or your account is '
                                                           'disabled temporarily. Please wait and try again later.')
    else:
        assert my_account_page.get_welcome_greeting() == 'Welcome, Shubham Shelar!'
