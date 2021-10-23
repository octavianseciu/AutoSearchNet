from pywinauto import Desktop
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import time
import yaml


class Tab:
    def __init__(self, pagWeb):
        window = Desktop(backend="uia").windows()
        print([w.window_text() for w in window])
        name_client = [i for i in [w.window_text()
                                   for w in window] if pagWeb in i][0]
        app = Application(backend='uia').connect(title=name_client, timeout=10)

        name_app = name_client.replace('.', '  ')
        name_app = name_app.replace('-', ' ')
        name_app = name_app.split(' ')
        name_app = [i.capitalize() for i in name_app]
        nameWindowApp = ''.join(name_app)

        window = app.window(best_match=nameWindowApp)
        print('connect -->Window -->', name_client, '->', nameWindowApp)
        window.wrapper_object()
        window.set_focus()
        self.connect = window


    def comenziYoutube(self, comanda):
        try:
            a = 0
            with open('data/comenzi.yaml', 'r', encoding='utf8') as f:
                data = yaml.safe_load(f)
            for q, w in data.items():
                for k in w:
                    self.connect.set_focus()
                    if comanda in k:
                        if comanda == 'tare' or comanda == 'sus':
                            print(comanda)
                            send_keys('{UP}')
                            time.sleep(1)
                            send_keys('{UP}')
                        elif comanda == 'încet' or comanda == 'jos':
                            send_keys('{DOWN}')
                            time.sleep(0.2)
                            send_keys('{DOWN}')
                        elif comanda == 'creează':
                            send_keys('{ENTER}')
                            send_keys('AutoSearchNet')
                            time.sleep(1)
                            send_keys('{ENTER}')
                        elif comanda == 'revenire':
                            send_keys('^w^c')  # ctr+w
                        else:
                            self.connect[q].click_input()
                        a = 1
                        break
                if a == 1:
                    break
        except:
            pass
