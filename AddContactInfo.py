import pandas as pd
import datetime

#Start by getting today's date
today = datetime.date.today().strftime('%m/%d/%Y')
temp = pd.Timestamp(today)
day_of_week = (temp.day_name())
print(day_of_week)
import sys
if day_of_week == 'Sunday':
    sys.exit()


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
prefs = {"profile.default_content_settings.popups": 0,
             "download.default_directory":
                        r"C:\Users\thegi\PycharmProjects\viasat_end_day_reports\\",
             "directory_upgrade": True}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(executable_path=r'C:\Users\thegi\PycharmProjects\viasat_end_day_reports\chromedriver.exe', options = options)

start_date = today

end_date = today

import time

driver.maximize_window()
driver.get("https://fulfillment.wildblue.net")
time.sleep(5)

#x = input("user name")
#y = input("password")

#ADD FFL USERNAME AND PASSWORD BELOW
elem = driver.find_element_by_name('j_username')
elem.send_keys("")
elem = driver.find_element_by_name('j_password')
elem.send_keys("")
elem = driver.find_element_by_name('submit')
elem.click()

#Go to Schedule Date
driver.get("https://fulfillment.wildblue.net/fsm-fe/fsm/browseOrder/browseOrder.page?execution=e3s1")

try:
    elem = driver.find_element_by_id("browseOrder:orderGrid:filterBoard:createdDateFilter:j_idt172") or driver.find_element_by_id("browseOrder:orderGrid:filterBoard:createdDateFilter:j_idt172")
    elem.click()
except NoSuchElementException:
    elem = driver.find_element_by_id("browseOrder:orderGrid:filterBoard:createdDateFilter:j_idt189")
    elem.click()


elem = driver.find_element_by_id("browseOrder:orderGrid:filterBoard:scheduledDateFilter:dateFromCal_input")
elem.click()
elem.send_keys(start_date)
elem.send_keys(Keys.TAB)
elem = driver.find_element_by_id("browseOrder:orderGrid:filterBoard:scheduledDateFilter:dateToCal_input")
elem.click()
elem.send_keys(end_date)
elem = driver.find_element_by_id('browseOrder:orderGrid:search')
elem.click()
time.sleep(17)
number_of_jobs = driver.find_element_by_xpath("//span[@class = 'ui-paginator-current']")
number_of_jobs = number_of_jobs.text
number_of_jobs = number_of_jobs.split("result:")[1]
print(number_of_jobs)
number_of_jobs = int(number_of_jobs)
x = 0
while number_of_jobs > 0:
    tech = driver.find_element_by_id(f"browseOrder:orderGrid:gridTable:{x}:orderGrid_technician:body")
    tech_1 = (tech.text)
    if tech_1 == 'Cross James':
        phone = '336-947-3509'
    elif tech_1 == 'Jordan Johnny':
        phone = '336-259-3888'
    elif tech_1 == 'Lewis David':
        phone = '910-434-5882'
    elif tech_1 == 'Crabtree Jim':
        phone = '336-328-7985'
    else:
        phone = '336-848-4077'
    elem = driver.find_element_by_id(f'browseOrder:orderGrid:gridTable:{x}:orderLink')
    elem.click()
    time.sleep(5)
    try:
        elem = driver.find_element_by_xpath('// *[ @ id = "noteForm:j_idt1571:noteInputarea"]')
        elem.click()
    except NoSuchElementException:
        elem = driver.find_element_by_xpath('// *[ @ id = "noteForm:j_idt1621:noteInputarea"]')
        elem.click()
    elem.send_keys(f"Best contact number for customer to reach the company/tech if needed is {phone}")
    try:
        elem = driver.find_element_by_xpath('//*[@id="noteForm:j_idt1571:j_idt1577"]/span')
        elem.click()
    except:
        elem = driver.find_element_by_xpath('//*[@id="noteForm:j_idt1621:j_idt1627"]/span')
        elem.click()

    time.sleep(3)
    driver.get("https://fulfillment.wildblue.net/fsm-fe/fsm/browseOrder/browseOrder.page?execution=e3s1")
    time.sleep(5)
    elem = driver.find_element_by_id('browseOrder:orderGrid:search')
    elem.click()
    time.sleep(7)
    x = x + 1
    number_of_jobs = number_of_jobs - 1
