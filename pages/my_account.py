from pages.luma_base import LumaBasePage


class MyAccountPage(LumaBasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = '/customer/account/'

        self.edit_link = self.page.get_by_role("link", name="Edit", exact=True)
        self.change_password = self.page.get_by_role("link", name="Change Password")
        self.manage_addresses_link = self.page.get_by_role("link", name="Manage Addresses")
        self.edit_billing_address_link = self.page.get_by_role("link", name="Edit Address").first
        self.edit_shipping_address_link = self.page.get_by_role("link", name="Edit Address").nth(1)
