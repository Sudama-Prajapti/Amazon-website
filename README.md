# Amazon Website Automation Testing (Python + Selenium)

## 📌 Project Overview
This project automates the testing of **Amazon.in** website functionalities using **Selenium WebDriver (Python)**.  
The main goal is to verify critical user journeys such as **Login, Product Search, Add to Cart, Order Simulation, and Tracking Orders**.

---

## 🛠 Tools & Technologies
- **Language**: Python  
- **Framework**: Selenium WebDriver  
- **Browser**: Google Chrome (chromedriver.exe required)  
- **OS**: Windows  

---

## 🚀 Features Tested
1. **Login Functionality**
   - ✅ Valid login with correct email & password  
   - ❌ Invalid login with wrong password  

2. **Search & Filter Products**
   - Search for products (Laptop)  
   - Apply price filter  

3. **Cart Operations**
   - Add items to cart  
   - Remove items from cart  

4. **Order Operations (Simulated)**
   - Place COD order (simulation)  
   - Place UPI order (simulation)  

5. **Order Management**
   - Track Orders  
   - Cancel Order (simulation)  



**Sample Test Cases & Results**
Test Case ID	Description	Expected Result
TC_01	Valid Login	Login successful
TC_02	Invalid Login (Wrong Password)	Error message shown
TC_03	Search Product "Laptop"	Search results displayed
TC_04	Apply Price Filter	Filter applied
TC_05	Add Item to Cart	Item successfully added
TC_06	Remove Item from Cart	Item successfully removed
TC_07	Place COD Order (Simulated)	COD option available
TC_08	Place UPI Order (Simulated)	UPI option available
TC_09	Track Orders	Order history displayed
TC_10	Cancel Order (Simulated)	Order cancelled

👨‍💻 Author

Sudama Prajapati
Automation Tester | Python | Selenium
