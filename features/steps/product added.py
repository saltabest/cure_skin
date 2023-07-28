from behave import *
from selenium.webdriver.common.by import By
from time import sleep




@given("Open Product Details page")
def open_details_page(context):
    # context.driver.get('https://shop.cureskin.com/')
    context.app.main_page.open_main()


@step("Click to add product to cart")
def click_add_product(context):
    context.app.main_page.click_add_product()

@step("Close window")
def close_window_popup(context):
    context.app.main_page.close_popup()


@step("Click cart icon")
def step_impl(context):
    context.app.main_page.click_cart()

@when('Click "View my cart" on icon page')
def step_impl(context):
    context.app.main_page.view_my_cart()
@then("Verify user is taken to the cart page")
def taken_to_cart(context):
    context.app.main_page.view_cart_page()