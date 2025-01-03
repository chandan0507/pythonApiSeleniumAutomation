availSingleElementsDict = {'id': 'ID', 'name': 'NAME', 'xpath': 'XPATH', 'linktext': 'LINK_TEXT', 'tagname': 'TAG_NAME', 'classname': 'CLASS_NAME', 'cssselector': 'CSS_SELECTOR', 'q': 'quit()'}
availOperationDict = {'click': 'click', 'input': 'send_keys', 'drag-drop' : 'drag_and_drop'}

def writeProdUrl(fileName, getProductName, urlGet):
    f = open(fileName, "a")
    try:
        f.write("import time\n")
        f.write("from postApiCall import apiCall\n")
        f.write("from selenium import webdriver\n")
        f.write("from selenium.webdriver.common.by import By\n\n")
        f.write(f"productName = '{getProductName}'\n\n")
        f.write("driver = webdriver.Chrome()\n")
        f.write(f"driver.get('{urlGet}')\n")
        f.write(f"time.sleep(3)\n")
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

def writeElementOperation(fileName, incrementCounterOnEachCall, userInputDescription, userInputElement, userInputElementValue, userInputOperation, userInputOperationValue, destKeySelector, destValSelector, waitTime):
    f = open(fileName, 'a')
    # getTimer function is called here, because to give manual sleep on each operation
    incrementCounterOnEachCallError = incrementCounterOnEachCall+"Error"
    try:
        f.write(f"try:\n")
        if userInputOperation == 'click':
            f.write(f"\t{incrementCounterOnEachCall} = driver.find_element(By.{userInputElement}, r'''{userInputElementValue}''')\n")
            f.write(f"\t{incrementCounterOnEachCall}.{userInputOperation}()\n")
            f.write(f"\tprint('Execution : {userInputDescription}')\n")
        elif userInputOperation == 'drag-drop':
            f.write(f"\tdrag{incrementCounterOnEachCall} = driver.find_element(By.{userInputElement}, r'''{userInputElementValue}''')\n")
            f.write(f"\tdrop{incrementCounterOnEachCall} = driver.find_element(By.{destKeySelector}, r'''{destValSelector}''')\n")
            f.write(f"\tActionChains(driver).drag_and_drop(drag{incrementCounterOnEachCall}, drop{incrementCounterOnEachCall}).perform()\n")
        else:
            f.write(f"\t{incrementCounterOnEachCall} = driver.find_element(By.{userInputElement}, r'''{userInputElementValue}''')\n")
            f.write(f"\t{incrementCounterOnEachCall}.{availOperationDict[userInputOperation]}('{userInputOperationValue}')\n")
            f.write(f"\tprint('Execution : {userInputDescription}')\n")
        f.write(f"except Exception as {incrementCounterOnEachCallError}:\n")
        f.write(f"\tprint('Received an exception : ', {incrementCounterOnEachCallError})\n")
        f.write(f"\tresult = 'FAIL'\n")
        f.write(f"\tcaptureResponse = apiCall('{fileName}', productName, result)\n")
        f.write(f"\tprint(captureResponse[0].text.strip(), \'testRunId :\', captureResponse[1], \'resultCode :\', captureResponse[0].status_code)\n")
        f.write(f"\tdriver.quit()\n")
        f.write(f"\tquit()\n")
        f.write(f"time.sleep({waitTime})\n\n")
    except FileNotFoundError:
        print("file not found")

def endOfFile(fileName):
    f = open(fileName, 'a')
    f.write(f"result = 'PASS'\n")
    f.write(f"captureResponse = apiCall('{fileName}', productName, result)\n")
    f.write(f"print(captureResponse[0].text.strip(), \'testRunId :\', captureResponse[1], \'resultCode :\', captureResponse[0].status_code)\n")
    f.write("driver.quit()\n")
    f.write("quit()")