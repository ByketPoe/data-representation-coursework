import requests

def readbook(url, id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    if response.status_code == 200:
        return response.text
    else:
        return "Request Error: " + str(response.status_code)

def createbook(url, book):
    response = requests.post(url, json=book)
    if response.status_code == 200:
        return response.text
    else:
        return "Request Error: " + str(response.status_code)

def updatebook(url, id, book):
    puturl = url + "/" + str(id)
    response = requests.put(puturl, json=book)
    if response.status_code == 200:
        return response.text
    else:
        return "Request Error: " + str(response.status_code)

def deletebook(url, id):
    delurl = url + "/" + str(id)
    response = requests.delete(delurl)
    if response.status_code == 200:
        return response.text
    else:
        return "Request Error: " + str(response.status_code)

if __name__ == "__main__":
    id = 92
    url = "http://andrewbeatty1.pythonanywhere.com/books"
    book = {"Author":"Sophie White","Price":7,"Title":"Where I End"}
    print(readbook(url, id))
    print(createbook(url, book))
    print(updatebook(url, id, book))
    print(deletebook(url, id))