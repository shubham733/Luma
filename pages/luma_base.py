from pages.base_page import BasePage
from playwright.sync_api import Page


class LumaBasePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.store_logo = self.page.get_by_label("store logo")
        self.whats_new_menu = self.page.get_by_role("menuitem", name="What's New")
        self.women_menu = self.page.get_by_role("menuitem", name="Women")
        self.men_menu = self.page.get_by_role("menuitem", name="Men")
        self.gear_menu = self.page.get_by_role("menuitem", name="Gear")
        self.training_menu = self.page.get_by_role("menuitem", name="Training")
        self.sale_menu = self.page.get_by_role("menuitem", name="Sale")
        self.sign_in_link = self.page.get_by_role("link", name="Sign In")
        self.create_account_link = self.page.get_by_role("link", name="Create an Account")
        self.global_search_input = self.page.get_by_placeholder("Search entire store here...")
        self.global_search_button = self.page.get_by_role("button", name="Search")
        self.my_cart_link = self.page.locator('.showcart')
        self.view_and_edit_cart_link = self.page.get_by_role("link", name="View and Edit Cart")
        self.tops_menu = self.page.get_by_role("menuitem", name="Tops")
        self.bottoms_menu = self.page.get_by_role("menuitem", name="Bottoms")
        self.jackets_menu = self.page.get_by_role("menuitem", name="Jackets")
        self.hoodies_and_sweatshirts_menu = self.page.get_by_role("menuitem", name="Hoodies & Sweatshirts")
        self.tees_menu = self.page.get_by_role("menuitem", name="Tees")
        self.bras_and_tanks_menu = self.page.get_by_role("menuitem", name="Bras & Tanks")
        self.pants_menu = self.page.get_by_role("menuitem", name="Pants")
        self.shorts_menu = self.page.get_by_role("menuitem", name="Shorts")
        self.tanks_menu = self.page.get_by_role("menuitem", name="Tanks")
        self.bags_menu = self.page.get_by_role("menuitem", name="Bags")
        self.fitness_equipment_menu = self.page.get_by_role("menuitem", name="Fitness Equipment")
        self.watches_menu = self.page.get_by_role("menuitem", name="Watches")
        self.video_download_menu = self.page.get_by_role("menuitem", name="Video Download")
        self.notes_link = self.page.get_by_role("link", name="Notes")
        self.search_terms_link = self.page.get_by_role("link", name="Search Terms")
        self.privacy_and_cookie_policy_link = self.page.get_by_role("link", name="Privacy and Cookie Policy")
        self.advanced_search_link = self.page.get_by_role("link", name="Advanced Search")
        self.orders_and_returns_link = self.page.get_by_role("link", name="Orders and Returns")
        self.product_name_link = self.page.locator('.product-item-name').get_by_role('link').first
        self.success_alert = self.page.locator("[data-ui-id='message-success']")
        self.error_alert = self.page.locator("[data-ui-id='message-error']")
        self.minicart_dialog = self.page.locator('#mini-cart')
        self.product_details_tile = self.page.locator('.product-item-details')
        self.remove_product_from_cart_ok_button = self.page.get_by_role("button", name="OK")
        self.cart_dialog_empty_product_title = self.page.locator('.subtitle.empty')
        self.welcome_banner = self.page.locator('.logged-in').first

    def search_product(self, search_keyword):
        self.global_search_input.fill(search_keyword)
        self.global_search_button.click()

    def navigate_to_what_is_new_tab(self):
        self.whats_new_menu.click()

    def navigate_to_women_tab(self):
        self.women_menu.click()

    def navigate_to_men_tab(self):
        self.men_menu.click()

    def navigate_to_gear_tab(self):
        self.gear_menu.click()

    def navigate_to_training_tab(self):
        self.training_menu.click()

    def navigate_to_sale_tab(self):
        self.sale_menu.click()

    def go_to_cart_dialog(self):
        self.page.wait_for_load_state('networkidle')
        self.my_cart_link.click()

    def navigate_to_sign_in(self):
        self.sign_in_link.click()

    def navigate_to_create_account(self):
        self.create_account_link.click()

    def navigate_to_women_sub_section(self, sub_section_name):
        self.women_menu.hover()
        if sub_section_name == 'Tops':
            self.tops_menu.click()
        if sub_section_name == 'Bottoms':
            self.bottoms_menu.click()

    def navigate_to_women_tops_sub_section(self, sub_section_name):
        self.women_menu.hover()
        self.tops_menu.hover()
        if sub_section_name == 'Jackets':
            self.jackets_menu.click()
        if sub_section_name == 'Hoodies & Sweatshirts':
            self.hoodies_and_sweatshirts_menu.click()
        if sub_section_name == 'Tees':
            self.tees_menu.click()
        if sub_section_name == 'Bras & Tanks':
            self.bras_and_tanks_menu.click()

    def navigate_to_women_bottoms_sub_section(self, sub_section_name):
        self.women_menu.hover()
        self.tops_menu.hover()
        if sub_section_name == 'Pants':
            self.pants_menu.click()
        if sub_section_name == 'Shorts':
            self.shorts_menu.click()

    def navigate_to_men_tops_sub_section(self, sub_section_name):
        self.men_menu.hover()
        self.tops_menu.hover()
        if sub_section_name == 'Jackets':
            self.jackets_menu.click()
        if sub_section_name == 'Hoodies & Sweatshirts':
            self.hoodies_and_sweatshirts_menu.click()
        if sub_section_name == 'Tees':
            self.tees_menu.click()
        if sub_section_name == 'Tanks':
            self.tanks_menu.click()

    def navigate_to_men_bottoms_sub_section(self, sub_section_name):
        self.men_menu.hover()
        self.tops_menu.hover()
        if sub_section_name == 'Pants':
            self.pants_menu.click()
        if sub_section_name == 'Shorts':
            self.shorts_menu.click()

    def navigate_to_gear_sub_section(self, sub_section_name):
        self.gear_menu.hover()
        if sub_section_name == 'Bags':
            self.bags_menu.click()
        if sub_section_name == 'Fitness Equipment':
            self.fitness_equipment_menu.click()
        if sub_section_name == 'Watches':
            self.watches_menu.click()

    def navigate_to_training_video_download_section(self):
        self.training_menu.hover()
        self.video_download_menu.click()

    def get_product_name_from_cart_dialog(self):
        return self.product_name_link.inner_text()

    def get_success_message(self):
        self.page.wait_for_load_state('networkidle')
        return self.success_alert.inner_text()

    def get_error_message(self):
        return self.error_alert.inner_text()

    def remove_product_from_cart_dialog(self, product_name):
        self.product_details_tile.filter(has_text=product_name).get_by_role("link", name='Remove').click()
        self.remove_product_from_cart_ok_button.click()

    def update_product_quantity_from_cart_dialog(self, product_name, product_quantity):
        self.product_details_tile.filter(has_text=product_name).get_by_label("Qty").fill(product_quantity)
        self.minicart_dialog.click()
        self.product_details_tile.filter(has_text=product_name).get_by_role("button", name="Update").click()

    def get_product_quantity_from_cart_dialog(self, product_name):
        self.page.wait_for_timeout(2000)
        return self.product_details_tile.filter(has_text=product_name).get_by_label("Qty").get_attribute('data-item-qty')

    def get_empty_product_message_from_cart_dialog(self):
        return self.cart_dialog_empty_product_title.inner_text()

    def get_product_name_from_my_wishlist(self):
        return self.product_name_link.inner_text()

    def remove_product_from_wishlist(self, product_name):
        self.product_details_tile.filter(has_text=product_name).get_by_title('Remove This Item').click()

    def get_welcome_greeting(self):
        self.page.wait_for_load_state('networkidle')
        return self.welcome_banner.inner_text()
