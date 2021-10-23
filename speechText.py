import speech_recognition as sr
import pyaudio


def speechTtext(timeout):
    recognizer = sr.Recognizer()
    ''' recording the sound '''
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print(f"Recording for {timeout} seconds")
            recorded_audio = recognizer.listen(source, timeout=timeout)
            print("Done recording")
        ''' Recorgnizing the Audio '''
    except:
        pass
    try:
        print("Recognizing the text")
        text = recognizer.recognize_google(
            recorded_audio,
            language="ro-RO"
        )
        return format(text)
    except Exception as ex:
        print(ex)


def redareAudio(text):
    from gtts import gTTS
    from playsound import playsound
    import time
    var = gTTS(text=text, lang='ro')
    var.save('cauta_sugestii.mp3')

    from pygame import mixer
    import pygame
    import sys

    file = 'cauta_sugestii.mp3'
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
