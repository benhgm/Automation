"""
Python script to scrape a webpage for form details

Reference code from:
https://www.thepythoncode.com/article/extracting-and-submitting-web-page-forms-in-python
"""

from selenium import webdriver

chromedriver_location = "/opt/homebrew/bin/chromedriver"

driver = webdriver.Chrome(chromedriver_location)
driver.get("https://form.gov.sg/#!/5ebe170b5b2a1c0011a3a2c0")

nric_field = "/html/body/section/section/div/submit-form-directive/div[1]/div/div/form/div[1]/field-directive/div/nric-field-component/div/div[1]/input"

driver.find_element_by_xpath(nric_field).send_keys("S9310687C")

