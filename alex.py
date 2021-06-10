import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import google

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    
def intro():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=5:
        speak("Hi i am 'Alex' sir.... I am your personal assistant..Looks like you are not having a good sleep. Do you need bed time stories?")
        print("Hi i am 'Alex' sir.... I am your personal assistant..Looks like you are not having a good sleep. Do you need bed time stories?")
    elif hour>=6 and hour<=10:
        speak("Goodmorning sir.. i am 'Alex' .... your personal assistant...Hope you had a great sleep")
        print("Goodmorning sir.. i am 'Alex' .... your personal assistant...Hope you had a great sleep")
    elif hour>=10 and hour==12:
        speak("Goodmorning sir.i am 'Alex'...  your personal assistant..What you want me to do?")
        print("Goodmorning sir.i am 'Alex'...  your personal assistant..What you want me to do?")
    elif hour>=12 and hour<=18:
        speak("Goodafternoon sir....I am 'Alex'... your personal assistant... What you want me to do?")
        print("Goodafternoon sir....I am 'Alex'... your personal assistant... What you want me to do?")
    else:
        speak("Good evening sir.....I am 'Alex'... your personal assistant......What you want me to do? ")
        print("Good evening sir.....I am 'Alex'... your personal assistant......What you want me to do?")

def commandlistener():
    m=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        speak("Listening")
        m.pause_threshold=0.5
        audio=m.listen(source)
    try:
        print("Recognizing")
        speak("Recognizing")
        query=m.recognize_google(audio, language='en-in')
        print(f'User said {query}')
    except Exception as m:
        pass
        return("None")
    return query

def app_comm():
        if 'open minecraft' in query or 'open tlauncher' in query:
            print("Opening Minecraft")
            speak("Opening Minecraft")
            mc="C:\\Users\\Vandana\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
            os.startfile(mc)
            print("Minecraft is opened now")
            speak("Minecraft is opened now")
        elif 'open spotify' in query or 'spotify' in query:
            print("Opening Spotify")
            speak('Opening spotify')
            os.system('spotify')
            print('Spotify is opened now')
            speak('Spotify is opened now')
        

def webopen():
        if "open discord" in query:
            print("Opening discord ")
            speak("Opening discord")
            webbrowser.open("https://discord.com/channels/@me")
            speak("Discord is open now")
            print("Discord is open now")
        elif "open youtube" in query :
            print("Opening youtube")
            speak("Opening youtube")
            webbrowser.open("https://www.youtube.com/")
            speak("Youtube is open now")
            print("Youtube is open now")
        elif "open github" in query or "open my github" in query:
            print("Opening github")
            speak("Opening github")
            webbrowser.open("https://github.com/")
            print("Github is open now")
            speak("Github is open now")
        elif "open stackoverflow" in query or "open stack overflow" in query:
            print("Stackoverflow is opening")
            speak("Stackoverflow is opening")
            webbrowser.open('https://stackoverflow.com/')
            print("Stackoverflow is open now")
            speak("Stackoverflow is open now")
        elif 'open classroom' in query or 'open google classroom' in query:
            print("opening classroom")
            speak("opening classroom")
            webbrowser.open('https://classroom.google.com/u/0/h')
            print('Classroom is opened now')
            speak('Classroom is opened now')
        elif 'open whatsapp' in query or 'whatsapp' in query or 'open whatsapp web' in query or 'whatsapp web' in query:
            print('Opening whatsapp')
            speak('Opening whatsapp')
            webbrowser.open('https://web.whatsapp.com/')
            print('Whatsapp is opened now')
            speak('Whatsapp is openned now')

def me():
    if 'alex' in query:
        speak('Yes sir')
        print('Yes sir')


if __name__== "__main__":
  intro()
  while True:
        query=commandlistener().lower()
        webopen()
        app_comm()
        me()
        if 'search wikepedia' in query or 'wikipedia' in query:
          try:
            if 'wikipedia' in query:
                print("Searching Wikipedia")
                speak("Searching Wikipedia")
                query=query.replace('wikipedia',"")
                results=wikipedia.summary(query,sentences=2)
                print(f'According to wikipedia {results}')
                speak(f'According to wikipedia {results}')
              
            elif 'search wikipedia' in query:
                print("Searching Wikipedia")
                speak("Searching Wikipedia")
                query=query.replace('search wikipedia',"")
                results=wikipedia.summary(query,sentences=1)
                print(f'According to wikipedia {results}')
                speak(f'According to wikipedia {results}')
              
         
          except:
            print("Couldnt find anything regarding this in wikipedia")
            speak("Couldnt find anything regarding this in wikipedia")
        else:
            print('Pardon sir..Can you please repeat')
            speak('Pardon sir..Can you please repeat')
'''elif 'open google' in query or 'open search' in query:
    '''  