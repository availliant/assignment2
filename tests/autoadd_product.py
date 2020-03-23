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
       driver.get("http://127.0.0.1:8000")
       assert "Logged In"
       time.sleep(5)
       elem = driver.find_element_by_link_text("Products").click()
       time.sleep(5)
       elem = driver.find_element_by_link_text("Add Product").click()
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[1]/div/select/option[4]").click()
       elem = driver.find_element_by_name("product")
       elem.send_keys("This is a test post with selenium")
       elem = driver.find_element_by_name("p_description")
       elem.send_keys("This is just a test description")
       elem = driver.find_element_by_name("quantity")
       elem.send_keys("2")
       elem = driver.find_element_by_name("charge")
       elem.send_keys("11")
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
       time.sleep(5)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
