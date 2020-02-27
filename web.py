import webbrowser,time

one='https://twitter.com/home'
two='https://old.reddit.com/'
three='https://www.youtube.com/'
four='https://www.twitch.tv/directory/game/League%20of%20Legends'
five='https://play.google.com/music/listen#/home'


for x in range(0,10):
    if x==0:
        webbrowser.open(one)
    elif x==1:
        webbrowser.open(two)
    elif x==2:
        webbrowser.open(three)
    elif x==3:
        webbrowser.open(four)
    elif x==4:
        webbrowser.open(five)

time.sleep(1)
print('Aight have fun')
