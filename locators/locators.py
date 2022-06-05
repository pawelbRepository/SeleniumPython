from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '.user-info a')
    EMIAL_FIELD = (By.ID, 'field-email')
    PASSWORD_FIELD = (By.ID, 'field-password')
    LOGIN_BUTTON = (By.ID, 'submit-login')
    LOGIN_FAILED_MESSAGE = (By.XPATH, "//li[contains(text(),'Authentication failed.') "
                                      "or contains(text(),'Błąd uwierzytelniania.')]")
    NO_ACCOUNT_LINK = (By.CSS_SELECTOR, '.no-account>a')


class HomePageLocators:
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '.user-info .logout')


class NavigationPageLocators:
    MAIN_PAGE = (By.ID, '_desktop_logo')
    CATEGORY_CLOTHES = (By.ID, 'category-3')
    CATEGORY_CLOTHES_MEN = (By.ID, 'category-4')
    CATEGORY_CLOTHES_WOMEN = (By.ID, 'category-5')
    CATEGORY_ACCESSORIES = (By.ID, 'category-6')
    CATEGORY_ACCESSORIES_STATIONERY = (By.ID, 'category-7')
    CATEGORY_ACCESSORIES_HOME = (By.ID, 'category-8')
    CATEGORY_ART = (By.ID, 'category-9')
    LANGUAGE_DROP_DOWN = (By.ID, '_desktop_language_selector')
    LANGUAGE_OPTION_ENGLISH = (By.CSS_SELECTOR, '#_desktop_language_selector .dropdown-item')[0]
    LANGUAGE_OPTION_POLISH = (By.CSS_SELECTOR, '#_desktop_language_selector .dropdown-item')[1]
    SEARCH_FIELD = (By.CSS_SELECTOR, '.ui-autocomplete-input')
    LOGOUT = (By.CSS_SELECTOR, '.user-info .logout')
    ACCOUNT = (By.CSS_SELECTOR, '.user-info .account')
    CART = (By.CSS_SELECTOR, '_desktop_cart')
    CART_NUMBER_OF_ITEMS = (By.CSS_SELECTOR, '#_desktop_cart .cart-products-count')


class AddToCartPageLocators:
    PRODUCT_LIST = (By.CSS_SELECTOR, '#js-product-list .products .product')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.add .add-to-cart')
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, '.cart-content-btn .btn-secondary')
    PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, '.cart-content-btn .btn-primary')
    PRODUCT_CUSTOMIZATION_ELEMENT = (By.CSS_SELECTOR, '.product-customization-item')
    PRODUCT_CUSTOMIZATION_SAVE_BUTTON = (By.NAME, 'submitCustomizedData')
    PRODUCT_CUSTOMIZATION_TEXT_FIELD = (By.CSS_SELECTOR, 'textarea#field-textField1')


class RegistrationPageLocators:
    REGISTRATION_PAGE_EXPECTED_TEXT_ELEMENT = (By.CSS_SELECTOR, '.page-header')
    RADIOBUTTON_GENDER_MEN = (By.ID, 'field-id_gender-1')
    FIRST_NAME_FILED = (By.ID, 'field-firstname')
    LAST_NAME_FIELD = (By.ID, 'field-lastname')
    EMAIL_FIELD = (By.ID, 'field-email')
    PASSWORD_FIELD = (By.ID, 'field-password')
    CONSENT_1_OF_2 = (By.NAME, 'customer_privacy')
    CONSENT_2_OF_2 = (By.NAME, 'psgdpr')
    WRONG_EMAIL_ERROR_MESSAGE_FIELD = (By.CSS_SELECTOR, '#customer-form>div>div:nth-child(4)>div.col-md-6>div>ul>li')
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'button.btn-primary.form-control-submit ')


class CartPageLocators:
    PROCEED_TO_ORDER_BUTTON = (By.CSS_SELECTOR, 'a.btn-primary')


class OrderPageLocators:
    ORDER_PAGE_VERIFICATION_TEXT_ELEMENT = (By.CSS_SELECTOR, 'section#checkout-personal-information-step')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'form>button.continue.btn-primary')
    CONFIRM_ADDRESS_BUTTON = (By.NAME, 'confirm-addresses')
    CONFIRM_SHIPPING_BUTTON = (By.NAME, 'confirmDeliveryOption')
    CONFIRM_PAYMENT_BUTTON = (By.CSS_SELECTOR, 'div#payment-confirmation>div>button')
    PERSONAL_INFORMATION_ELEMENT = (By.CSS_SELECTOR, 'p.identity>a')
    ADDRESSES_SECTION_ELEMENT = (By.ID, 'delivery-addresses')
    ADDRESSES_SECTION_ADDRESS_FIELD = (By.ID, 'field-address1')
    ADDRESSES_SECTION_POST_CODE_FIELD = (By.ID, 'field-postcode')
    ADDRESSES_SECTION_CITY_FIELD = (By.ID, 'field-city')
    SHIPPING_SECTION_ELEMENT = (By.ID,'js-delivery')
    PAYMENT_SECTION_ELEMENT = (By.CSS_SELECTOR, '.payment-options')
    SET_PAYMENT_OPTION_RADIO_BUTTON = (By.ID, 'payment-option-2')
    MARK_CONDITIONS_CHECKBOX = (By.ID, 'conditions_to_approve[terms-and-conditions]')
    ORDER_CONFIRMATION_TEXT_ELEMENT = (By.CSS_SELECTOR, 'section#content-hook_order_confirmation h3')









































