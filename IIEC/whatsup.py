import selenium
from selenium import webdriver	  
import time 
from selenium.webdriver.common.keys import Keys  
#enter perfect name as in your contact (it is case sensitive) 
name=input("to whom you want to send message?") 
#replace /chromedriver with loaction of chromedriver on your computer  
browser = webdriver.Chrome("C:\\Users\\dchanna\\Documents\\Learning\\Python\\IIEC\\chromedriver.exe") 
browser.get('https://web.whatsapp.com')  
time.sleep(10)  
elem = browser.find_element_by_xpath("//input[@title='Search or start new chat']") 
elem.click()  
elem.send_keys(name) 
time.sleep(10) 
browser.find_element_by_xpath("//*[@title='"+name+"']").click(); 
time.sleep(5) 
elem = browser.find_element_by_xpath("//div[@data-tab='1']") 
elem.click() 
for i in range(20):  
 elem.send_keys("hello this is from python " + Keys.ENTER)  
 time.sleep(1) 