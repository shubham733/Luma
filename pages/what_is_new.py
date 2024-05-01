from pages.luma_base import LumaBasePage


class WhatIsNewPage(LumaBasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = '/what-is-new.html'

        self.title_heading = self.page.locator('.page-title-heading')
        self.shopping_cart_link = self.page.get_by_role("link", name="shopping cart")
        self.product_details_tile = self.page.locator('.product-item-details')

    def navigate_to_product_details(self, product_name):
        self.page.get_by_title(product_name).click()

    def select_product_size(self, product_name, product_size):
        self.product_details_tile.filter(has_text=product_name).get_by_label(product_size).click()

    def select_product_color(self, product_name, product_color):
        self.product_details_tile.filter(has_text=product_name).get_by_label(product_color).click()

    def add_product_to_cart(self, product_name, product_size, product_color):
        self.select_product_size(product_name, product_size)
        self.select_product_color(product_name, product_color)
        self.page.get_by_title(product_name).hover()
        self.product_details_tile.filter(has_text=product_name).get_by_title('Add to Cart').click()

    def add_product_to_wishlist(self, product_name, product_size, product_color):
        self.select_product_size(product_name, product_size)
        self.select_product_color(product_name, product_color)
        self.page.get_by_title(product_name).hover()
        self.product_details_tile.filter(has_text=product_name).get_by_title('Add to Wish List').click()

    def navigate_to_shopping_cart(self):
        self.shopping_cart_link.click()
