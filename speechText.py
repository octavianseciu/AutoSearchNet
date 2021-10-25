import speech_recognition as sr
import pyaudio
from pygame import mixer
import pygame
import sys
from gtts import gTTS
from playsound import playsound
import time

def speechTtext(timeout):
    '''inregistreaza sunetul utilizand microfonul clientului'''
    recognizer = sr.Recognizer() # initializeaza inregistrarea
    try:
        print('play')
        # gestioneaza deschiderea/inchiderea microfonului
        with sr.Microphone() as source: 
            # reduce zgomotul de fond
            recognizer.adjust_for_ambient_noise(source, duration=1) 
            # inregistreaza cu o durata data de parametrul timeout
            recorded_audio = recognizer.listen(source, timeout=timeout) 
        print('stop')

        ''' transcriptul textului in limba romana'''
        text = recognizer.recognize_google(
            recorded_audio,
            language="ro-RO"
        )
        return format(text)
    except Exception as ex:
        print(ex)


def redareAudio(text):
    '''preluarea textului si salvarea in format mp3
    '''
    mp3 = gTTS(text=text, lang='ro')
    file = 'static/translator.mp3'
    mp3.save(file)
    '''redarea vocala 
    este limitata de token-procesor instalat in windows
    pt limba romana nu este disponibil un Tokenizer in Windows 10'''
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load((file))
    pygame.mixer.music.play()
    SONG_END = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(SONG_END)
    while True:
        for event in pygame.event.get():
            if event.type == SONG_END:
                print("the song ended!")
                pygame.quit()
                sys.exit()
