import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(url)

print (response.text)