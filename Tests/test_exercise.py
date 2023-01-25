from Pages.way2automationpage import Way2AutomationPage
from Utilities.handlers import DatasetHandlers
import time, json, pytest

#deserialize supporting file-like object containing a JSON document to a Python object
with open("C:\\Users\\Felicitas Peredo\\Documents\\felicitas_peredo_teladoc_challenge\\Config\\dataset.json") as jsonFile:
    file = json.load(jsonFile)

class TestCases():
    #parametrize the test with possible new users data, in this case only one
    @pytest.mark.parametrize("dataset", DatasetHandlers.test_handler(file))
    def test_add_user(self, init_driver, dataset):
        driver = init_driver
        # initialize Way2AutomationPage class instance
        way2automation_page = Way2AutomationPage(driver)
        #add new user
        way2automation_page.add_new_user(dataset['new_user'])
        #validate the new user is added to the table
        added = way2automation_page.validate_new_user_added(dataset['new_user'])
        assert added

    @pytest.mark.parametrize("user", [('novak')])
    def test_delete_user(self, init_driver, user):
        driver = init_driver
        # initialize Way2AutomationPage class instance
        way2automation_page = Way2AutomationPage(driver)
        #delete a user
        way2automation_page.delete_user(user)
        #validate the user was deleted from the table
        deleted = way2automation_page.validate_deleted_user(user)
        assert deleted
        