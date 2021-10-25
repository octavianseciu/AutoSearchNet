from flask import Flask, render_template, redirect, url_for, request
from speechText import *
from autowin import *
from searchYoutube import *

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')


sugestiiCautare = []
dateYoutube = []
comanda = None


@app.route('/')
def home():
    return redirect(url_for('my_page'))


@app.route('/my_page')
def my_page():
    return render_template('my_page.html', errorcomandaVocala='')


@app.route('/rezultat', methods=['GET', 'POST'])
def rezultat():
    return render_template('rezultat.html')


@app.route('/my_page', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        global sugestiiCautare, dateYoutube, comanda
        # print(request.form)
        if request.form['comanda_1'] == 'ComandaVocala1':
            x = 0
            while True:
                x += 1
                try:
                    comanda = speechTtext(7)
                except:
                    pass
                time.sleep(0.5)
                if comanda != None:
                    break
            youtubesearch = YoutubeSearch(comanda)
            sugestiiCautare = youtubesearch.suggestions
            dateYoutube = youtubesearch.videos
            # print(comanda, sugestiiCautare, dateYoutube)
            return render_template('rezultat.html', sugestiiCautare=sugestiiCautare, dateYoutube=dateYoutube, comanda=comanda)
        
        elif request.form['comanda_1'] == 'ComandaVocala3':
            sugestiiLinks = ','.join(sugestiiCautare)
            # print('sugestiiCautare', sugestiiCautare)
            try:
                redareAudio(sugestiiLinks)
            except:
                pass
            return render_template('rezultat.html', sugestiiCautare=sugestiiCautare, dateYoutube=dateYoutube, comanda=comanda)
        
        elif request.form['comanda_1'] == 'ComandaVocala4':
            titluYutube = []
            for i in dateYoutube:
                titluYutube.append(i[1])
            titluYutube = ','.join(titluYutube)
            try:
                redareAudio(titluYutube)
            except:
                pass
            return render_template('rezultat.html', sugestiiCautare=sugestiiCautare, dateYoutube=dateYoutube, comanda=comanda)
        elif request.form['comanda_1'] == 'ComandaVocala2':
            nr, comanda = comandaOpenWebYoutube()
            if comanda != None and comanda == 'deschide':
                nr = nrLinkrezultat(nr)
                print(nr)
                if nr != None:
                    tab = openTabrezultat(dateYoutube, nr)
                    print(tab)
                    time.sleep(6)
                    x = Tab('YouTube')
                    while True:
                        try:
                            comanda = str(speechTtext(3))
                            print(comanda)
                        except:
                            pass
                        if comanda != None:
                            comanda = comanda.strip()
                            comanda = comanda.lower()
                            x.comenziYoutube(comanda)
                            if comanda == 'întoarce':
                                break
                        time.sleep(0.1)
                    try:
                        w = Application(backend='uia').connect(path='chrome.exe', title_re='autoSEARCHNet')
                        w.wrapper_object()
                        w.wait('visible')
                        w.click_input()
                    except:
                        pass
                    return render_template('rezultat.html', sugestiiCautare=sugestiiCautare, dateYoutube=dateYoutube)
                else:
                    return render_template('rezultat.html', sugestiiCautare=sugestiiCautare, dateYoutube=dateYoutube, errorcomandaVocala='Comanda vocala nepotrivita\nRepetati inregisrarea comanzii vocale')
            elif comanda != None and comanda == 'stop':
                dateYoutube.clear()
                sugestiiCautare.clear()
                return render_template('my_page.html', errorcomandaVocala='')
            else:
                return render_template('my_page.html', errorcomandaVocala='Comanda vocala nepotrivita\nRepetati inregisrarea comanzii vocale')


if __name__ == "__main__":
    app.run(debug=True)
