import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("goodmorning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("Hello Boss I am Veronica and tell me How may i assist you")

def takeCommand():
    '''It take microphone input from user'''

    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("listening.....")
        r.pause_threshold = 1#seconds of non speaking audio before we consider the speaking audio a phrase
        audio = r.listen(sourse)

    try:
        print("recognizing....")
        query =r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("say that again.....")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()  #converted to lower string

                                 #logic executing tasks based on query

        if 'wikipedia' in query:
          speak('searching wikipedia...')
          query = query.replace("wikipedia", "")
          results = wikipedia.summary(query, sentences=4)
          speak("According to wikipedia ")
          print(results)
          speak(results)

        elif 'open youtube' in query:
              webbrowser.open("youtube.com")
        elif 'open google' in query:
              webbrowser.open("google.com")
        elif 'open stack over flow' in query:
              webbrowser.open("stackoverflow.com")

