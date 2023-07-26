import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page


class MainPage(Page):
    POP_UP_CLOSE = (By.XPATH, "//button[@class='popup-close']")
    ADD_BTN = (By.XPATH, "//add-to-cart[@class='w-full button button--small']")
    CART_BTN = (By.XPATH, "//svg[@class='bi bi-bag']")
    VIEW_MY_CART = (By.CSS_SELECTOR, '#cart-icon-bubble')


    def open_main(self):
        self.open_url('https://shop.cureskin.com/')

    def close_popup(self):
        self.wait_for_element_click(*self.POP_UP_CLOSE)

    def click_add_product(self):
        return self.driver.find_element(*self.ADD_BTN).click()

    def click_cart(self):
        self.driver.find_element(*self.CART_BTN).click()


    def view_my_cart(self):
        self.driver.find_element(*self.VIEW_MY_CART)

    def view_cart_page(self):
        return self.wait.until(EC.presence_of_element_located(*self.YOUR_CART))
