from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

use_step_matcher("re")


@given("Open Product Details page")
def open_details_page(context):
    context.driver.get('https://shop.cureskin.com/')


@step("Click to add product to cart")
def click_add_product(context):
    context.driver.find_element(By.CSS_SELECTOR, '.w-full button button--small').click()


@when('Verify "added to your cart" confirmation is shown')
def cart_information_shown(context):
     context.driver.find_element(By.CSS_SELECTOR, '.mini-cart__inner')


@step('Click "View my cart"')
def click_view_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, ".button button--secondary").click()


@then("Verify user is taken to the cart page")
def taken_to_cart(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])