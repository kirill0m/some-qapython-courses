from selenium.webdriver.common.by import By

def nav_sample(path):
    return (By.XPATH, f"//a[contains(@class, 'center-module-{path}')]")

def pages_identifiers(page):
    if page == 'billing':
        return (By.XPATH, "//li[contains(@data-type, 'deposit')]")
    elif page == 'statistics':
        return (By.XPATH, "//div[contains(@class, 'ads-summary-statistics')]")

QUERY_LOCATOR_LOGIN = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")
QUERY_LOCATOR_EMAIL = (By.NAME, 'email')
QUERY_LOCATOR_PASS = (By.NAME, 'password')
GO_BUTTON_AUTH = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")
QUERY_LOCATOR_RIGHT_MENU = (By.XPATH, "//div[contains(@class, 'right-module-userNameWrap')]")
GO_BUTTON_LOGOUT = (By.XPATH, "//a[contains(@href, 'logout')]")
QUERY_LOCATOR_FIO = (By.XPATH, "//div[contains(@data-name, 'fio')]/div/input")
QUERY_LOCATOR_PHONE_NUM = (By.XPATH, "//div[contains(@data-name, 'phone')]/div/input")
GO_BUTTON_SAVE = (By.XPATH, "//button[contains(@data-class-name, 'Submit')]")
QUERY_LOCATOR_PAGECONTENT = (By.XPATH, "//div[contains(@class, 'layout-module-pageContentWrap')]")