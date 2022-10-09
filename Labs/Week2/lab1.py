# The purpose of this script is to parse an XML and print content from it to a CSV file.
# Author: Emma Farrell

import requests
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
#print(doc.toprettyxml(newl = ''))

# with open("trainxml.xml", "w") as xmlfp:
    # doc.writexml(xmlfp)
retrieveTags = ['TrainStatus', 'TrainLatitude', 'TrainLongitude', 'TrainCode', 'TrainDate', 'PublicMessage', 'Direction'] 
with open("week2_q6_train.csv", mode="w", newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    objTrainPosNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPosNode in objTrainPosNodes:
        # trainCodeNode = objTrainPosNode.getElementsByTagName("TrainCode").item(0)
        # trainCode = trainCodeNode.firstChild.nodeValue.strip()
        #print(trainCode)
        # trainLatNode = objTrainPosNode.getElementsByTagName("TrainLatitude").item(0)
        # trainLat = trainLatNode.firstChild.nodeValue.strip()
        dataList = []
        trainCode = objTrainPosNode.getElementsByTagName("TrainCode").item(0).firstChild.nodeValue.strip()
        if trainCode[0] == "D":
            for retrieveTag in retrieveTags:
                dataNode = objTrainPosNode.getElementsByTagName(retrieveTag).item(0)
                dataList.append(dataNode.firstChild.nodeValue.strip())
            train_writer.writerow(dataList)
        #print(trainLat)