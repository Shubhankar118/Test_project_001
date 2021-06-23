import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib



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
    speak("Hello Sir I am Veronica and tell me How may i assist you")

def takeCommand():
    #It take microphone input from user and return string outputs

    r = sr.Recognizer() #recognizer helps to recognize the voice 
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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('zayns470@hmail.com','your-password')
    server.sendmail('zayns470@gmail.com', to, content)
    server.close() 



if __name__ == '__main__':
     wishMe()
while True:
        query = takeCommand().lower()  #converted to lower string
        
        
        #logic executing tasks based on query
        if 'wikipedia' in query:
          speak('searching wikipedia...')
          query = query.replace("wikipedia", "")
          results = wikipedia.summary(query, sentences=2)
          speak("According to wikipedia ")
          print(results)
          speak(results)

        elif 'open youtube' in query:
              webbrowser.open("youtube.com")
        elif 'open google' in query:
              webbrowser.open("google.com")
        elif 'open stack overflow' in query:
              webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir =  'D:\\NARUTO\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'open code ' in query:
            codePath = "C:\\Users\\Shubhankar\\AppData\\Local\\Program\Microsoft VS Code"
            os.startfile(codePath)
        elif 'send email' in query:
            try: 
                speak("what shound i say")
                content =takeCommand()
                to = "abhayr625@gmail.com"
                sendEmail(to, content)
                speak("email has been sent!")
            except Exception as e:
                #print(e)
                speak("sir right now you did not gave me permission to send emils")