from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
Servi_obj = Service(r"C:\drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=Servi_obj)
driver.get("https://www.amazon.in/")
driver.maximize_window()

# Login Function
def login(email, password):
    driver.find_element(By.XPATH, "//*[@id='nav-link-accountList']/a/span").click()
    driver.find_element(By.ID,"ap_email_login").send_keys("sudama89840@gmail.com")
    driver.find_element(By.XPATH,"//*[@id='continue']/span/input").click()
    driver.find_element(By.ID,"ap_password").send_keys("shiva3690")

#Login  valid ID & Password
def test_login_valid():
    login("sudama89840@gmail.com", "shiva3690")
    if 'shiva' in driver.page_source:
        print("Test Pass 01: Valid login successful")
    else:
        print('Test Fail 01: Valid login failed')

#Login with invalid password
def test_login_invalid():
    login("sudama89840@gmail.com", "shiva369")
    if "password is incorrect" in driver.page_source:
        print('Test Pass 02: Error message displayed  wrong password"') #if you put wrong password
    else:
        print("Test Fail 02: Wrong password")


#serch Products
def test_serch_products():
    driver.get("https://www.amazon.in/")
    search_box = driver.find_element(By.ID,"twotabsearchtextbox")
    search_box.send_keys('latop')
    search_box.send_keys(Keys.RETURN)
    if 'laptop' in driver.page_source:
        print("Test pass 03: Search results displayed")
    else:
        print("Test Fail 03: Search results not displayed")

#Apply price filter
def test_price_filter():
    driver.get("https://www.amazon.in/s?k=laptops")
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "//span[contains(text(),'₹1,500 - ₹3,400')]").click()
        time.sleep(2)
        print("Test Pass 04: Price filter applied")
    except:
        print("Test Fail 04: Price filter not applied")

# Add item to cart
def test_add_to_cart():
    driver.get("https://www.amazon.in/s?k=laptops")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='a-autoid-1-announce']").click()
    time.sleep(2)
    if "Added to Cart" in driver.page_source:
        print("Test Pass 05: Item added to cart")
    else:
        print("Test Fail 05: Item not added to cart")

# Remove item from cart
def test_remove_from_cart():
    driver.get("https://www.amazon.in/s?k=laptops")
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "//span[@class='a-icon a-icon-small-trash']").click()
        time.sleep(2)
        print("Test Pass 06: Item removed from cart")
    except:
        print("Test Fail 06: No item to remove from cart")

#Place COD order (Simulated - not completing payment)
def test_place_cod():
    print("Test information 07: COD order placement test  (requires UPI account & payment)")

#  Place UPI order
def test_place_upi():
    print("Test Information 08: UPI payment test ")

# Track order
def test_track_order():
    driver.get("https://www.amazon.in/gp/your-account/order-history")
    if "Your Orders" in driver.page_source:
        print("Test pass 09: Order history page loaded")
    else:
        print("Test Fail 09: Order history not loaded")

#Cancel order
def test_cancel_order():
    print("Test information 10: your order is cancel")

