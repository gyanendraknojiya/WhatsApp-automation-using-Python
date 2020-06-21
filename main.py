from selenium  import webdriver
from selenium.webdriver.common.keys import Keys
import time 



options = webdriver.ChromeOptions()  
options.add_argument("--user-data-dir=C:/Users/Spider/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(executable_path='./chromedriver',options=options)

mobileNumber = str(input('Enter a whatsapp number without country code:  '))
message = str(input('Enter your Message:  '))
messagesCount = int(input('How many times do you want to send messages:  '))
# driver.maximize_window()
driver.get('https://web.whatsapp.com/send?phone=91'+ mobileNumber +'&amp;text&amp;source&amp;data&amp;app_absent')
time.sleep(10)

count =  0
while count <messagesCount:
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys(message)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    count +=1 
    print(count)

   

