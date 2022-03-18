from selenium.webdriver.common import action_chains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select

class Home:
    # Home Page

    menu = "//div[text()='Menu']"
    top_250 = "//span[text()='Top 250 Movies']"
    dropdown = "//select[@id='lister-sort-by-options']"

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        title = self.driver.title
        return title

    def click_on_menu(self):
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH,self.menu))
        self.driver.find_element_by_xpath(self.menu).click()

    def click_on_sub_menu(self):
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, self.top_250))
        self.driver.find_element_by_xpath(self.top_250).click()

    def select_release_date(self, value):
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, self.dropdown))

        s = select.Select(self.driver.find_element_by_xpath(self.dropdown))
        s.select_by_visible_text(value)
