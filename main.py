from selenium import webdriver
import pyautogui as py
# driver = webdriver.Chrome()
# driver = webdriver.Chrome("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://web.telegram.org/#/im")


driver.maximize_window()
msg = input("Enter the message:lhklj ")

x=2
while(x<=11):
    link = driver.find_element_by_xpath("//*[@id='ng-app']/body/div[5]/div[2]/div/div/div[3]/div[2]/div[2]/div/div["+str(x)+"]/div[1]/a")
    link.click()
    link = driver.find_element_by_xpath("//*[@id='ng-app']/body/div[6]/div[2]/div/div/div[2]/div/a/i")
    link.click()
    py.moveTo(990,887)
    py.click()
    py.write(msg)
    py.keyDown('enter')
    link = driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/ul/li[1]/a/div[3]/div[1]/span")
    link.click()
    link = driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[1]/div/div/div[2]/div/div[2]/a/div/span[1]")
    link.click()
    x=x+1


print("Success")    

