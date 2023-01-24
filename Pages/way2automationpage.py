from Pages.basepage import BasePage
from Config.locators import Locators
from selenium.common.exceptions import NoSuchElementException

class Way2AutomationPage(BasePage):

    #initializer
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.way2automation.com/angularjs-protractor/webtables/')

    def add_new_user(self, dataset):
        try:
            #click the add user button
            self.do_click(Locators.add_user_btn)
            #populate the following fields
            self.do_send_keys(Locators.first_name_input, dataset['First Name'])
            self.do_send_keys(Locators.last_name_input, dataset['Last Name'])
            self.do_send_keys(Locators.user_name_input, dataset['User Name'])
            self.do_send_keys(Locators.password_input, dataset['Password'])
            # self.do_click(Locators.company_aaa_radio_btn)
            self.do_dropdown_single_select(Locators.role_select, Locators.sales_team_select_option)
            self.do_send_keys(Locators.email_input, dataset['E-mail'])
            self.do_send_keys(Locators.phone_input, dataset['Cell Phone'])
            #click the save new user button
            self.do_click(Locators.save_btn)
        except:
            raise Exception

    def validate_new_user_added(self, dataset):
        try:
            del dataset['Password']
            #initialize an empty dictionary to store the data from the page
            page_dict = {}
            for i in range(1,8):
                #get the column names in the specified position
                column = self.get_attribute(f'(//tr/th[not(contains(@class, "ng-hide"))])[{i}]', 'textContent')
                #once the text matches the users first name, get the value for the corresponding position
                value = self.get_attribute(f"(//tbody/tr/td[text()='{dataset['First Name']}']/parent::tr/td[not(contains(@class, 'ng-hide'))])[{i}]", 'textContent')
                #update the dictionary with the columns as keys and the values as values
                page_dict.update({column: value})
            #compare actual results with expected results
            return dataset == page_dict
        except:
            raise Exception

    def delete_user(self, user):
        try:
            #click the delete button
            self.do_click(Locators.delete_user_btn.replace('ReplaceMe', user))
            #click the confirmation button to delete a user
            self.do_click(Locators.delete_confirmation_btn)
        except:
            raise Exception

    def validate_deleted_user(self, user):
        try:
            #try to find the user, if not return true
            self.find_element(Locators.table_cell.replace('ReplaceMe', user))
            return False
        except NoSuchElementException:
            return True
        



