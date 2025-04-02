availSingleElementsDict = {'id': 'ID', 'name': 'NAME', 'xpath': 'XPATH', 'linktext': 'LINK_TEXT', 'tagname': 'TAG_NAME', 'classname': 'CLASS_NAME', 'cssselector': 'CSS_SELECTOR', 'q': 'quit()', 'containstext': 'XPATH'}
availOperationDict = {'click': 'click', 'input': 'send_keys', 'drag-drop' : 'drag_and_drop', 'clear':'clear', 'right-click' : 'perform', 'scroll' : 'move_to_element'}

def writeProdUrl(fileName, getProductName, urlGet):
    f = open(fileName, "a")
    try:
        f.write("import time\n")
        f.write("import json\n")
        f.write("import requests\n")
        # f.write("from postApiCall import apiCall\n")
        f.write("from selenium import webdriver\n")
        f.write(f"from selenium.webdriver.common.action_chains import ActionChains\n")
        f.write(f"from selenium.webdriver.support.ui import WebDriverWait\n")
        f.write(f"from selenium.webdriver.support import expected_conditions as EC\n")
        f.write("from selenium.webdriver.common.by import By\n\n")
        f.write(f"testRunId = int(time.time())\n")
        f.write(f"executionTime = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())\n\n")
        #Below is writing the function itself
        f.write(f"def apiCall(testCaseName, product, result):\n")
        f.write(f"\ttestCaseName = testCaseName.replace('.py', '')\n")
        f.write("\theaders = {'content-type': 'application/json'}\n")
        f.write(f"\turl = 'http://10.0.1.127:8081/post_test'\n")
        f.write('\tdata = {"TEST_RUN_ID": testRunId, "TEST_CASE_NAME": testCaseName, "PRODUCT": product, "EXECUTION_TIME": executionTime, "RESULT": result}\n')
        f.write(f"\tresponse = requests.post(url, data=json.dumps(data), headers=headers)\n")
        f.write(f"\treturn response, testRunId\n\n")
        f.write(f"productName = '{getProductName}'\n\n")
        f.write(f"")
        f.write("driver = webdriver.Chrome()\n")
        f.write(f"driver.get('{urlGet}')\n")
        f.write(f"driver.maximize_window()\n")
        f.write(f"wait = WebDriverWait(driver, 10)\n")
        f.write(f"time.sleep(3)\n\n\n")
    except FileNotFoundError:
        print("file not found")
        f.close()

def matchChecker(fileName, incrementCounterOnEachCall, userInputDescription, userInputElement, userInputElementValue, userInputOperation, userInputOperationValue, destKeySelector, destValSelector, waitTime):
    # code here
    match userInputElement:
        case 'id':
            writeElementOperation(fileName, incrementCounterOnEachCall, userInputDescription, availSingleElementsDict['id'], userInputElementValue, userInputOperation, userInputOperationValue, destKeySelector, destValSelector, waitTime)
        case 'name':
            writeElementOperation(fileName, incrementCounterOnEachCall, userInputDescription, availSingleElementsDict['name'], userInputElementValue, userInputOperation, userInputOperationValue, destKeySelector, destValSelector, waitTime)
        case 'xpath':
            writeElementOperation(fileName, incrementCounterOnEachCall, userInputDescription, availSingleElementsDict['xpath'], userInputElementValue, userInputOperation, userInputOperationValue, destKeySelector, destValSelector, waitTime)
        case 'linktext':
            writeElementOperation(fileName, incrementCounterOnEachCall, userInputDescription, availSingleElementsDict['linktext'], userInputElementValue, userInputOperation, userInputOperationValue, destKeySelector, destValSelector, waitTime)
        case 'tagname':
            writeElementOperation(fileName, incrementCounterOnEachCall, userInputDescription, availSingleElementsDict['tagname'], userInputElementValue, userInputOperation, userInputOperationValue, destKeySelector, destValSelector, waitTime)
        case 'classname':
            writeElementOperation(fileName, incrementCounterOnEachCall, userInputDescription, availSingleElementsDict['classname'], userInputElementValue, userInputOperation, userInputOperationValue, destKeySelector, destValSelector, waitTime)
        case 'cssselector':
            writeElementOperation(fileName, incrementCounterOnEachCall, userInputDescription, availSingleElementsDict['cssselector'], userInputElementValue, userInputOperation, userInputOperationValue, destKeySelector, destValSelector, waitTime)
        case 'containstext':
            writeElementOperation(fileName, incrementCounterOnEachCall, userInputDescription, availSingleElementsDict['containstext'], userInputElementValue, userInputOperation, userInputOperationValue, destKeySelector, destValSelector, waitTime)
#For containstext need to give as //*[contains(text(), 'grt_tqa')]

def writeElementOperation(fileName, incrementCounterOnEachCall, userInputDescription, userInputElement, userInputElementValue, userInputOperation, userInputOperationValue, destKeySelector, destValSelector, waitTime):
    f = open(fileName, 'a')
    # getTimer function is called here, because to give manual sleep on each operation
    incrementCounterOnEachCallError = incrementCounterOnEachCall+"Error"
    try:
        f.write(f"try:\n")
        if userInputOperation == 'click' or userInputOperation == 'clear':
            f.write(f"\t{incrementCounterOnEachCall} = wait.until(EC.element_to_be_clickable((By.{userInputElement}, r'''{userInputElementValue}''')))\n")
            f.write(f"\t{incrementCounterOnEachCall}.{userInputOperation}()\n")
            f.write(f"\tprint('Execution : {userInputDescription}')\n")
        elif userInputOperation == 'drag-drop':
            f.write(f"\tdrag{incrementCounterOnEachCall} = wait.until(EC.visibility_of_element_located((By.{userInputElement}, r'''{userInputElementValue}''')))\n")
            f.write(f"\tdrop{incrementCounterOnEachCall} = wait.until(EC.visibility_of_element_located((By.{availSingleElementsDict[destKeySelector]}, r'''{destValSelector}''')))\n")
            f.write(f"\tActionChains(driver).drag_and_drop(drag{incrementCounterOnEachCall}, drop{incrementCounterOnEachCall}).perform()\n")
        elif userInputOperation == 'right-click':
            f.write(f"\trc{incrementCounterOnEachCall} = wait.until(EC.element_to_be_clickable((By.{userInputElement}, r'''{userInputElementValue}''')))\n")
            f.write(f"\tActionChains(driver).context_click(rc{incrementCounterOnEachCall}).{availOperationDict[userInputOperation]}()\n")
            f.write(f"\tprint('Execution : {userInputDescription}')\n")
        elif userInputOperation == 'scroll':
            f.write(f"\trc{incrementCounterOnEachCall} = wait.until(EC.visibility_of_element_located((By.{userInputElement}, r'''{userInputElementValue}''')))\n")
            f.write(f"\tActionChains(driver).{availOperationDict[userInputOperation]}(rc{incrementCounterOnEachCall}).perform()\n")
            f.write(f"\tprint('Execution : {userInputDescription}')\n")
        else:
            f.write(f"\t{incrementCounterOnEachCall} = wait.until(EC.element_to_be_clickable((By.{userInputElement}, r'''{userInputElementValue}''')))\n")
            f.write(f"\t{incrementCounterOnEachCall}.{availOperationDict[userInputOperation]}('{userInputOperationValue}')\n")
            f.write(f"\tprint('Execution : {userInputDescription}')\n")
        f.write(f"except Exception as {incrementCounterOnEachCallError}:\n")
        f.write(f"\tprint('Received an exception : ', {incrementCounterOnEachCallError})\n")
        f.write(f"\tresult = 'FAIL'\n")
        f.write(f"\tcaptureResponse = apiCall('{fileName}', productName, result)\n")
        f.write(f"\tprint(captureResponse[0].text.strip(), \'testRunId :\', captureResponse[1], \'resultCode :\', captureResponse[0].status_code)\n")
        f.write(f"\tdriver.quit()\n")
        f.write(f"\tquit()\n\n")
        #f.write(f"time.sleep({waitTime})\n\n")
    except FileNotFoundError:
        print("file not found")

def endOfFile(fileName):
    f = open(fileName, 'a')
    f.write(f"result = 'PASS'\n")
    f.write(f"captureResponse = apiCall('{fileName}', productName, result)\n")
    f.write(f"print(captureResponse[0].text.strip(), \'testRunId :\', captureResponse[1], \'resultCode :\', captureResponse[0].status_code)\n")
    f.write("driver.quit()\n")
    f.write("quit()")
