# Created by Eugene at 7/19/2023
Feature: User can add a product to a cart

  Scenario:
  Given Open Product Details page
  And Click to add product to cart
  When Verify "added to your cart" confirmation is shown
  And Click "View my cart"
  Then Verify user is taken to the cart page
