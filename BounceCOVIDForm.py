from selenium import webdriver
import keyboard, time
##Within the parenthesis should be the file path to the chromedriver.exe
chromedriver_location = "(Location of ChromeDriver Path)"
driver = webdriver.Chrome(chromedriver_location)
##Within the parenthesis should be a link of your choice that chromedriver will load into
driver.get('(Link)')
FirstName = '//*[@id="first_3"]'
LastName = '//*[@id="last_3"]'
Email = '//*[@id="input_4"]'
AreaCode = '//*[@id="input_5_area"]'
Number = '//*[@id="input_5_phone"]'
DOB = '//*[@id="lite_mode_35"]'
NextButton = '//*[@id="form-pagebreak-next_6"]'
Q1 = '//*[@id="input_36_1"]'
Q2 = '//*[@id="input_37_1"]'
Q3 = '//*[@id="input_40_11"]'
Q4 = '//*[@id="input_41_0"]'
SubmitButton = '//*[@id="input_33"]'
driver.find_element_by_xpath(FirstName).send_keys("Johnny")
time.sleep(0.0001)
driver.find_element_by_xpath(LastName).send_keys("Appleseed")
time.sleep(0.0001)
driver.find_element_by_xpath(Email).send_keys("johhnyappleseed@gmail.com")
time.sleep(0.0001)
driver.find_element_by_xpath(AreaCode).send_keys("721")
time.sleep(0.0001)
driver.find_element_by_xpath(Number).send_keys("987-2817")
time.sleep(0.0001)
driver.find_element_by_xpath(DOB).send_keys("07-14-1992")
time.sleep(0.01)
driver.find_element_by_xpath(NextButton).click();
driver.find_element_by_xpath(NextButton).click();
time.sleep(0.1)
driver.find_element_by_xpath(Q1).click();
time.sleep(0.0001)
driver.find_element_by_xpath(Q2).click();
time.sleep(0.0001)
driver.find_element_by_xpath(Q3).click();
time.sleep(0.0001)
driver.find_element_by_xpath(Q4).click();
time.sleep(0.0001)
driver.find_element_by_xpath(SubmitButton).click()
driver.find_element_by_xpath(SubmitButton).click()
time.sleep(0.0001)
driver.close()
time.sleep(0.0001)
driver.quit()




