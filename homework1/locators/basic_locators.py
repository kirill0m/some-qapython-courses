from selenium.webdriver.common.by import By

NAVIGATION = {
    'campaigns': (By.XPATH, "//a[contains(@class, 'center-module-campaigns')]"),
    'audiences': (By.XPATH, "//a[contains(@class, 'center-module-segments')]"),
    'billing': (By.XPATH, "//a[contains(@class, 'center-module-billing')]"),
    'statistics': (By.XPATH, "//a[contains(@class, 'center-module-statistics')]"),
    'pro': (By.XPATH, "//a[contains(@class, 'center-module-pro')]"),
    'profile': (By.XPATH, "//a[contains(@class, 'center-module-profile')]"),
    'tools': (By.XPATH, "//a[contains(@class, 'center-module-tools')]"),
    'help': (By.XPATH, "//a[contains(@class, 'center-module-help')]")
}

QUERY_LOCATOR_LOGIN = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")
QUERY_LOCATOR_EMAIL = (By.NAME, 'email')
QUERY_LOCATOR_PASS = (By.NAME, 'password')
GO_BUTTON_AUTH = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")
QUERY_LOCATOR_RIGHT_MENU = (By.XPATH, "//div[contains(@class, 'right-module-userNameWrap')]")
GO_BUTTON_LOGOUT = (By.XPATH, "//a[contains(@href, 'logout')]")
QUERY_LOCATOR_FIO = (By.XPATH, "//div[contains(@data-name, 'fio')]/div/input")
QUERY_LOCATOR_PHONE_NUM = (By.XPATH, "//div[contains(@data-name, 'phone')]/div/input")
GO_BUTTON_SAVE = (By.XPATH, "//button[contains(@data-class-name, 'Submit')]")