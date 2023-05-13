import speech_recognition as srec
import pyttsx3 as pyt
import pywhatkit
import wikipedia


engine = pyt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def perintah():
    mendengar = srec.Recognizer()
    with srec.Microphone() as source:
        pyt.speak('hallo i am michelle, can i have you?')
        print('Listening...')
        mendengar.pause_threshold = 0.9
        suara = mendengar.listen(source, phrase_time_limit=5)
        try: 
            print('Loading...')
            layanan = mendengar.recognize_google(suara, language='id-ID')
            print(layanan)
        except: 
            pass
        return layanan

def talk(audio):
    engine.say(audio)
    engine.runAndWait

def run_michelle():
    layanan = perintah()
    print(layanan)
    if 'open' in layanan:
        video = layanan.replace('open', '')
        pyt.speak('opening' + video)
        print(video + ' opening...')
        pywhatkit.playonyt(video)

    if 'find out' in layanan:
        wiki = layanan.replace('find out', '')
        hasil = wikipedia.summary(wiki, sentences = 4)
        print(hasil)
        pyt.speak(hasil)
    
run_michelle()
    