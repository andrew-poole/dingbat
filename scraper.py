import requests, bs4
res=requests.get('https://twitter.com/dncks10')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)

'<img alt="Image" draggable="true" src="https://pbs.twimg.com/media/EK9leBJUUAEL7eO?format=png&amp;name=900x900" class="css-9pa8cd">'
