from pywinauto import Desktop
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import time
import yaml
from fuzzywuzzy import process


class Tab:
    def __init__(self, pagWeb):
        '''
        1.asigura conectarea la pagina web-youtube deschisa
        2.pagina web-youtube se formateaza ca obiect pentru a se accesa
        metode pywinauto
        '''
        window = Desktop(backend="uia").windows()
        print([w.window_text() for w in window])
        name_client = [i for i in [w.window_text()
                                   for w in window] if pagWeb in i][0]
        app = Application(backend='uia').connect(title=name_client, timeout=10)

        # se transforma name_client in format acceptat de metoda
        name_app = name_client.replace('.', '  ')
        name_app = name_app.replace('-', ' ')
        name_app = name_app.split(' ')
        name_app = [i.capitalize() for i in name_app]
        nameWindowApp = ''.join(name_app)
        # accesam clasa pywinauto.application si
        # metoda set_focus care initializeaza parintele window
        window = app.window(best_match=nameWindowApp)
        print('connect -->Window -->', name_client, '->', nameWindowApp)
        window.wrapper_object()
        window.set_focus()
        self.connect = window

    def comenziYoutube(self, comanda):  # variabila de tip str
        try:
            # se deserializeaza datele fisierului yaml --> dict
            with open('data/comenzi.yaml', 'r', encoding='utf8') as f:
                data = yaml.safe_load(f)
            c = []
            for q, w in data.items():
                c += w
            # daca comanda vocala exista in {data} se trimit key acceptate de pagina youtub, sau
            # actiuni ale mouse-lui pt zone sau butoane ale paginii youtube prin self.connect[q]
            highest = process.extractOne(comanda, c)
            if highest[1] > 80:
                print(comanda)
                key = [key for key in data if highest[0] in data[key]][0]
                self.connect.set_focus()
                if highest[0] == 'tare' or highest[0] == 'sus':
                    self.connect['Playerul video You tube'].set_focus()
                    send_keys('{UP}')
                    time.sleep(0.1)
                    send_keys('{UP}')
                elif highest[0] == 'încet' or highest[0] == 'jos':
                    self.connect['Playerul video You tube'].set_focus()
                    send_keys('{DOWN}')
                    time.sleep(0.2)
                    send_keys('{DOWN}')
                elif highest[0] == 'creează':
                    self.connect['Playerul video You tube'].set_focus()
                    send_keys('{ENTER}')
                    send_keys('AutoSearchNet')
                    time.sleep(1)
                    send_keys('{ENTER}')
                elif highest[0] == 'întoarce':
                    self.connect['Playerul video You tube'].set_focus()
                    send_keys('^w^c')  # ctr+w
                else:
                    print(highest[0], key)
                    self.connect['Playerul video You tube'].set_focus()
                    self.connect[key].click_input()

        except:
            pass
