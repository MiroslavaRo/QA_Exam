"""add/remove elements"""
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestAddRemoveElements(unittest.TestCase):

    """add_remove_elem
    http://the-internet.herokuapp.com/add_remove_elements/"""
    def setUp(self):
        serv = Service ("D:/ПРОГРАММЫ/chromedriver_win32/chromedriver.exe")
        self.driver = webdriver.Chrome(service = serv)
        self.base_url = "http://the-internet.herokuapp.com/add_remove_elements/"
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(self.base_url)
        time.sleep(2)
        self.assertIn(self.base_url, self.driver.current_url)

    def test_add_remove_elem(self):
        "test_add_remove_elem"
        driver = self.driver
        elem = self.driver.find_element(By.CSS_SELECTOR, "#content > div > button")
        self.assertTrue(elem)
        for _ in range(5):
            time.sleep(1)
            elem.click()
        driver.save_screenshot("C:/Users/asus/source/repos/QA_Exam/AddRemoveElem/add_elem.png")
        selec = self.driver.find_element(By.CSS_SELECTOR,'#elements')
        length = len(selec.find_elements_by_class_name('added-manually'))
        i = length
        while i>2:
            selec.find_elements_by_class_name('added-manually')[0].click()
            time.sleep(1)
            i-=1
        driver.save_screenshot('C:/Users/asus/source/repos/QA_Exam/AddRemoveElem/remove_elem.png')

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == '__main__':
    unittest.main(
    )
