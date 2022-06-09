import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        time.sleep(5)
    def test_loginFunctionality(self):

        self.driver.get("https://www.netflix.com/bd/")
        self.driver.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div/div/div/div/div[1]/div/a').click()
        time.sleep(3)
        self.driver.find_element(By.NAME, "userLoginId").send_keys("4rough07@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.ID, "id_password").send_keys("wq12!@")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()
        time.sleep(3)

        print("================================")
        print(self.driver.title)
        print("test successfull")
        print("================================")

    def test_loginFunctionality_01(self):
        self.driver.get("https://www.netflix.com/bd/")
        self.driver.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div/div/div/div/div[1]/div/a').click()
        time.sleep(3)
        self.driver.find_element(By.NAME, "userLoginId").send_keys("rezviahmed07@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.ID, "id_password").send_keys("wq12!@")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()
        time.sleep(3)

        print("================================")
        print(self.driver.title)
        print("test successfull")
        print("================================")

        # self.assertEqual(True, False)  # add assertion here

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/user/PycharmProjects/pythonProject1/NETFLIXauto_utest/report'))
