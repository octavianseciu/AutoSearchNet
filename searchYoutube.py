import time
from speechText import speechTtext
import re
import webbrowser
from youtubesearchpython import VideosSearch
from youtubesearchpython import Suggestions


class YoutubeSearch:
    def __init__(self, comanda):
        self.comanda = comanda

    @property
    def suggestions(self):
        suggestions = Suggestions(language='en', region='ro', )
        text = suggestions.get(self.comanda)
        text = ','.join(text['result'])
        sugestiiCautare = text.split(',')
        return sugestiiCautare

    @property
    def videos(self):
        try:
            videosSearch = VideosSearch(self.comanda, limit=10)
            dateYoutube = []
            x = -1
            for i in videosSearch.result()['result']:
                dateYoutube += [[]]
                x += 1
                dateYoutube[x].append(i['link'])
                dateYoutube[x].append(i['title'])
                descriere = i['descriptionSnippet'][0]['text']
                descriere = ''.join(descriere)
                dateYoutube[x].append(descriere)
                dateYoutube[x].append(i['duration'])
                dateYoutube[x].append(i['publishedTime'])
            return dateYoutube
        except:
            pass
        finally:
            return dateYoutube


def comandaOpenWebYoutube():
    '''returneaza nr link-ului din rezultate si 
    textul comenzii vocale
    asigura o bucla(limitata la x==3) privind speechTtext 
    si verifica 2 comenzi 'deschide' si 'stop'
    '''
    x = 0
    while True:
        x += 1
        time.sleep(1)
        comanda = speechTtext(5)
        if comanda != None:
            comanda = str(comanda).lower()
            if 'deschide' in comanda:
                nrLink = comanda.replace('deschide', ' ')
                nrLink = nrLink.strip()
                return nrLink, 'deschide'
            elif 'stop' in comanda:
                return comanda, 'stop'
            elif x == 4:
                return None, None
        elif x == 3:
            return None, None


def nrLinkrezultat(nrLink):
    '''
    verifica rezultatul comandaOpenWebYoutube()[0] si 
    returneaza int un numar de la 1 la 10'''
    match = re.search('\d{1,2}', nrLink)
    if match:
        return int(match.group())
    else:
        x = 0
        for i in ['unu', 'doi', 'trei', 'patru', 'cinci', 'șase', 'șapte', 'opt', 'noua', 'zece']:
            x += 1
            if nrLink == i:
                return x


def openTabrezultat(dateYoutube, nr):
    '''realizeaza deschiderea in Chrome a linkului indicat de
    parametrul nr
    returneaza link-ul
    '''
    x = -1
    for i in dateYoutube:
        x += 1
        if x == nr:
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register(
                'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(dateYoutube[x-1][0])
            # webbrowser.open(dateYoutube[x][0], autoraise=True)
            return dateYoutube[x-1][0]
