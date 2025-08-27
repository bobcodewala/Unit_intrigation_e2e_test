import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestWebCalculator(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Requires chromedriver installed
        self.driver.get("http://example.com/calculator")  # Replace with your app URL

    def test_addition(self):
        driver = self.driver
        driver.find_element(By.ID, "num1").send_keys("10")
        driver.find_element(By.ID, "num2").send_keys("20")
        driver.find_element(By.ID, "addBtn").click()
        result = driver.find_element(By.ID, "result").text
        self.assertEqual(result, "30")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
