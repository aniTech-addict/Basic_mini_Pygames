import requests

url = "https://random-word-api.herokuapp.com/word"

def get_word():
    response = requests.get(url)
    word = response.json()[0]
    return word

