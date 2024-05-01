from pages.luma_base import LumaBasePage


class CustomerLoginPage(LumaBasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = '/customer/account/login/'

        self.email_input = self.page.get_by_label("Email", exact=True)
        self.password_input = self.page.get_by_label("Password")
        self.sign_in_button = self.page.get_by_role("button", name="Sign In")

    def login_customer(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.sign_in_button.click()
