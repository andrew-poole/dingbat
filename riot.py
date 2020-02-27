import requests
import json
devkey="RGAPI-d37d5a51-59c9-403b-b12f-844efcefaf06"#this is the devkey
myID = input('Enter Summoner Name: ')

url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{myID}?api_key={devkey}"
response = requests.get(url)
data = response.text

parsed = json.loads(data)
mysummonerId = parsed ["accountId"]
indexy = 0

def dingusFetchMatches(): 
    url=f"https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/{mysummonerId}?api_key={devkey}&beginIndex={indexy}00"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    matches = parsed ["matches"]
    return matches


matches = dingusFetchMatches()
matchlist = matches


while  len(matches)>0:
    indexy+=1
    matches = dingusFetchMatches()
    matchlist = matchlist + matches#adds it to list


lanecounts={'BOTTOM':0,'TOP':0,'JUNGLE':0,'MID':0,'NONE':0}
for match in matchlist:
    if "lane" in match:
        lane=match["lane"]
        lanecounts[lane]+=1
maxlane = ''
maxgames = 0
for lane in lanecounts:
    if lanecounts[lane]>maxgames:
        maxgames = lanecounts[lane]
        maxlane = lane


print("You've played", len(matchlist),"games")
print("You play",maxlane,"lane the most at",maxgames,"games!")
print("You've played for about", len(matchlist)*30, "minutes since season 5. What a dang loser")