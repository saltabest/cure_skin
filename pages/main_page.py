import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Page


class MainPage(Page):

    POP_UP_CLOSE = (By.XPATH, "//button[@class='popup-close']")
    ADD_BTN = (By.XPATH, "//add-to-cart[@class='w-full button button--small']")
    CART_BTN = (By.ID, 'cart-icon-bubble')
    VIEW_MY_CART = (By.CSS_SELECTOR, '#cart-icon-bubble')
    YOUR_CART = (By.XPATH,"//h1[@class=[title']")


    def open_main(self):
        self.open_url('https://shop.cureskin.com/')

    def close_popup(self):
        self.wait_for_element_click(*self.POP_UP_CLOSE)

    def click_add_product(self):
        return self.driver.find_element(*self.ADD_BTN).click()



    def click_cart(self):
        sleep(10)
        self.wait_for_element_click(*self.CART_BTN)




    def view_my_cart(self):
        self.driver.find_element(*self.VIEW_MY_CART)

    def view_cart_page(self):
        self.find_element(*self.VIEW_MY_CART).get_attribute('value')
        assert int(cart_val) == 1, f"shopping cart has more than one items"
        e = self.wait_for_element_appear(*self.YOUR_CART)
        assert e.is_displayed(), f"element {e} is not displayed"
