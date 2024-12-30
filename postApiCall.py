import requests
import json
import time

testRunId = int(time.time())
executionTime = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())

def apiCall(testCaseName, product, result):
    testCaseName = testCaseName.replace('.py', '')
    headers = {'content-type': 'application/json'}
    url = 'http://10.0.1.127:8081/post_test'
    data = {"TEST_RUN_ID": testRunId, "TEST_CASE_NAME": testCaseName, "PRODUCT": product, "EXECUTION_TIME": executionTime, "RESULT": result}

    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response, testRunId