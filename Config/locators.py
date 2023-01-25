
class Locators():
    add_user_btn = '//button[@class="btn btn-link pull-right"]'
    first_name_input = '//input[@name="FirstName"]'
    last_name_input = '//input[@name="LastName"]'
    user_name_input = '//input[@name="UserName"]'
    password_input = '//input[@name="Password"]'
    company_aaa_radio_btn = '//label[text()="Company AAA"]/input'
    company_bbb_radio_btn = '//label[text()="Company BBB"]/input'
    role_select = '//select[@name="RoleId"]'
    sales_team_select_option = '//select[@name="RoleId"]/option[@value="0"]'
    email_input = '//input[@name="Email"]'
    phone_input = '//input[@name="Mobilephone"]'
    save_btn = '//button[@class="btn btn-success"]'
    delete_confirmation_btn = '//button[contains(text(), "OK")]'
    delete_user_btn = '//tbody/tr/td[text()="ReplaceMe"]/parent::tr/td/button[@ng-click="delUser()"]'
    table_cell = '//tbody/tr/td[text()="ReplaceMe"]'
    