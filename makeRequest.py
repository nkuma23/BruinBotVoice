import requests

#takes in an int num and calls post request to dispense that gift
def dispense(num):
    numToWord = {1:"one", 2:"two", 3:"three", 4:"four"}
    url = 'http://192.168.0.101:5000/dispense'
    try:
        requests.post(url, json={'bin':numToWord[num]})
    except:
        print(f"Error dispensing gift {num}")

def callEmotion(emotion):
    url = 'http://192.168.0.101:5000/face'
    try:
        requests.post(url, json={'emotion':emotion, 'duration':'50'})
    except:
        print(f"Error calling emotion")




requests.post("http://192.168.0.101:5000/dispense", json={'bin':'two'})