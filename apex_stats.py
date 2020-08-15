import requests
import datetime

class singleStats():

    def __init__(self, apikey=None):
        if not apikey:
            raise ValueError("Please enter apikey")
        else:
            testReq = requests.get(f"https://public-api.tracker.gg/v2/apex/standard/profile/origin/test", headers={"TRN-Api-Key":f"{apikey}"})

            if str(testReq) == "<Response [401]>":
                raise ValueError("ApiKey is wrong")
            else:
                self.apiKey = apikey 

    def recentlyPlayed(self, userId : str, userPlatform="origin"):
    
        primReq = requests.get(f"https://public-api.tracker.gg/v2/apex/standard/profile/{userPlatform}/{userId}", headers={"TRN-Api-Key":f"{self.apiKey}"})
        # we check whether the account exists or not

        if str(primReq) == "<Response [200]>":
            charactersPlayed = []

            # we make a list using a for loop

            for i in range(len(primReq.json()["data"]["segments"])):
                segReq = primReq.json()["data"]["segments"][i]["metadata"]["name"]
                charactersPlayed.append(segReq)
            charactersPlayed.remove("Lifetime")
            return charactersPlayed

        # we check whether the api key is working

        else:
            raise Exception("This account doesn't exist")

    def matchHistory(self, userId : str, gameCount : int, userPlatform="origin"):

        primReq = requests.get(f"https://public-api.tracker.gg/v2/apex/standard/profile/{userPlatform}/{userId}/sessions", headers={"TRN-Api-Key":f"{self.apiKey}"})
        segReq = primReq.json()
        if str(primReq) == "<Response [200]>":

            data = []

            for i in range(gameCount):
                matchDict = dict() 
                matchDict["legend"] = segReq['data']['items'][i]["matches"][0]["metadata"]["character"]["displayValue"]
                matchDict["kills"] = segReq['data']['items'][i]['stats']['kills']["value"]
                matchDict["duration"] = float(segReq['data']['items'][i]['metadata']['duration']['value'][3:].replace(':', '.'))
                data.append(matchDict)
            return data
        else:
            raise Exception("This account doesn't exist")
