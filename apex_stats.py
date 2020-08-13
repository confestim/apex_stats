import requests

class apex():

    def __init__(self, apikey=None):
        self.apikey = apikey

    def recentlyPlayed(self, userId, userPlatform="origin"):
        primReq = requests.get(f" https://public-api.tracker.gg/v2/apex/standard/profile/{userPlatform}/{userId}", headers={"TRN-Api-Key":f"{self.apikey}"})
        # we check whether the account exists or not
        if str(primReq) == "<Response [200]>":
            charactersPlayed = []
            # we make a list using a for loop
            for i in range(len(primReq.json()["data"]["segments"])):
                segReq = primReq.json()["data"]["segments"][i]["metadata"]["name"]
                charactersPlayed.append(segReq)
            return charactersPlayed
        # we check whether the api key is working
        elif str(primReq) == "<Response [401]>":
            return print("ApiKey is wrong")
        else:
            return print("This account doesn't exist")
