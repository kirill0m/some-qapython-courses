from ui.locators.basic_locators import SegmentsLocators
from ui.pages.base_page import BasePage
 

class SegmentsPage(BasePage):
    locators = SegmentsLocators

    def __init__(self, driver):
        self.driver = driver

    def create_segment(self, segment_name):
        create_segment_btn = self.find(self.locators.LOCATOR_CREATE_SEGMENT)
        if create_segment_btn.is_displayed():
            self.click(self.locators.LOCATOR_CREATE_SEGMENT)
        else:
            self.click(self.locators.LOCATOR_CREATE_FIRST_SEGMENT)

        self.click(self.locators.LOCATOR_SEGMENT_CHECKBOX)
        self.click(self.locators.LOCATOR_ADD_SEGMENT_BUTTON)

        self.fill_out(self.locators.LOCATOR_SEGMENT_NAME_INPUT, segment_name)
            
        self.click(self.locators.LOCATOR_CONFIRM_SEGMENT_CREATION)

    def check_if_segment_is_created(self, segment_name):
        return True if self.find(self.locators.name_cell_segment(segment_name)) else False
    
    def delete_segment_by_name(self, name):
        name_cell = self.find(self.locators.name_cell_segment(name))
        segment_id = name_cell.get_attribute('href').split('/')[-1]
        self.click(self.locators.removal_button_by_id(segment_id))
        self.click(self.locators.LOCATOR_CONFIRM_SEGMENT_REMOVAL)
        try:
            while self.find(self.locators.LOCATOR_OVERLAY, timeout=5).is_displayed():
                continue
        except:
            pass