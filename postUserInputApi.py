from flask import jsonify, request
from writeFileProd import availSingleElementsDict, availOperationDict, writeProdUrl, matchChecker, endOfFile

def postUserInput():
    if request.method == 'POST':
        jsonData = request.get_json()
        # Below checks if jsonData['txnId'] has any value or not, if no value then retuns 402 response
        if not jsonData['txnId']:
            return jsonify({'errorMessage' : 'tnxId is null'}), 402
        if not(5<= len(jsonData['fileName']) <=20):
            return jsonify({'errorMessage' : 'fileName length should be between 5 & 20'}), 405
        if not jsonData['webUrl']:
            return jsonify({'errorMessage' : 'webUrl is null'}), 402
        if not jsonData['productName']:
            return jsonify({'errorMessage' : 'productName is null'}), 402
        for action in jsonData['actions']:
            if action['selectorKey'].lower().strip() not in availSingleElementsDict.keys():
                return jsonify({'errorMessage' : 'selectorKey is null'}), 402
            if not action['selectorValue']:
                return jsonify({'errorMessage' : 'selectorValue is null'}), 402
            if not action['waitTime']:
                return jsonify({'errorMessage' : 'waitTime is null'}), 402
            if action['optionKey'].lower().strip() not in availOperationDict.keys():
                return jsonify({'errorMessage' : 'optionKey is null'}), 402
            if not action['description']:
                return jsonify({'errorMessage' : 'description is null'}), 402
            if not action['optionValue']:
                pass
            if not action['destOptionKey']:
                pass
            if not action['destOptionVal']:
                pass
        if jsonData:
            provideResponse(jsonData['fileName'], jsonData['productName'], jsonData['webUrl'], jsonData['actions'])
            print(dict(jsonData))
        return jsonify({'errorMessage' : 'Success'}), 201

def provideResponse(fileName, productName, webUrl, jsonData):
    fileName = fileName.strip()
    fileNamepy = fileName+".py"
    print(f"Given fileName is {fileNamepy}")
    # Below will create the file with url, product name
    writeProdUrl(fileNamepy, productName, webUrl)
    count = 0
    for action in jsonData:
        incrementCounterOnEachCall = "element"
        incrementCounterOnEachCall = incrementCounterOnEachCall+str(count)
        selectorKeySender = action['selectorKey'].lower()
        selectorValSender = action['selectorValue']
        optionKeySender = action['optionKey'].lower()
        optionValSender = action['optionValue']
        destKeySelector = action['destOptionKey'].lower()
        destValSelector = action['destOptionVal'].lower()
        descriptionSender = action['description']
        waitTimeSender = action['waitTime']
        matchChecker(fileNamepy, incrementCounterOnEachCall, descriptionSender, selectorKeySender, selectorValSender, optionKeySender, optionValSender, waitTimeSender)
        count+=1
    endOfFile(fileNamepy)

# Below is the body for api, request. action is an array so multiple dictionary could be included

# {
#     "txnId" : "9721628",
#     "fileName" : "chand",
#     "webUrl" : "https://",
#     "productName" : "vocus",
#     "actions" : [
#         {
#             "selectorKey" : "Id",
#             "selectorValue" : "someButton",
#             "optionKey" : "something",
#             "optionValue" : "thisVal",
#             "destOptionKey" : "id",
#             "destOptionVal" : "Val",
#             "waitTime" : 10,
#             "description" : "click on button"
#         },
#         {
#             "selectorKey" : "name",
#             "selectorValue" : "event",
#             "optionKey" : "something",
#             "optionValue" : null,
#             "destOptionKey" : null,
#             "destOptionVal" : null,
#             "waitTime" : 10,
#             "description" : "click on button"
#         },
#         {
#             "selectorKey" : "link",
#             "selectorValue" : "aref",
#             "optionKey" : "something",
#             "destOptionKey" : null,
#             "destOptionVal" : null,
#             "optionValue" : "thisVal",
#             "waitTime" : 10,
#             "description" : "click on button"
#         }
#     ]
# }