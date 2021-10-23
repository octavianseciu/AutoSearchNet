import time
from speechText import speechTtext


def text_comanda_sec(links):
    x = 0
    while True:
        x += 1
        time.sleep(1)
        comanda = speechTtext(5)
        if comanda != None:
            comanda = str(comanda).lower()
            if 'deschide' in comanda:
                links.append(1)
                comanda = comanda.replace('deschide', ' ')
                comanda = comanda.strip()
                return comanda, 'deschide'
            elif 'revenire' in comanda:
                return comanda, 'revenire'
            elif x == 4:
                return None, None
        elif x == 3:
            return None, None


def nrTabrezultat(text):
    import re
    match = re.search('\d{1,2}', text)
    if match:
        return int(match.group())
    else:
        x = -1
        for i in ['unu', 'unul', 'doi', 'trei', 'patru', 'cinci', 'șase', 'șapte', 'opt', 'noua', 'zece']:
            x += 1
            if text == i:
                return x


def openTabrezultat(dateYoutube, nr):
    x = -1
    for i in dateYoutube:
        x += 1
        if x == nr:
            import webbrowser
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register(
                'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(dateYoutube[x-1][0])
            # webbrowser.open(dateYoutube[x][0], autoraise=True)
            return dateYoutube[x-1][0]
