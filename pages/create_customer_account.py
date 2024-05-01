from pages.luma_base import LumaBasePage


class CreateCustomerAccountPage(LumaBasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = '/customer/account/create/'

        self.first_name_input = self.page.get_by_label("First Name")
        self.last_name_input = self.page.get_by_label("Last Name")
        self.email_input = self.page.get_by_label("Email", exact=True)
        self.password_input = self.page.get_by_role("textbox", name="Password*", exact=True)
        self.confirm_password_input = self.page.get_by_label("Confirm Password")
        self.create_account_button = self.page.get_by_role("button", name="Create an Account")
        self.email_error = self.page.locator('#email_address-error')
        self.password_error = self.page.locator('#password-confirmation-error')

    def create_customer_account(self, first_name, last_name, email, password, confirm_password):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.confirm_password_input.fill(confirm_password)
        self.create_account_button.click()

    def get_email_error_message(self):
        return self.email_error.inner_text()

    def get_password_confirmation_error_message(self):
        return self.password_error.inner_text()
