print("Welcome\n")
PlayerPool={
    'QB':{
        'qb1':'Pat Mahomes',
        'qb2':'Russell Wilson',
        'qb3':'Lamar Jackson',
    },
    'RB':{
        'rb1':'Christian Mccafferey',
        'rb2':'Chris Carson',
        'rb3':'Leonard Fournette',
    }
}
def team1(players):
    return players

results={}
counter=1
while counter in range(1,3):
    firstpick=team1(input("Enter player name: "))
    if firstpick in PlayerPool:
        firstpick = PlayerPool.QB.get('qb1')
        firstcount = PlayerPool.QB.get('Pat Mahomes')
    else:firstcount=("QB",counter)
    secondpick=team1(input("Enter player name: "))
    counter +=1
    secondcount=("QB",counter)
    if counter == 2:
        break

    

print("Your team is:\n")

print(firstpick,firstcount,'\n')
print(secondpick,secondcount,'\n')
