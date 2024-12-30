import time
from postApiCall import apiCall
from selenium import webdriver
from selenium.webdriver.common.by import By

productName = 'wicp'

driver = webdriver.Chrome()
driver.get('https://10.0.6.46:8443/pcc/welcome/jsp/login.jsp')
time.sleep(3)
try:
	element0 = driver.find_element(By.ID, r'''details-button''')
	element0.click()
	print('Execution : click on advanced button')
except Exception as element0Error:
	print('Received an exception : ', element0Error)
	result = 'FAIL'
	captureResponse = apiCall('loginCred.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element1 = driver.find_element(By.ID, r'''proceed-link''')
	element1.click()
	print('Execution : click on proceed unsafe')
except Exception as element1Error:
	print('Received an exception : ', element1Error)
	result = 'FAIL'
	captureResponse = apiCall('loginCred.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element2 = driver.find_element(By.ID, r'''username''')
	element2.send_keys('admin')
	print('Execution : send username')
except Exception as element2Error:
	print('Received an exception : ', element2Error)
	result = 'FAIL'
	captureResponse = apiCall('loginCred.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element3 = driver.find_element(By.NAME, r'''password''')
	element3.send_keys('Tayana25')
	print('Execution : send password')
except Exception as element3Error:
	print('Received an exception : ', element3Error)
	result = 'FAIL'
	captureResponse = apiCall('loginCred.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element4 = driver.find_element(By.XPATH, r'''//*[@id='passdiv']/div/input''')
	element4.click()
	print('Execution : click on submit button')
except Exception as element4Error:
	print('Received an exception : ', element4Error)
	result = 'FAIL'
	captureResponse = apiCall('loginCred.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(10)

result = 'PASS'
captureResponse = apiCall('loginCred.py', productName, result)
print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
driver.quit()
quit()