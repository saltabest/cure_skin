from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

POPUP_BTN = (By.CSS_SELECTOR, "div.popup__content")


@given("Open Product Details page")
def open_details_page(context):
    # context.driver.get('https://shop.cureskin.com/')
    context.app.main_page.open_main()


@step("Click to add product to cart")
def click_add_product(context):
    context.app.main_page.click_add_product()




@then("Verify user is taken to the cart page")
def taken_to_cart(context):
    context.app.main_page.view_cart_page()


@step("Close window")
def close_window_popup(context):
    context.app.main_page.close_popup()


@step("Click cart icon")
def step_impl(context):
    context.app.main_page.click_cart()


@step('Click "View my cart" on icon page')
def step_impl(context):
    context.app.main_page.view_my_cart()