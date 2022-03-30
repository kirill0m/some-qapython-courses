from selenium.webdriver.common.by import By

class BasePageLocators:
    QUERY_LOCATOR_RIGHT_MENU = (By.XPATH, "//div[contains(@class, 'right-module-userNameWrap')]")
    GO_BUTTON_LOGOUT = (By.XPATH, "//a[contains(@href, 'logout')]")


class LoginPageLocators:
    LOCATOR_LOGIN = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")
    LOCATOR_EMAIL = (By.NAME, 'email')
    LOCATOR_PASS = (By.NAME, 'password')
    GO_BUTTON_AUTH = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")
    GO_BUTTON_AUTH_DISABLED = (By.XPATH, "//div[contains(@class, 'authForm-module-disabled')]")
    LOCATOR_LOGIN_ERROR = (By.XPATH, "//div[contains(@class, 'notify-module-notifyBlock')]")


class MainPageLocators():
    def nav_sample(path):
        return (By.XPATH, f"//a[contains(@class, 'center-module-{path}')]")


class CampaignLocators:
    LOCATOR_CREATE_CAMPAIGN = (By.XPATH, "//div[contains(@class, 'dashboard-module-createButtonWrap')]")
    LOCATOR_CAMPAIGN_URL = (By.XPATH, "//input[contains(@class, 'mainUrl-module-searchInput')]")
    LOCATOR_UPLOAD_BANNER = (By.XPATH, "//div[contains(@class, 'image240x400-module-wrapper')]/div/input")
    LOCATOR_SUBMIT_BANNER_CREATION = (By.XPATH, "//div[contains(@data-test, 'submit_banner_button')]")
    LOCATOR_SUBMIT_CAMPAIGN_CREATION = (By.XPATH, "//div[contains(@class, 'js-save-button-wrap')]/button")
    LOCATOR_MAIN_TABLE = (By.XPATH,  "//div[contains(@class, 'dashboard-module-table')]")
    LOCATOR_CREATION_NOTIFY = (By.XPATH, "//div[contains(@class, 'notify-module-succes')]")

    def campaign_creation(path):
        return (By.XPATH, f"//div[contains(@class, 'column-list-item _{path}')]")

    def advt_patterns(path):
        return (By.XPATH, f"//div[contains(@id, 'patterns_{path}')]")


class SegmentsLocators():
    LOCATOR_CREATE_SEGMENT = (By.XPATH, "//div[contains(@class, 'js-create-button-wrap')]/button")
    LOCATOR_SEGMENT_CHECKBOX = (By.XPATH, "//input[contains(@class, 'adding-segments-source__checkbox')]")
    LOCATOR_ADD_SEGMENT_BUTTON = (By.XPATH, "//div[contains(@class, 'js-add-button')]/button")
    LOCATOR_SEGMENT_NAME_INPUT = (By.XPATH, "//div[contains(@class, 'input_create-segment-form')]/div/input")
    LOCATOR_CONFIRM_SEGMENT_CREATION = (By.XPATH, "//div[contains(@class, 'js-create-segment-button-wrap')]/button")
    LOCATOR_CONFIRM_SEGMENT_REMOVAL = (By.XPATH, "//button[contains(@class, 'button_confirm-remove')]")

    LOCATOR_OVERLAY = (By.XPATH, "//div[contains(@class, 'js-modal-overlay')]")

    def name_cell_segment(name):
        return (By.XPATH, f"//a[contains(@title, '{name}')]")

    def removal_button_by_id(id):
        return (By.XPATH, f"//div[contains(@data-test, 'remove-{id}')]/span")