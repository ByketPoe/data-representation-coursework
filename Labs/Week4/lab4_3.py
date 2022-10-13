import requests

def readbooks(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Request Error: " + str(response.status_code)

if __name__ == "__main__":
    url = "http://andrewbeatty1.pythonanywhere.com/books"
    print(readbooks(url))