import requests
import time
from bs4 import BeautifulSoup

url = "https://shop.doverstreetmarket.com/dsm-sale/new-additions"

chatID = "635598675"
token = "533166914:AAEdWHy_pOTtFURFW0rm9vm4gtht82zaMjc"

###############~SEND MESSAGE TO CHAT WITH ANTON~################

def sendMessageToChat(message):
    METHOD_NAME = "sendMessage"
    url = "https://api.telegram.org/bot"+token+"/"+METHOD_NAME + "?chat_id=" + chatID + "&text=" + message
    response = requests.get(url)
    print("request to :   " + url)
    print(response.text)

def getListFromUrl(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imgs = soup.findAll('img')
    test = soup.findAll("h2")
    aList = []
    for i in test:
            aList.append(i.a.unwrap())
    output = [x["title"] for x in aList]
    return output

def isNotSameList(first_List, second_List):
    if len(first_List) != len(second_List):
        return True
    if len(first_List) == len(second_List):
        if first_List != second_List:
            return True
    return False


def runTheProgramm():
    baseList = getListFromUrl(url)
    while(True):
        newList = getListFromUrl(url)
        time.sleep(60)
        if(isNotSameList(baseList, newList)):
            sendMessageToChat("hallo")
    
                
runTheProgramm()









