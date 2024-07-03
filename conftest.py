import os
import pytest
from pages.customer_login import CustomerLoginPage


@pytest.fixture(autouse=True)
def go_to_base_url(page):
    page.goto(os.getenv('BASE_URL'), timeout=60000)

    yield page

    page.close()


@pytest.fixture()
def login_customer(page):
    customer_login_page = CustomerLoginPage(page)
    customer_login_page.navigate_to_sign_in()
    customer_login_page.login_customer(os.getenv('USERNAME'), os.getenv('PASSWORD'))
