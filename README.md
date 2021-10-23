# AutoSearchNet
Proiect AutoSearchNet
## Descriere proiect 
este  o aplicație web WSGI(interfața de gateway a serverului web, standard Python) folosind automatizarea interfeței grafice Microsoft Windows. Permite trimiterea de acțiuni ale mouse-ului și tastaturii către ferestre de dialog și controale. 
Contine suport pentru motorul de recunoaștere a vorbirii / API. Se utilizeaza comanda vocala pentru actionarea motoarelor Youtub, care cauta videoclipuri, obtine informatii despre acestea si sugestii de cautare.
Rezultatele sunt afisate,redate vocal, cu posibilitatea deschiderii paginii web dorite (cu continut youtube) si a controlului  acesteia.
## Dependente si Instalare module
AutoSearchNet este dependent de Python si Windows. De asemenea, leagă și încorporează mai multe alte biblioteci mai mici: Flask, Pywinauto, SpeechText, Pyaudio,Webbrowser, Youtubesearchpython, Pygame,Time, Sys, 
## Structura aplicației
* AutoSearchNet
		-static
		          	-imagini.png, jpg
		-templates (crearea paginilor cu Jinja, HTML și CSS )
			- index.html
			-my_page.html
			-rezultat.html
		-auto_search.py (codul principal al aplicației, serverul care direcționea utilizatorul către pagina de pornire și către pagina de 					  rezultate )
		-searchYoutube.py
		-autowin.py
		-speechText.py
## Utilizare
Dupa instalare si pornirea serverului din auto_search.py, aplicatia prezinta in pagina web/my_page butonul “citeste mai mult” pentru a accesa prezenta informare despre proiect.
Central, exista butonul de pornire a inregistrarii comenzilor vocale, avand un background image intuitiv.
Accesarea butonului, activeaza microfonul incorporat in masina de lucru(PC), se inregistreaza vocea cu o frecventa a duratei de 5sec si pauza de 2sec, in bucla, pana la identificarea unei voci, respectiv inregistrari. In baza transriptului se cauta rezultate si sugestii in aplicatia youtube si se prezinta conform sablonului rezultat.htlm.
Rezultatele sunt afisate in format tabelar cu descriere detaliata: Link, Titlu, Desciere, Durata, Data Publicarii. In acelasi timp sunt prezentate si alte sugestii de cautare apropiate cautarii initiale.
Utilizatorul are optiunea redarii audio atat a rezultatelor cat si a sugestiilor.
Desciderea paginii web/youtube se face prin comanda vocala specificata, actionand butonul dedicat, care se efectueaza in Chrome. 
Pentru pagina deschisa sunt specificate comenzi vocale dedicate, care au rolul de manipulare a playerului video si de inchidere a paginii web.
Actiunile utilizatorului se pot repeta ori de cate ori se doreste.
