import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):  # TEST SCENARIO

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(executable_path='C:\Sanbercode-QA-Final_Project\Shidqi-Adiatma\chromedriver.exe')

    # Success login with valid Email and Password
    def test_01_success_login(self):
        # steps
        browser = self.browser  #buka web browser
        browser.get("https://www.harisenin.com/") #mengakses website
        time.sleep(3) 
        browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/nav/div/div[2]/button').click() #klik tombol masuk
        time.sleep(1) 
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[1]/input').send_keys("shidqi1.upscale@gmail.com") #isi email 
        time.sleep(1) 
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[2]/div/input').send_keys("JagoQuality123") #isi passsword
        time.sleep(1) 
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/button').click() #klik tombol login
        time.sleep(3) 
        
    # Failed login with invalid Email and Password
    def test_02_failed_login_with_invalid_email_password(self):
        # steps
        browser = self.browser  #buka web browser
        browser.get("https://www.harisenin.com/") #mengakses website
        time.sleep(3) 
        browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/nav/div/div[2]/button').click() #klik tombol masuk
        time.sleep(1) 
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[1]/input').send_keys("shidqi1.gmail.com") #isi email 
        time.sleep(1) 
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[2]/div/input').send_keys("quality123") #isi passsword
        time.sleep(1) 
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/button').click() #klik tombol login
        time.sleep(3) 
        
         # validation
        response_message = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[1]/small").text

        # Cannot login
        self.assertIn('Email tidak valid', response_message)
    
    # Failed login with not registered Email and Password
    def test_03_failed_login_with_notregistered_email_password(self):
        browser = self.browser  #buka web browser
        browser.get("https://www.harisenin.com/") #mengakses website
        time.sleep(3) 
        browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/nav/div/div[2]/button').click() #klik tombol masuk
        time.sleep(1) 
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[1]/input').send_keys("shidqi2.upscale@gmail.com") #isi email 
        time.sleep(1) 
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[2]/div/input').send_keys("JagoQuality123") #isi passsword
        time.sleep(1) 
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/button').click() #klik tombol login
        time.sleep(3) 
        
         # validation
        response_message = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div[2]/div[2]/div[2]").text

        # Cannot login
        self.assertIn('Email belum terdaftar', response_message)
        
    # Failed login with valid Email and wrong Password
    def test_04_failed_login_with_valid_email_wrong_password(self):
        browser = self.browser  #buka web browser
        browser.get("https://www.harisenin.com/") #mengakses website
        time.sleep(3) 
        browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/nav/div/div[2]/button').click() #klik tombol masuk
        time.sleep(1) 
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[1]/input').send_keys("shidqi1.upscale@gmail.com") #isi email 
        time.sleep(1) 
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[2]/div/input').send_keys("JagoKualitas123") #isi passsword
        time.sleep(1) 
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/button').click() #klik tombol login
        time.sleep(3) 
        
         # validation
        response_message = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div[2]/div[2]/div[2]").text

        # Cannot login
        self.assertIn('Password yang kamu masukkan salah', response_message)
    
     # Failed login with valid Email and empty Password
    def test_05_failed_login_with_valid_email_empty_password(self):
        browser = self.browser  #buka web browser
        browser.get("https://www.harisenin.com/") #mengakses website
        time.sleep(3) 
        browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/nav/div/div[2]/button').click() #klik tombol masuk
        time.sleep(1) 
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[1]/input').send_keys("shidqi1.upscale@gmail.com") #isi email 
        time.sleep(1) 
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[2]/div/input').send_keys("") #isi passsword
        time.sleep(1) 
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/button').click() #klik tombol login
        time.sleep(3) 
        
         # validation
        response_message = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[2]/small").text

        # Cannot login
        self.assertIn('Password harus diisi', response_message)
    
    # Failed login with empty Email and Password
    def test_06_failed_login_with_empty_email_password(self):
        browser = self.browser  #buka web browser
        browser.get("https://www.harisenin.com/") #mengakses website
        time.sleep(3) 
        browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/nav/div/div[2]/button').click() #klik tombol masuk
        time.sleep(1) 
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[1]/input').send_keys("") #isi email 
        time.sleep(1) 
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[2]/div/input').send_keys("JagoQuality123") #isi passsword
        time.sleep(1) 
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/button').click() #klik tombol login
        time.sleep(3) 
        
         # validation
        response_message = browser.find_element(By.XPATH, " /html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[1]/small").text

        # Cannot login
        self.assertIn('Email harus diisi', response_message)
    
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()