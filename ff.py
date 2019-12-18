print("Welcome\n")


QB=['qb1','qb2','qb3',]
RB=['rb1','rb2','rb3',]

def team1(players):
    return players

results={}
counter=1
while counter in range(1,3):
    firstpick=team1(input("Enter player name: "))
    firstcount=("QB",counter)
    secondpick=team1(input("Enter player name: "))
    counter +=1
    secondcount=("QB",counter)
    if counter == 2:
        break

    

print("Your team is")

print(firstpick,firstcount,'\n')
print(secondpick,secondcount)