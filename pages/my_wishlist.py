from pages.luma_base import LumaBasePage


class MyWishListPage(LumaBasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = '/wishlist/'

        self.update_wishlist_button = self.page.get_by_role("button", name="Update Wish List")

    def update_product_quantity_from_wishlist(self, product_name, product_quantity):
        self.page.get_by_role("link", name=product_name).first.hover()
        self.page.get_by_label("Qty").fill(product_quantity)
        self.success_alert.click()
        self.update_wishlist_button.click()
