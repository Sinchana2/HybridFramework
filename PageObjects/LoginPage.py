
class LoginPage:
    # Login Page
    SignIn = "//div[text()='Sign In']"
    create_account = "//a[text()='Create a New Account']"
    name_by_id ="//input[@id='ap_customer_name']"
    email_by_id = "//input[@id='ap_email']"
    password_by_id = "//input[@id='ap_password']"
    reenter_password_by_id = "//input[@id='ap_password_check']"
    create_account_butn = "//input[@class='a-button-input']"



    def __init__(self,driver):
        self.driver=driver

    def signIn(self, username, emailid, password):
        self.driver.find_element_by_xpath(self.SignIn).click()
        self.driver.find_element_by_xpath(self.create_account).click()
        self.driver.find_element_by_xpath(self.name_by_id).send_keys(username)
        self.driver.find_element_by_xpath(self.email_by_id).send_keys(emailid)
        self.driver.find_element_by_xpath(self.password_by_id).send_keys(password)
        self.driver.find_element_by_xpath(self.reenter_password_by_id).send_keys(password)
        self.driver.find_element_by_xpath(self.create_account_butn).click()

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()