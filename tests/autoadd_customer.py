import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "availliant"
       pwd = "B-town91"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/admin/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("http://127.0.0.1:8000/admin")
       assert "Logged In"
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/a").click()
       time.sleep(5)
       elem = driver.find_element_by_name("cust_name")
       elem.send_keys("Test Name")
       elem = driver.find_element_by_name("organization")
       elem.send_keys("This is just a test organization")
       elem = driver.find_element_by_name("role")
       elem.send_keys("This is a test role")
       elem = driver.find_element_by_name("email")
       elem.send_keys("test@unomaha.edu")
       elem = driver.find_element_by_name("bldgroom")
       elem.send_keys("This is a test room")
       elem = driver.find_element_by_name("address")
       elem.send_keys("This is a test address")
       elem = driver.find_element_by_name("account_number")
       elem.send_keys("11")
       elem = driver.find_element_by_name("city")
       elem.send_keys("Omaha")
       elem = driver.find_element_by_name("state")
       elem.send_keys("NE")
       elem = driver.find_element_by_name("zipcode")
       elem.send_keys("68137")
       elem = driver.find_element_by_name("phone_number")
       elem.send_keys("402-111-5555")
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
       time.sleep(5)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
