# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from riotwatcher import LolWatcher, ApiError
from PIL import Image
import requests
from io import BytesIO


def getAPI_key():
    f = open("../key.txt", "r")
    return f.read()


lol_watcher = LolWatcher(getAPI_key())

my_region = 'euw1'
me = lol_watcher.summoner.by_name(my_region, 'Wadget')

test = lol_watcher.match.matchlist_by_puuid("europe", me["puuid"], queue=420)
print(test)


def getSummonerName(puuid):
    summoner = lol_watcher.summoner.by_puuid("euw1", puuid)
    return summoner["name"]


def printMatch(matchId):
    match = lol_watcher.match.by_id("europe", matchId)
    print(match["info"]["teams"])
    print(match["metadata"]["participants"])
    for i in range(len(match["metadata"]["participants"])):
        getSummonerName(match["metadata"]["participants"][i])


def winrate(wins, losses):
    return 5

# printMatch("EUW1_5772977953")


match = lol_watcher.match.by_id("europe", "EUW1_5772977953")
print(match["info"]["gameDuration"]/60)
# print(match["info"]["teams"])
# print(match["metadata"]["participants"])


def getGameDuration(game):
    return game["info"]["gameDuration"]/60

#lol_watcher.summoner.by_puuid(region, encrypted_puuid)

# print(match["info"]["teams"][0]["win"])


def playerSide(participants, player):
    # return string "blue" if player is on blue side, "red" if on red side
    # "player not found" if player is in neither team
    #match=lol_watcher.match.by_id("europe", gameId)
    for i in range(len(participants)):
        if(participants[i]) == player:
            if i < 5:
                return "blue"
            elif i<10:
                return "red"
            else:
                return "player not found"
    


def playerWinMatch(result, participants, player):
    # return True if player won, false if lost
    #match=lol_watcher.match.by_id("europe", gameId)
    if playerSide(participants, player) == "blue":
        return result[0]
    if playerSide(participants, player) == "red":
        return result[1]
# print(playerWinMatch("EUW1_5772977953","Wadget"))


def calculateWinrate(player, n):
    # bon, il faut compter les remake mtn, et faudra mettre + de param pour rendre
    # la fct g??n??rique
    games = lol_watcher.match.matchlist_by_puuid(
        "europe", me["puuid"], queue=420, count=n)
    wins = 0
    total = 0
    for i in range(len(games)):
        game = lol_watcher.match.by_id("europe", games[i])
        participants = []
        j=0
        for j in range(len(match["metadata"]["participants"])):
            participants = participants + [getSummonerName(game["metadata"]["participants"][j])]

        gameResult = [game["info"]["teams"][0]
                      ["win"], game["info"]["teams"][1]["win"]]
        if (game["info"]["gameDuration"]/60) > 5.0:

            if(playerWinMatch(gameResult, participants, player) == True):
                wins = wins+1
                total = total+1
            if(playerWinMatch(gameResult, participants, player) == False):
                total = total+1
    return (wins/total)*100


print(calculateWinrate("Wadget", 20))


#response = requests.get("https://ddragon.leagueoflegends.com/cdn/11.14.1/img/profileicon/"+str(me["profileIconId"])+".png")
#img = Image.open(BytesIO(response.content)).show()
